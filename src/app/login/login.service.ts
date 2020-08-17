import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import {User} from '../classes/user'

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(private http:HttpClient) { }

  checkUser(login:string, password:string):Observable<User>{
    
    var param:HttpParams=new HttpParams();
    param.set("login",login);
    param.set("password",password);
    return this.http.get<User>("", { params:param});
  }
  
  getUserById(id:number):Observable<User>{
    var param:HttpParams=new HttpParams();
    param.set("id",id.toString())
    return this.http.get<User>("",{params:param});

  }
}
