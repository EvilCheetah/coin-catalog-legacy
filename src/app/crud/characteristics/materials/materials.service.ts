import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import {Material} from 'src/app/classes/material'

@Injectable({
  providedIn: 'root'
})
export class MaterialsService {

  constructor(private http:HttpClient) { }

  public getAllMaterials():Observable<Material[]>{
    return this.http.get<Material[]>("http://127.0.0.1:8000/material/");
  }

  public editMaterial(material:Material){
    return this.http.put("",material);
  }

  public createMaterial(material:Material):Observable<Material>{
    return this.http.post<Material>("",material);
  }
  
  public deleteMaterial(id:number){
    var param:HttpParams=new HttpParams();
    param.set("id",id.toString())
    return this.http.delete("", {params:param});
  }
}
