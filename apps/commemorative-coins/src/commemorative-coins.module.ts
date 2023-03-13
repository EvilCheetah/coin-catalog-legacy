import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';

import { RabbitMQModule } from '@/modules';
import { validationSchema } from './config/validation.schema';
import { GeolocationModule } from './geo-location/geo-location.module';


@Module({
    imports: [
        ConfigModule.forRoot({
            validationSchema,
            expandVariables: true
        }),
        RabbitMQModule,

        GeolocationModule
    ]
})
export class CommemorativeCoinsModule {}