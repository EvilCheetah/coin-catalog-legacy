import { Component, OnInit } from '@angular/core';
import {FormControl, Validators} from '@angular/forms';
import {MaterialsService} from './materials.service';
import {Material} from 'src/app/classes/material'

@Component({
  selector: 'app-materials',
  templateUrl: './materials.component.html',
  styleUrls: ['./materials.component.css']
})
export class MaterialsComponent implements OnInit {

  constructor(private service:MaterialsService) { }

  materials:Material[]=[];

  selectedMaterial:Material=new Material();
  nameControl= new FormControl('', [Validators.minLength(1), Validators.required]);
  createMode:boolean=false;

  ngOnInit(): void {
    this.loadMaterials();
  }

  loadMaterials(){
    this.service.getAllMaterials().subscribe(data=>this.materials=data);
  }

  changeCreateMode(){
    this.cancelEdit();
    this.createMode=!this.createMode;
    this.nameControl= new FormControl('', [Validators.minLength(1), Validators.required]);
  }

  selectMaterial(material:Material){
    this.selectedMaterial=material;
    this.nameControl.setValue(material.name);
  }

  deleteMaterial(id:number){
  this.service.deleteMaterial(id).subscribe(()=>this.loadMaterials());  
  }

  createMaterial(){
  let material = new Material();
  material.name = this.nameControl.value;
  this.service.createMaterial(material).subscribe(()=>this.loadMaterials())
  this.changeCreateMode();
  }

  saveEdit(){
  let material = new Material();
  material.id = this.selectedMaterial.id;
  material.name = this.nameControl.value;
  this.service.editMaterial(material).subscribe(()=>
  {
    this.loadMaterials();
    this.cancelEdit();
  })
  }

  cancelEdit(){
    this.nameControl=new FormControl('', [Validators.minLength(1), Validators.required]);
    this.selectedMaterial=new Material();
  }

}
