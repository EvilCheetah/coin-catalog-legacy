import { ServiceName } from '@/constants';
import { RabbitMQService } from '@/modules';
import { NestFactory } from '@nestjs/core';
import { CommemorativeCoinsModule } from './commemorative-coins.module';


async function bootstrap()
{
    const app = await NestFactory.create(CommemorativeCoinsModule);

    const rmq_microservice = app.get<RabbitMQService>(RabbitMQService);
    app.connectMicroservice(
        rmq_microservice.get_config(ServiceName.CommemorativeCoinsService)
    );

    await app.startAllMicroservices();
}


bootstrap();