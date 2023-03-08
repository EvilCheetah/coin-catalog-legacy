import { Injectable } from "@nestjs/common";
import { ConfigService } from "@nestjs/config";
import { RmqContext, RmqOptions, Transport } from "@nestjs/microservices";


@Injectable()
export class RabbitMQService
{
    constructor(
        private readonly config: ConfigService
    ) {}


    get_config(queue: string, noAck = false): RmqOptions
    {
        return {
            transport: Transport.RMQ,
            options: {
                urls:      [this.config.get<string>('RABBIT_MQ_URI')],
                queue:      this.config.get<string>(`RABBIT_MQ_${queue}_QUEUE`),
                noAck,
                persistent: true
            }
        }
    }


    ack(context: RmqContext)
    {
        const channel          = context.getChannelRef();
        const original_message = context.getMessage()

        channel.ack( original_message );
    }
}