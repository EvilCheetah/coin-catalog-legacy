import { Component, OnInit } from '@angular/core';
import {FormControl, Validators} from '@angular/forms';
import {RegionsService} from './regions.service';
import {Region} from 'src/app/classes/region'

@Component({
  selector: 'app-regions',
  templateUrl: './regions.component.html',
  styleUrls: ['./regions.component.css']
})
export class RegionsComponent implements OnInit {

  constructor(private service:RegionsService) { }

  regions:Region[]=[
    
  ];

  selectedRegion:Region=new Region();
  nameControl= new FormControl('', [Validators.minLength(1), Validators.required]);
  createMode:boolean=false;

  ngOnInit(): void {
    this.loadRegions();
  }

  loadRegions(){
    this.service.getAllRegions().subscribe(data=>this.regions=data);
  }

  changeCreateMode(){
    this.cancelEdit();
    this.createMode=!this.createMode;
    this.nameControl= new FormControl('', [Validators.minLength(1), Validators.required]);
  }

  selectRegion(region:Region){
    this.selectedRegion=region;
    this.nameControl.setValue(region.name);
  }

  deleteRegion(id:number){
  this.service.deleteRegion(id).subscribe(()=>this.loadRegions());  
  }

  createRegion(){
  let region = new Region();
  region.name = this.nameControl.value;
  this.service.createRegion(region).subscribe(()=>this.loadRegions())
  this.changeCreateMode();
  }

  saveEdit(){
  let region = new Region();
  region.id = this.selectedRegion.id;
  region.name = this.nameControl.value;
  this.service.editRegion(region).subscribe(()=>
  {
    this.loadRegions();
    this.cancelEdit();
  })
  }

  cancelEdit(){
    this.nameControl=new FormControl('', [Validators.minLength(1), Validators.required]);
    this.selectedRegion=new Region();
  }

}
