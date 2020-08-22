import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import {Country} from 'src/app/classes/country';
import {Category} from 'src/app/classes/category';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CategoriesService {

  constructor(private http:HttpClient) { }

  public getAllCategories():Observable<Category>{
    return this.http.get<Category>("");
  }

  public getAllCountries():Observable<Country>{
    return this.http.get<Country>("");
  }

  public editCategory(category:Category){
    return this.http.put("",category);
  }

  public createCategory(category:Category):Observable<Category>{
    return this.http.post<Category>("",category);
  }
  
  public deleteCategory(id:number){
    var param:HttpParams=new HttpParams();
    param.set("id",id.toString())
    return this.http.delete("", {params:param});
  }
}
