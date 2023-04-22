import * as dotenv from 'dotenv';
import { defineConfig } from "@mikro-orm/core";
import { Region } from "./src/geo-location/region/entities/region.entity";


dotenv.config({ path: 'apps/commemorative-coins/environment/.env' })


export default defineConfig({
    type:    'postgresql',
    host:     process.env.DB_HOST,
    port:    +process.env.DB_PORT,
    user:     process.env.DB_USERNAME,
    password: process.env.DB_PASSWORD,
    dbName:   process.env.DB_DATABASE,
    entities: [
        Region
    ],
    migrations: {
        pathTs: './apps/commemorative-coins/migrations'
    }
});