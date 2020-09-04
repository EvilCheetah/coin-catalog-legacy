import {CoinStyle} from 'src/app/classes/coinStyle';
import {Coin} from 'src/app/classes/coin';
import {Image} from 'src/app/classes/image';
import {CoinSculptor} from 'src/app/classes/coinSculptor';
import {CoinAuthor} from 'src/app/classes/coinAuthor';
import {Note} from 'src/app/classes/note';

export class CoinInfo{
coin:Coin;
style:CoinStyle;
images:Image[];
coinAuthors:CoinAuthor[];
coinSculptors:CoinSculptor[];
note:Note;    
}



