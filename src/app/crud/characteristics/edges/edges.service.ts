import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import {Edge} from 'src/app/classes/edge'

@Injectable({
  providedIn: 'root'
})
export class EdgesService {

  constructor(private http:HttpClient) { }

  public getAllEdges():Observable<Edge[]>{
    return this.http.get<Edge[]>("");
  }

  public editEdge(edge:Edge){
    return this.http.put("",edge);
  }

  public createEdge(edge:Edge):Observable<Edge>{
    return this.http.post<Edge>("",edge);
  }
  
  public deleteEdge(id:number){
    var param:HttpParams=new HttpParams();
    param.set("id",id.toString())
    return this.http.delete("", {params:param});
  }
}
