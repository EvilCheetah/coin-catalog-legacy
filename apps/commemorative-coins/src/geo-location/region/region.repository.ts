import { Injectable } from "@nestjs/common";
import { EntityRepository, wrap } from "@mikro-orm/core";
import { InjectRepository } from "@mikro-orm/nestjs";

import { Region } from "./entities/region.entity";
import { CreateRegionDTO } from "./dto/create-region.dto";
import { RegionNotFoundException } from "./errors/region-not-found.exception";
import { UpdateRegionDTO } from "./dto/update-region.dto";


@Injectable()
export class RegionRepository
{
    constructor(
        @InjectRepository(Region)
        private readonly regionRepository: EntityRepository<Region>
    ) {}


    async create(createRegionDTO: CreateRegionDTO): Promise<Region>
    {
        const region = this.regionRepository.create(createRegionDTO);

        await this.regionRepository.persistAndFlush(region);

        return region;
    }

    find_all(): Promise<Region[]>
    {
        return this.regionRepository.findAll();
    }

    async find_one(region_id: number): Promise<Region>
    {
        const region = await this.regionRepository.findOne({ region_id });

        if ( !region )
            throw new RegionNotFoundException(region_id);
        
        return region;
    }

    async update({region_id, ...data}: UpdateRegionDTO): Promise<Region>
    {
        const region = await this.find_one(region_id);

        wrap(region).assign(data);
        await this.regionRepository.persistAndFlush(region);

        return region;
    }

    async remove(region_id: number): Promise<void>
    {
        const region = await this.find_one(region_id);

        await this.regionRepository.removeAndFlush(region);
    }
}