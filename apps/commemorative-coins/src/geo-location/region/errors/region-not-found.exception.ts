import { NotFoundException } from "@nestjs/common";


export class RegionNotFoundException extends NotFoundException
{
    constructor(region_id: number)
    {
        super(`Region with id: '${region_id}' was NOT FOUND`)
    }
}