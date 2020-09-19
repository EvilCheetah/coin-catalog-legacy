import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import {Shape} from 'src/app/classes/shape'

@Injectable({
  providedIn: 'root'
})
export class ShapesService {

  constructor(private http:HttpClient) { }

  public getAllShapes():Observable<Shape[]>{
    return this.http.get<Shape[]>("http://127.0.0.1:8000/shape/");
  }

  public editShape(shape:Shape){
    return this.http.put("",shape);
  }

  public createShape(shape:Shape):Observable<Shape>{
    return this.http.post<Shape>("",shape);
  }
  
  public deleteShape(id:number){
    var param:HttpParams=new HttpParams();
    param.set("id",id.toString())
    return this.http.delete("", {params:param});
  }
}
