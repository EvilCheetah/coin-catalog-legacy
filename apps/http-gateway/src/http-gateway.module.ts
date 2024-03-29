import { Services } from '@/constants';
import { RabbitMQModule } from '@/modules';
import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { RegionController } from './controllers/region.controller';


@Module({
    imports: [
        ConfigModule.forRoot({
            envFilePath: './apps/http-gateway/environment/.env',
            expandVariables: true
        }),
        RabbitMQModule.register({ name: Services.CommemorativeCoinsService })
    ],
    controllers: [
        RegionController
    ]
})
export class HttpGatewayModule {}