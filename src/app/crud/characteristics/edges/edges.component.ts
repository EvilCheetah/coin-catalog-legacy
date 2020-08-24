import { Component, OnInit } from '@angular/core';
import {FormControl, Validators} from '@angular/forms';
import {EdgesService} from './edges.service';
import {Edge} from 'src/app/classes/edge'


@Component({
  selector: 'app-edges',
  templateUrl: './edges.component.html',
  styleUrls: ['./edges.component.css']
})
export class EdgesComponent implements OnInit {

  constructor(private service:EdgesService) { }

  edges:Edge[]=[
    {name:'hello', id:1},
    {name:'hell', id:2},
  ];

  selectedEdge:Edge=new Edge();
  nameControl= new FormControl('', [Validators.minLength(1), Validators.required]);
  createMode:boolean=false;

  ngOnInit(): void {
    //this.loadRegions();
  }

  loadEdges(){
    this.service.getAllEdges();
  }

  changeCreateMode(){
    this.cancelEdit();
    this.createMode=!this.createMode;
    this.nameControl= new FormControl('', [Validators.minLength(1), Validators.required]);
  }

  selectEdge(edge:Edge){
    this.selectedEdge=edge;
    this.nameControl.setValue(edge.name);
  }

  deleteEdge(id:number){
  this.service.deleteEdge(id).subscribe(()=>this.loadEdges());  
  }

  createEdge(){
  let edge = new Edge();
  edge.name = this.nameControl.value;
  this.service.createEdge(edge).subscribe(()=>this.loadEdges())
  this.changeCreateMode();
  }

  saveEdit(){
  let edge = new Edge();
  edge.id = this.selectedEdge.id;
  edge.name = this.nameControl.value;
  this.service.editEdge(edge).subscribe(()=>
  {
    this.loadEdges();
    this.cancelEdit();
  })
  }

  cancelEdit(){
    this.nameControl=new FormControl('', [Validators.minLength(1), Validators.required]);
    this.selectedEdge=new Edge();
  }

}
