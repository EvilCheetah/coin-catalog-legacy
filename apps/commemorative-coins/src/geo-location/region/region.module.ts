import { Module } from "@nestjs/common";
import { MikroOrmModule } from "@mikro-orm/nestjs";

import { Region } from "./entities/region.entity";
import { RegionService } from "./region.service";
import { RegionController } from "./region.controller";
import { RegionRepository } from "./region.repository";


@Module({
    imports:     [MikroOrmModule.forFeature([ Region ])],
    controllers: [RegionController],
    providers:   [RegionService, RegionRepository]
})
export class RegionModule {}