import { Injectable } from "@nestjs/common";
import { CreateRegionDTO } from "./dto/create-region.dto";
import { UpdateRegionDTO } from "./dto/update-region.dto";


@Injectable()
export class RegionService
{
    constructor() {}

    create(regionDTO: CreateRegionDTO)
    {
        
    }

    find_one(region_id: number)
    {

    }

    find_all()
    {

    }

    update({ region_id, ...data }: UpdateRegionDTO)
    {

    }

    remove(region_id: number)
    {
        
    }
}