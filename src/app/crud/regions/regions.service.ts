import { Injectable } from '@angular/core';
import {Region} from 'src/app/classes/region'
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RegionsService {

  constructor(private http:HttpClient) { }

  public getAllRegions():Observable<Region[]>{
    return this.http.get<Region[]>("http://127.0.0.1:8000/region/");
  }

  public editRegion(category:Region){
    return this.http.put("",category);
  }

  public createRegion(category:Region):Observable<Region>{
    return this.http.post<Region>("",category);
  }
  
  public deleteRegion(id:number){
    var param:HttpParams=new HttpParams();
    param.set("id",id.toString())
    return this.http.delete("", {params:param});
  }
}
