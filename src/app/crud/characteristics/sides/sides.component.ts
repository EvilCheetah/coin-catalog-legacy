import { Component, OnInit } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { Side } from 'src/app/classes/side';
import { SidesService } from './sides.service';

@Component({
  selector: 'app-sides',
  templateUrl: './sides.component.html',
  styleUrls: ['./sides.component.css']
})
export class SidesComponent implements OnInit {

  constructor(private service:SidesService) { }

  sides:Side[]=[];

  selectedSide:Side=new Side();
  nameControl= new FormControl('', [Validators.minLength(1), Validators.required]);
  createMode:boolean=false;

  ngOnInit(): void {
    this.loadSides();
  }

  loadSides(){
    this.service.getAllSides().subscribe(data=>this.sides=data);
  }

  changeCreateMode(){
    this.cancelEdit();
    this.createMode=!this.createMode;
    this.nameControl= new FormControl('', [Validators.minLength(1), Validators.required]);
  }

  selectSide(side:Side){
    this.selectedSide=side;
    this.nameControl.setValue(side.name);
  }

  deleteSide(id:number){
  this.service.deleteSide(id).subscribe(()=>this.loadSides());  
  }

  createSide(){
  let side = new Side();
  side.name = this.nameControl.value;
  this.service.createSide(side).subscribe(()=>this.loadSides())
  this.changeCreateMode();
  }

  saveEdit(){
  let side = new Side();
  side.id = this.selectedSide.id;
  side.name = this.nameControl.value;
  this.service.editSide(side).subscribe(()=>
  {
    this.loadSides();
    this.cancelEdit();
  })
  }

  cancelEdit(){
    this.nameControl=new FormControl('', [Validators.minLength(1), Validators.required]);
    this.selectedSide=new Side();
  }

}
