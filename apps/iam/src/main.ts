import { NestFactory } from '@nestjs/core';

import { Services } from '@/constants';
import { IamModule } from './iam.module';
import { RabbitMQService } from '@/modules';


async function bootstrap()
{
    const app = await NestFactory.create(IamModule);

    const rmq_microservice = app.get<RabbitMQService>(RabbitMQService);
    app.connectMicroservice(
        rmq_microservice.get_config(Services.IamService)
    );

    await app.startAllMicroservices();
}


bootstrap();