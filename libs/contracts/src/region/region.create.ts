import { CreateRegionDTO } from "@/dtos";
import { Region } from "apps/commemorative-coins/src/geo-location/region/entities/region.entity";


export namespace RegionCreate
{
    export const topic    = 'region.create.command';

    export class Request extends CreateRegionDTO {};

    export class Response extends Region {};
}