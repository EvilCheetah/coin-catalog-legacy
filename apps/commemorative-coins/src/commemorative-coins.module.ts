import { RabbitMQModule } from '@/modules';
import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { GeolocationModule } from './geo-location/geo-location.module';


@Module({
    imports: [
        ConfigModule.forRoot({
            envFilePath: './environment/.env',
        }),
        RabbitMQModule,

        GeolocationModule
    ]
})
export class CommemorativeCoinsModule {}