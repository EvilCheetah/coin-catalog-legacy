import { CreateRegionDTO } from "@/dtos";
import { IRegion } from "@/interfaces";


export namespace RegionCreate
{
    export const topic   = 'region.create.command';

    export type Request  = CreateRegionDTO;

    export type Response = IRegion;
}