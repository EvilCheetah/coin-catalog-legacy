import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { GeolocationModule } from './geo-location/geo-location.module';


@Module({
    imports: [
        ConfigModule.forRoot({
            envFilePath: '../environment/.env'
        }),

        GeolocationModule
    ]
})
export class CommemorativeCoinsModule {}