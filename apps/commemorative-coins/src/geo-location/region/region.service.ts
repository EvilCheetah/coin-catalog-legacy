import { Injectable } from "@nestjs/common";
import { CreateRegionDTO } from "./dto/create-region.dto";
import { UpdateRegionDTO } from "./dto/update-region.dto";
import { Region } from "./entities/region.entity";
import { RegionRepository } from "./region.repository";


@Injectable()
export class RegionService
{
    constructor(
        private readonly regionRepository: RegionRepository
    ) {}

    create(regionDTO: CreateRegionDTO): Promise<Region>
    {
        return this.regionRepository.create(regionDTO);
    }

    find_one(region_id: number): Promise<Region>
    {
        return this.regionRepository.find_one(region_id);
    }

    find_all(): Promise<Region[]>
    {
        return this.regionRepository.find_all();
    }

    update(updateRegionDTO: UpdateRegionDTO): Promise<Region>
    {
        return this.regionRepository.update(updateRegionDTO);
    }

    remove(region_id: number): Promise<void>
    {
        return this.regionRepository.remove(region_id);
    }
}