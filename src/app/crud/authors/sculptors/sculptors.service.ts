import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import {Sculptor} from 'src/app/classes/author'

@Injectable({
  providedIn: 'root'
})
export class SculptorsService {

  constructor(private http:HttpClient) { }

  public getAllSculptors():Observable<Sculptor[]>{
    return this.http.get<Sculptor[]>("http://127.0.0.1:8000/sculptor_name/");
  }

  public editSculptor(sculptor:Sculptor){
    return this.http.put("",sculptor);
  }

  public createSculptor(sculptor:Sculptor):Observable<Sculptor>{
    return this.http.post<Sculptor>("",sculptor);
  }
  
  public deleteSculptor(id:number){
    var param:HttpParams=new HttpParams();
    param.set("id",id.toString())
    return this.http.delete("", {params:param});
  }
}
