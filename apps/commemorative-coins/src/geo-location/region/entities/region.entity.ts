import { Entity, PrimaryKey, Property } from "@mikro-orm/core";


@Entity()
export class Region
{
    @PrimaryKey()
    region_id: number;

    @Property({ unique: true })
    region_name: string;
}