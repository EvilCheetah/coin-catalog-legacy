import { NestFactory } from '@nestjs/core';
import { HttpGatewayModule } from './http-gateway.module';


async function bootstrap()
{
    const app = await NestFactory.create(HttpGatewayModule);
    
    await app.listen(3000);
}


bootstrap();
