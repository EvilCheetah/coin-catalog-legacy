import { CreateRegionDTO } from "@/dtos";

export namespace RegionCreate
{
    export const topic    = 'region.create.command';

    export const Request  = CreateRegionDTO;

    export const Response = {}
}