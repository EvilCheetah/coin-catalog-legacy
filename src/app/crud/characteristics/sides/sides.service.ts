import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Side } from 'src/app/classes/side';

@Injectable({
  providedIn: 'root'
})
export class SidesService {

  constructor(private http:HttpClient) { }

  public getAllSides():Observable<Side[]>{
    return this.http.get<Side[]>("http://127.0.0.1:8000/material/");
  }

  public editSide(side:Side){
    return this.http.put("",Side);
  }

  public createSide(side:Side):Observable<Side>{
    return this.http.post<Side>("",side);
  }
  
  public deleteSide(id:number){
    var param:HttpParams=new HttpParams();
    param.set("id",id.toString())
    return this.http.delete("", {params:param});
  }
}
