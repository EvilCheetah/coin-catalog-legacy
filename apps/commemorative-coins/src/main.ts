import { NestFactory } from '@nestjs/core';
import { CommemorativeCoinsModule } from './commemorative-coins.module';


async function bootstrap()
{
    const app = await NestFactory.create(CommemorativeCoinsModule);
    await app.listen(3000);
}


bootstrap();
