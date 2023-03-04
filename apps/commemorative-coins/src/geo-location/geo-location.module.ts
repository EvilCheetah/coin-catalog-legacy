import { Module } from "@nestjs/common";
import { RegionModule } from "./region/region.module";


@Module({
    imports: [
        RegionModule
    ]
})
export class GeolocationModule {}