import { MikroOrmModuleAsyncOptions } from "@mikro-orm/nestjs";
import { ConfigModule, ConfigService } from "@nestjs/config";



export function get_db_config(): MikroOrmModuleAsyncOptions
{
    return {
        useFactory: (config: ConfigService) =>
        ({
            type:     'postgresql',
            host:     config.get<string>('DB_HOST'),
            port:     config.get<number>('DB_PORT'),
            user:     config.get<string>('DB_USERNAME'),
            password: config.get<string>('DB_PASSWORD'),
            dbName:   config.get<string>('DB_DATABASE'),
            entities: []
        }),
        imports: [ConfigModule],
        inject:  [ConfigService]
    }
}