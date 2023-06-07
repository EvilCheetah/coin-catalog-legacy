import { NestFactory } from '@nestjs/core';
import { IamModule } from './app.module';


async function bootstrap()
{
    const app = await NestFactory.create(IamModule);
    await app.listen(3000);
}


bootstrap();
