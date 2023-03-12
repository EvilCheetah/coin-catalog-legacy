import { RabbitMQModule } from '@/modules';
import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { UsersModule } from './users/users.module';


@Module({
    imports: [
        ConfigModule.forRoot({}),
        RabbitMQModule,

        UsersModule
    ],
})
export class IamModule {}