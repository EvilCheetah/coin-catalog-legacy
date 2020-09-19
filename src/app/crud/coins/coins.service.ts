import { Injectable } from '@angular/core';
import {Coin} from 'src/app/classes/coin';
import {MintedBy} from 'src/app/classes/mintedBy';
import {Author} from 'src/app/classes/author';
import {Sculptor} from 'src/app/classes/author';
import {Shape} from 'src/app/classes/shape';
import {CoinStyle} from 'src/app/classes/coinStyle';
import { Quality } from 'src/app/classes/quality';
import { Edge } from 'src/app/classes/edge';
import { Material } from 'src/app/classes/material';
import {SubStyle} from 'src/app/classes/substyle';
import {Note} from 'src/app/classes/note';
import {Image} from 'src/app/classes/image';
import {Collection} from 'src/app/classes/collection';
import {CoinInfo} from 'src/app/classes/createCoin';
import {CoinSculptor} from 'src/app/classes/coinSculptor';
import {CoinAuthor} from 'src/app/classes/coinAuthor';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CoinsService {

  constructor(private http:HttpClient) { }

  getAllCoins():Observable<Coin[]>{
    return this.http.get<Coin[]>("http://127.0.0.1:8000/coin_family/");
  }

  getAllCollections():Observable<Collection[]>{
    return this.http.get<Collection[]>("http://127.0.0.1:8000/collection/");
  }

  getAllAuthors():Observable<Author[]>{
    return this.http.get<Author[]>("http://127.0.0.1:8000/author_name/");
  }

  getAllSculptors():Observable<Sculptor[]>{
    return this.http.get<Sculptor[]>("http://127.0.0.1:8000/sculptor_name/");
  }

  getAllMintedBy():Observable<MintedBy[]>{
    return this.http.get<MintedBy[]>("http://127.0.0.1:8000/minted_by/");
  }

 

  getAllShapes():Observable<Shape[]>{
    return this.http.get<Shape[]>("http://127.0.0.1:8000/shapes/");
  }

  getAllQualities():Observable<Quality[]>{
    return this.http.get<Quality[]>("http://127.0.0.1:8000/quality/");
  }

  getAllEdges():Observable<Edge[]>{
    return this.http.get<Edge[]>("http://127.0.0.1:8000/edge/");
  }

  getAllMaterials():Observable<Material[]>{
    return this.http.get<Material[]>("http://127.0.0.1:8000/material/");
  }

  getSubstylesById(id:number):Observable<SubStyle[]>{
    var param:HttpParams=new HttpParams();
    param.set("id",id.toString())
    return this.http.get<SubStyle[]>("",{params:param});
  }

  getNoteByStyleId(id:number):Observable<Note>{
    var param:HttpParams=new HttpParams();
    param.set("id",id.toString())
    return this.http.get<Note>("",{params:param});
  }

  getImagesById(id:number):Observable<Image[]>{
    var param:HttpParams=new HttpParams();
    param.set("id",id.toString())
    return this.http.get<Image[]>("",{params:param});
  }

  getCoinAuthorsById(id:number):Observable<CoinAuthor[]>{
    var param:HttpParams=new HttpParams();
    param.set("id",id.toString())
    return this.http.get<CoinAuthor[]>("",{params:param}); 
  }

  getCoinSculptorsById(id:number):Observable<CoinSculptor[]>{
    var param:HttpParams=new HttpParams();
    param.set("id",id.toString())
    return this.http.get<CoinSculptor[]>("",{params:param}); 
  }

  getCoinsStyleById(id:number):Observable<CoinStyle>{
    var param:HttpParams=new HttpParams();
    param.set("id",id.toString())
    return this.http.get<CoinStyle>("",{params:param});
  }

  createCoin(coinInfo:CoinInfo[]){
    return this.http.post("",coinInfo);
  }

  updateCoin(coinInfo:CoinInfo[]){
    return this.http.put("",coinInfo);
  }

  deleteCoin(id:number){
    var param:HttpParams=new HttpParams();
    param.set("id",id.toString())
    return this.http.delete("",{params:param});
  }

}
