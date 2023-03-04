import { Module } from '@nestjs/common';
import { GeolocationModule } from './geo-location/geo-location.module';


@Module({
    imports: [
        GeolocationModule
    ]
})
export class CommemorativeCoinsModule {}