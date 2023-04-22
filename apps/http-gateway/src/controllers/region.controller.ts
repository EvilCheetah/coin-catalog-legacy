import { Body, Controller, Delete, Get, Inject, Logger, Patch, Post } from "@nestjs/common";
import { ClientProxy } from "@nestjs/microservices";
import { lastValueFrom } from 'rxjs';

import { Services } from '@/constants';
import { RegionCreate } from '@/contracts';


@Controller('regions')
export class RegionController
{
    private readonly logger = new Logger(RegionController.name)
    
    constructor(
        @Inject(Services.CommemorativeCoinsService)
        private readonly rabbitMQ: ClientProxy,
    ) {}

    @Post()
    create(
        @Body()
        data: RegionCreate.Request
    )
    {
        return this.rabbitMQ.send<RegionCreate.Response>(
            RegionCreate.topic, data
        );
    }

    @Get()
    find_all()
    {

    }

    @Get()
    find_one()
    {

    }

    @Patch()
    update()
    {

    }

    @Delete()
    remove()
    {
        
    }
}