import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import {Region} from 'src/app/classes/region'
import {Country} from 'src/app/classes/country';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CountriesService {

  constructor(private http:HttpClient) { }

  public getAllRegions():Observable<Region[]>{
    return this.http.get<Region[]>("");
  }
  public getAllCountries():Observable<Country[]>{
    return this.http.get<Country[]>("");
  }

  public editCountry(country:Country){
    return this.http.put("",country);
  }

  public createCountry(country:Country){
    return this.http.post("",country);
  }
  
  public deleteCountry(id:number){
    var param:HttpParams=new HttpParams();
    param.set("id",id.toString())
    return this.http.delete("", {params:param});
  }
}

