import { Component, OnInit } from '@angular/core';
import {FormControl, Validators} from '@angular/forms';
import {SculptorsService} from './sculptors.service';
import {Sculptor} from 'src/app/classes/author'

@Component({
  selector: 'app-sculptors',
  templateUrl: './sculptors.component.html',
  styleUrls: ['./sculptors.component.css']
})
export class SculptorsComponent implements OnInit {

  constructor(private service:SculptorsService) { }

  sculptors:Sculptor[]=[];

  selectedSculptor:Sculptor=new Sculptor();
  nameControl= new FormControl('', [Validators.minLength(1), Validators.required]);
  createMode:boolean=false;

  ngOnInit(): void {
    this.loadSculptors();
  }

  loadSculptors(){
    this.service.getAllSculptors().subscribe(data=>this.sculptors=data);
  }

  changeCreateMode(){
    this.cancelEdit();
    this.createMode=!this.createMode;
    this.nameControl= new FormControl('', [Validators.minLength(1), Validators.required]);
  }

  selectSculptor(sculptor:Sculptor){
    this.selectedSculptor=sculptor;
    this.nameControl.setValue(sculptor.name);
  }

  deleteSculptor(id:number){
  this.service.deleteSculptor(id).subscribe(()=>this.loadSculptors());  
  }

  createSculptor(){
  let sculptor = new Sculptor();
  sculptor.name = this.nameControl.value;
  this.service.createSculptor(sculptor).subscribe(()=>this.loadSculptors())
  this.changeCreateMode();
  }

  saveEdit(){
  let sculptor = new Sculptor();
  sculptor.id = this.selectedSculptor.id;
  sculptor.name = this.nameControl.value;
  this.service.editSculptor(sculptor).subscribe(()=>
  {
    this.loadSculptors();
    this.cancelEdit();
  })
  }

  cancelEdit(){
    this.nameControl=new FormControl('', [Validators.minLength(1), Validators.required]);
    this.selectedSculptor=new Sculptor();
  }

}
