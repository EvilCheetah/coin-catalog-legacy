import { Component, OnInit } from '@angular/core';
import {FormControl, Validators} from '@angular/forms';
import {MintedByService} from './minted-by.service';
import {MintedBy} from 'src/app/classes/mintedBy'

@Component({
  selector: 'app-minted-by',
  templateUrl: './minted-by.component.html',
  styleUrls: ['./minted-by.component.css']
})
export class MintedByComponent implements OnInit {

  constructor(private service:MintedByService) { }

  mintedBy:MintedBy[]=[
    {name:'hello', id:1},
    {name:'hell', id:2},
  ];

  selectedMintedBy:MintedBy=new MintedBy();
  nameControl= new FormControl('', [Validators.minLength(1), Validators.required]);
  createMode:boolean=false;

  ngOnInit(): void {
    //this.loadRegions();
  }

  loadMintedBy(){
    this.service.getAllMintedBy();
  }

  changeCreateMode(){
    this.cancelEdit();
    this.createMode=!this.createMode;
    this.nameControl= new FormControl('', [Validators.minLength(1), Validators.required]);
  }

  selectMintedBy(mintedBy:MintedBy){
    this.selectedMintedBy=mintedBy;
    this.nameControl.setValue(mintedBy.name);
  }

  deleteMintedBy(id:number){
  this.service.deleteMintedBy(id).subscribe(()=>this.loadMintedBy());  
  }

  createMintedBy(){
  let mintedBy = new MintedBy();
  mintedBy.name = this.nameControl.value;
  this.service.createMintedBy(mintedBy).subscribe(()=>this.loadMintedBy())
  this.changeCreateMode();
  }

  saveEdit(){
  let mintedBy = new MintedBy();
  mintedBy.id = this.selectedMintedBy.id;
  mintedBy.name = this.nameControl.value;
  this.service.editMintedBy(mintedBy).subscribe(()=>
  {
    this.loadMintedBy();
    this.cancelEdit();
  })
  }

  cancelEdit(){
    this.nameControl=new FormControl('', [Validators.minLength(1), Validators.required]);
    this.selectedMintedBy=new MintedBy();
  }

}
