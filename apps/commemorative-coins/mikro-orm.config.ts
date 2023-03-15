import { defineConfig } from "@mikro-orm/core";
import { ConfigService } from "@nestjs/config";

import { Region } from "./src/geo-location/region/entities/region.entity";


const config = new ConfigService();


export default defineConfig({
    type:    'postgresql',
    host:     config.get<string>('DB_HOST'),
    port:     config.get<number>('DB_PORT'),
    user:     config.get<string>('DB_USERNAME'),
    password: config.get<string>('DB_PASSWORD'),
    dbName:   config.get<string>('DB_DATABASE'),
    entities: [
        Region
    ]
});