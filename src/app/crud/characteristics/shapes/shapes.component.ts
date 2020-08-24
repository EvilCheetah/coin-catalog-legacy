import { Component, OnInit } from '@angular/core';
import {FormControl, Validators} from '@angular/forms';
import {ShapesService} from './shapes.service';
import {Shape} from 'src/app/classes/shape'


@Component({
  selector: 'app-shapes',
  templateUrl: './shapes.component.html',
  styleUrls: ['./shapes.component.css']
})
export class ShapesComponent implements OnInit {

  constructor(private service:ShapesService) { }

  shapes:Shape[]=[
    {name:'hello', id:1},
    {name:'hell', id:2},
  ];

  selectedShape:Shape=new Shape();
  nameControl= new FormControl('', [Validators.minLength(1), Validators.required]);
  createMode:boolean=false;

  ngOnInit(): void {
    //this.loadRegions();
  }

  loadShapes(){
    this.service.getAllShapes();
  }

  changeCreateMode(){
    this.cancelEdit();
    this.createMode=!this.createMode;
    this.nameControl= new FormControl('', [Validators.minLength(1), Validators.required]);
  }

  selectShape(shape:Shape){
    this.selectedShape=shape;
    this.nameControl.setValue(shape.name);
  }

  deleteShape(id:number){
  this.service.deleteShape(id).subscribe(()=>this.loadShapes());  
  }

  createShape(){
  let shape = new Shape();
  shape.name = this.nameControl.value;
  this.service.createShape(shape).subscribe(()=>this.loadShapes())
  this.changeCreateMode();
  }

  saveEdit(){
  let shape = new Shape();
  shape.id = this.selectedShape.id;
  shape.name = this.nameControl.value;
  this.service.editShape(shape).subscribe(()=>
  {
    this.loadShapes();
    this.cancelEdit();
  })
  }

  cancelEdit(){
    this.nameControl=new FormControl('', [Validators.minLength(1), Validators.required]);
    this.selectedShape=new Shape();
  }

}
