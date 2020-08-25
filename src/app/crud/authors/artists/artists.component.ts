import { Component, OnInit } from '@angular/core';
import {FormControl, Validators} from '@angular/forms';
import {ArtistsService} from './artists.service';
import {Author} from 'src/app/classes/author'

@Component({
  selector: 'app-artists',
  templateUrl: './artists.component.html',
  styleUrls: ['./artists.component.css']
})
export class ArtistsComponent implements OnInit {

  constructor(private service:ArtistsService) { }

  artists:Author[]=[
    {name:'hello', id:1},
    {name:'hell', id:2},
  ];

  selectedArtist:Author=new Author();
  nameControl= new FormControl('', [Validators.minLength(1), Validators.required]);
  createMode:boolean=false;

  ngOnInit(): void {
    //this.loadRegions();
  }

  loadArtists(){
    this.service.getAllArtists();
  }

  changeCreateMode(){
    this.cancelEdit();
    this.createMode=!this.createMode;
    this.nameControl= new FormControl('', [Validators.minLength(1), Validators.required]);
  }

  selectArtist(region:Author){
    this.selectedArtist=region;
    this.nameControl.setValue(region.name);
  }

  deleteArtist(id:number){
  this.service.deleteArtist(id).subscribe(()=>this.loadArtists());  
  }

  createArtist(){
  let artist = new Author();
  artist.name = this.nameControl.value;
  this.service.createArtist(artist).subscribe(()=>this.loadArtists())
  this.changeCreateMode();
  }

  saveEdit(){
  let artist = new Author();
  artist.id = this.selectedArtist.id;
  artist.name = this.nameControl.value;
  this.service.editArtist(artist).subscribe(()=>
  {
    this.loadArtists();
    this.cancelEdit();
  })
  }

  cancelEdit(){
    this.nameControl=new FormControl('', [Validators.minLength(1), Validators.required]);
    this.selectedArtist=new Author();
  }

}


