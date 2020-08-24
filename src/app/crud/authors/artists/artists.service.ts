import {Injectable} from '@angular/core'
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import {Artist} from 'src/app/classes/author'


@Injectable({
  providedIn: 'root'
})
export class ArtistsService {

  constructor(private http:HttpClient) { }

  public getAllArtists():Observable<Artist[]>{
    return this.http.get<Artist[]>("");
  }

  public editArtist(artist:Artist){
    return this.http.put("",artist);
  }

  public createArtist(artist:Artist):Observable<Artist>{
    return this.http.post<Artist>("",artist);
  }
  
  public deleteArtist(id:number){
    var param:HttpParams=new HttpParams();
    param.set("id",id.toString())
    return this.http.delete("", {params:param});
  }
}