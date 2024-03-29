import { Module } from "@nestjs/common";
import { DynamicModule } from "@nestjs/common";
import { ConfigModule } from "@nestjs/config";
import { ClientsModule } from "@nestjs/microservices";

import { RabbitMQOptions } from "./rabbit-mq.options";
import { RabbitMQService } from "./rabbit-mq.service";
import { get_queue_details } from './config/get-queue.config'


@Module({
    imports:   [ConfigModule],
    providers: [RabbitMQService],
    exports:   [RabbitMQService]
})
export class RabbitMQModule
{
    static register({ name }: RabbitMQOptions): DynamicModule
    {
        return {
            module:   RabbitMQModule,
            exports: [ClientsModule],
            imports: [
                ClientsModule.registerAsync([ get_queue_details(name) ])
            ]
        }
    }
}