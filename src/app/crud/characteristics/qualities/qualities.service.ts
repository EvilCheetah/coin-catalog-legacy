import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import {Quality} from 'src/app/classes/quality'

@Injectable({
  providedIn: 'root'
})
export class QualitiesService {

  constructor(private http:HttpClient) { }

  public getAllQualities():Observable<Quality[]>{
    return this.http.get<Quality[]>("");
  }

  public editQuality(quality:Quality){
    return this.http.put("",quality);
  }

  public createQuality(quality:Quality):Observable<Quality>{
    return this.http.post<Quality>("",quality);
  }
  
  public deleteQuality(id:number){
    var param:HttpParams=new HttpParams();
    param.set("id",id.toString())
    return this.http.delete("", {params:param});
  }
}
