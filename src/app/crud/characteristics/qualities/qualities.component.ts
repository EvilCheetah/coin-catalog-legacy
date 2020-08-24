import { Component, OnInit } from '@angular/core';
import {FormControl, Validators} from '@angular/forms';
import {QualitiesService} from './qualities.service';
import {Quality} from 'src/app/classes/quality'

@Component({
  selector: 'app-qualities',
  templateUrl: './qualities.component.html',
  styleUrls: ['./qualities.component.css']
})
export class QualitiesComponent implements OnInit {

  constructor(private service:QualitiesService) { }

  qualities:Quality[]=[
    {name:'hello', id:1},
    {name:'hell', id:2},
  ];

  selectedQuality:Quality=new Quality();
  nameControl= new FormControl('', [Validators.minLength(1), Validators.required]);
  createMode:boolean=false;

  ngOnInit(): void {
    //this.loadRegions();
  }

  loadQualities(){
    this.service.getAllQualities();
  }

  changeCreateMode(){
    this.cancelEdit();
    this.createMode=!this.createMode;
    this.nameControl= new FormControl('', [Validators.minLength(1), Validators.required]);
  }

  selectQuality(quality:Quality){
    this.selectedQuality=quality;
    this.nameControl.setValue(quality.name);
  }

  deleteQuality(id:number){
  this.service.deleteQuality(id).subscribe(()=>this.loadQualities());  
  }

  createQuality(){
  let quality = new Quality();
  quality.name = this.nameControl.value;
  this.service.createQuality(quality).subscribe(()=>this.loadQualities())
  this.changeCreateMode();
  }

  saveEdit(){
  let quality = new Quality();
  quality.id = this.selectedQuality.id;
  quality.name = this.nameControl.value;
  this.service.editQuality(quality).subscribe(()=>
  {
    this.loadQualities();
    this.cancelEdit();
  })
  }

  cancelEdit(){
    this.nameControl=new FormControl('', [Validators.minLength(1), Validators.required]);
    this.selectedQuality=new Quality();
  }

}
