import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { MikroOrmModule } from '@mikro-orm/nestjs';

import { RabbitMQModule } from '@/modules';
import { get_db_config } from './config/database.config';
import { validationSchema } from './config/validation.schema';
import { GeolocationModule } from './geo-location/geo-location.module';


@Module({
    imports: [
        ConfigModule.forRoot({
            validationSchema,
            expandVariables: true
        }),
        MikroOrmModule.forRootAsync( get_db_config() ),
        RabbitMQModule,

        GeolocationModule
    ]
})
export class CommemorativeCoinsModule {}