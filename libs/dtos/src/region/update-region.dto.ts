import { PartialType } from "@nestjs/mapped-types";
import { CreateRegionDTO } from "./create-region.dto";


export class UpdateRegionDTO extends PartialType(CreateRegionDTO)
{
    region_id: number;
}