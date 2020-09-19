import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import {Collection} from 'src/app/classes/collection'
import {Category} from 'src/app/classes/category';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CollectionsService {

  constructor(private http:HttpClient) { }

  public getAllCategories():Observable<Category[]>{
    return this.http.get<Category[]>("http://127.0.0.1:8000/category/");
  }
  public getAllCollections():Observable<Collection[]>{
    return this.http.get<Collection[]>("http://127.0.0.1:8000/collection/");
  }

  public editCollection(collection:Collection){
    return this.http.put("",collection);
  }

  public createCollection(collection:Collection){
    return this.http.post("",collection);
  }
  
  public deleteCollection(id:number){
    var param:HttpParams=new HttpParams();
    param.set("id",id.toString())
    return this.http.delete("", {params:param});
  }
}
