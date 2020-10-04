export class Image{
    id?:number;
    side:number;
    coin_style?:number;
    path?:string;
    file?:File;

    constructor(side:number, file:File){
        this.side=side;
        this.file=file;
    }
}