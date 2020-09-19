import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import {MintedBy} from 'src/app/classes/mintedBy'

@Injectable({
  providedIn: 'root'
})
export class MintedByService {

  constructor(private http:HttpClient) { }

  public getAllMintedBy():Observable<MintedBy[]>{
    return this.http.get<MintedBy[]>("http://127.0.0.1:8000/minted_by/");
  }

  public editMintedBy(mintedBy:MintedBy){
    return this.http.put("",mintedBy);
  }

  public createMintedBy(mintedBy:MintedBy):Observable<MintedBy>{
    return this.http.post<MintedBy>("",mintedBy);
  }
  
  public deleteMintedBy(id:number){
    var param:HttpParams=new HttpParams();
    param.set("id",id.toString())
    return this.http.delete("", {params:param});
  }
}
