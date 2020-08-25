import {Injectable} from '@angular/core'
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import {Author} from 'src/app/classes/author'


@Injectable({
  providedIn: 'root'
})
export class ArtistsService {

  constructor(private http:HttpClient) { }

  public getAllArtists():Observable<Author[]>{
    return this.http.get<Author[]>("");
  }

  public editArtist(artist:Author){
    return this.http.put("",artist);
  }

  public createArtist(artist:Author):Observable<Author>{
    return this.http.post<Author>("",artist);
  }
  
  public deleteArtist(id:number){
    var param:HttpParams=new HttpParams();
    param.set("id",id.toString())
    return this.http.delete("", {params:param});
  }
}