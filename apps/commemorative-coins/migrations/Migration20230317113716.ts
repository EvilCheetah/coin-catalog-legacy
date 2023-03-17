import { Migration } from '@mikro-orm/migrations';


export class Migration20230317113716 extends Migration
{

    async up(): Promise<void>
    {
        this.addSql(`
            CREATE TABLE "region" (
                "region_id"   SERIAL       PRIMARY KEY,
                "region_name" VARCHAR(255) NOT NULL
            );
        `);

        this.addSql(`
            ALTER TABLE "region"
            ADD CONSTRAINT "region_region_name_unique"
            UNIQUE ("region_name");
        `);
    }

    async down(): Promise<void>
    {
        this.addSql(`
            DROP TABLE IF EXISTS "region" CASCADE;
        `);
    }
}