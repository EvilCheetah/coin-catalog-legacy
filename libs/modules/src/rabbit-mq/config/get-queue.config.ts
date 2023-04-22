import { ConfigModule, ConfigService } from "@nestjs/config";
import { ClientsProviderAsyncOptions, Transport } from "@nestjs/microservices";


export function get_queue_details(name: string): ClientsProviderAsyncOptions
{
    return {
        name,
        useFactory: (config: ConfigService) =>
        ({
            transport: Transport.RMQ,
            options: {
                urls:  [config.get<string>('RABBIT_MQ_URI')],
                queue:  name
            }
        }),
        imports: [ConfigModule],
        inject:  [ConfigService]
    }
}