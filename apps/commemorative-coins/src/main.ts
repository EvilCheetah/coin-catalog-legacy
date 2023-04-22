import { NestFactory } from '@nestjs/core';
import { ValidationPipe } from '@nestjs/common';

import { Services } from '@/constants';
import { RabbitMQService } from '@/modules';
import { CommemorativeCoinsModule } from './commemorative-coins.module';


async function bootstrap()
{
    const app = await NestFactory.create(CommemorativeCoinsModule);

    const rmq_microservice = app.get<RabbitMQService>(RabbitMQService);
    app.connectMicroservice(
        rmq_microservice.get_config(Services.CommemorativeCoinsService)
    );

    await app.startAllMicroservices();
}


bootstrap();