export namespace RegionCreate
{
    export const topic    = 'region.create.command';

    export class Request
    {
        region_name: string;
    };
}