import { IsString } from "class-validator";


export class CreateRegionDTO
{
    @IsString()
    region_name: string;
}