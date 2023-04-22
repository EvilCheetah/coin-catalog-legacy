import { Controller } from "@nestjs/common";
import { MessagePattern, Payload } from "@nestjs/microservices";
import { CreateRegionDTO } from "./dto/create-region.dto";
import { RegionService } from "./region.service";
import { RegionCreate } from '@/contracts';


@Controller()
export class RegionController
{
    constructor(
        private readonly regionService: RegionService
    ) {}


    @MessagePattern(RegionCreate.topic)
    create(
        @Payload()
        regionDTO: CreateRegionDTO
    )
    {
        return this.regionService.create(regionDTO);
    }


    // @MessagePattern('region.find.all')
    // find_all()
    // {
    //     return this.regionService.find_all();
    // }


    // @MessagePattern('region.find.one')
    // find_one(
    //     @Payload()
    //     region_id: number
    // )
    // {
    //     return this.regionService.find_one(region_id);
    // }

    
    // @MessagePattern('region.update')
    // update(
    //     @Payload()
    //     updateRegionDTO: UpdateRegionDTO
    // )
    // {
    //     return this.regionService.update(updateRegionDTO);
    // }


    // @MessagePattern('region.remove')
    // remove(
    //     @Payload()
    //     region_id: number
    // )
    // {
    //     return this.regionService.remove(region_id);
    // }
}