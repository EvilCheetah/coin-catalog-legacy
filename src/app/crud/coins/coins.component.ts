import { Component, OnInit } from '@angular/core';
import {FormControl, FormGroup, Validators} from '@angular/forms';
import {CoinsService} from './coins.service';
import {Coin} from 'src/app/classes/coin';
import {MintedBy} from 'src/app/classes/mintedBy';
import {Author} from 'src/app/classes/author';
import {Sculptor} from 'src/app/classes/author';
import {Shape} from 'src/app/classes/shape';
import {CoinStyle} from 'src/app/classes/coinStyle';
import { Quality } from 'src/app/classes/quality';
import { Edge } from 'src/app/classes/edge';
import { Material } from 'src/app/classes/material';
import {SubStyle} from 'src/app/classes/substyle';
import {Note} from 'src/app/classes/note';
import {Image} from 'src/app/classes/image';
import {Collection} from 'src/app/classes/collection';
import {CoinInfo} from 'src/app/classes/createCoin';



@Component({
  selector: 'app-coins',
  templateUrl: './coins.component.html',
  styleUrls: ['./coins.component.css']
})
export class CoinsComponent implements OnInit {

  coins:Coin[]=[{id:1, collection:1, name:"Coin1", mintedBy:1, author:1, sculptor:1},
  {id:2, collection:2, name:"Coin1", mintedBy:1, author:1, sculptor:1}];

  collections:Collection[]=[{id:1, name:"Collection1", category:1},
  {id:2, name:"Collection2", category:2}];
  authors:Author[]=[{id:1, name:"Author1"}];
  sculptors:Sculptor[]=[{id:1, name:"Sculptor1"}];
  mintedBy:MintedBy[]=[{id:1, name:"Belarus"}];
  

  coinsStyles:CoinStyle[]=[{id:1, year:1999, coin:1, shape:1,
     quality:1, edge:1, material:1, standart:"Standart", denomination:"Denomination",
      mintage:1, additional_name:"NaN", km_number:"Number", is_rare:true, is_substyle:false,
    weight:10, length:30, width:40}]
  
  shapes: Shape[]=[{id:1, name:"Shape1"}];
  qualities : Quality[]=[{id:1, name:"Quality1"}];
  edges : Edge[]=[{id:1, name:"Edge1"}];
  materials : Material[]=[{id:1, name:"Material1"}];

  subStyles:SubStyle[]=[{id:1, parent_coin:1, substyle_coin:2 }];
  note = new Note;
  images:Image[]=[{id:1, side:"frontal", coin_style:1, path:"https://dh.img.tyt.by/n/zamirovskiy/06/b/04_pushkinskaya_20200815_zam_tutby_phsl.jpg"},
  {id:2, side:"back", coin_style:1, path:"https://dh.img.tyt.by/n/buryakina/08/c/photo_2020-08-15_16-32-09.jpg"}];

  selectedCoin=new Coin();
  createMode:Boolean=false;
  coinGroup:FormGroup= new FormGroup(
    {
      collectionControl:new FormControl("", [Validators.minLength(1), Validators.required]),
      nameControl:new FormControl("", [Validators.minLength(1), Validators.required]),
      mintedByControl:new FormControl("", [Validators.minLength(1), Validators.required]),
      authorControl:new FormControl("", [Validators.minLength(1), Validators.required]),
      sculptorControl:new FormControl("", [Validators.minLength(1), Validators.required]),
      yearControl:new FormControl("", [Validators.minLength(1), Validators.required]),
      shapeControl:new FormControl("", [Validators.minLength(1), Validators.required]),
      qualityControl:new FormControl("", [Validators.minLength(1), Validators.required]),
      edgeControl:new FormControl("", [Validators.minLength(1), Validators.required]),
      materialControl:new FormControl("", [Validators.minLength(1), Validators.required]),
      standartControl:new FormControl("", [Validators.minLength(1), Validators.required]),
      denominationControl:new FormControl("", [Validators.minLength(1), Validators.required]),
      mintageControl:new FormControl("", [Validators.minLength(1), Validators.required]),
      additionalNameControl:new FormControl(""),
      kmNumberControl:new FormControl(""),
      rareControl:new FormControl(""),
      substyleControl:new FormControl(""),
      weightControl:new FormControl("", [ Validators.required]),
      lengthControl:new FormControl("", [ Validators.required]),
      widthControl:new FormControl("", [ Validators.required]),
      noteControl:new FormControl("")
    }
  );
  frontPath:any="assets/images/add.png";
  backPath:any="assets/images/add.png";
  edgePath:any="assets/images/add.png";

  frontFile:File=null;
  backFile:File=null;
  edgeFile:File=null;

  coinInfo:CoinInfo[]=[];
  

  constructor(private service:CoinsService) { }

  ngOnInit(): void {
    this.note.id=1;
    this.note.description="This is fucking description";
    
    
  }

  clearPaths(){
    this.frontPath="assets/images/add.png";
    this.backPath="assets/images/add.png";
    this.edgePath="assets/images/add.png";
    this.frontFile = null;
    this.backFile = null;
    this.edgeFile = null;
  }

  previewFront(event){
    this.frontFile=<File>event.target.files[0];
    var reader = new FileReader();
    reader.readAsDataURL(this.frontFile);
    reader.onload=((fl)=>{
      this.frontPath=reader.result;
    })
  }

  previewBack(event){
    this.backFile=<File>event.target.files[0];
    var reader = new FileReader();
    reader.readAsDataURL(this.backFile);
    reader.onload=((fl)=>{
      this.backPath=reader.result;
    })
  }

  previewEdge(event){
    this.edgeFile=<File>event.target.files[0];
    var reader = new FileReader();
    reader.readAsDataURL(this.edgeFile);
    reader.onload=((fl)=>{
      this.edgePath=reader.result;
    })
  }

  addNewStyle(){
    let coinInf = new CoinInfo();
    let coin = new Coin();
    let coinStyl = new CoinStyle();
    let imgs:Image[]=[
      {side:"Front", file:this.frontFile},
      {side:"Back", file:this.backFile},
      {side:"Edge", file:this.edgeFile}
    ];
    coin.author = this.coinGroup.controls["authorControl"].value;
    coin.collection = this.coinGroup.controls["collectionControl"].value;
    coin.mintedBy = this.coinGroup.controls["mintedByControl"].value;
    coin.name = this.coinGroup.controls["nameControl"].value;
    coin.sculptor = this.coinGroup.controls["sculptorControl"].value;
    coinStyl.is_rare = this.coinGroup.controls["rareControl"].value;
    if (this.coinInfo.length!=0) coinStyl.is_substyle=true;
    else coinStyl.is_substyle=false;
    coinStyl.km_number = this.coinGroup.controls["kmNumberControl"].value;
    coinStyl.length = this.coinGroup.controls["lengthControl"].value;
    coinStyl.material = this.coinGroup.controls["materialControl"].value;
    coinStyl.mintage = this.coinGroup.controls["mintageControl"].value;
    coinStyl.quality = this.coinGroup.controls["qualityControl"].value;
    coinStyl.shape = this.coinGroup.controls["shapeControl"].value;
    coinStyl.standart = this.coinGroup.controls["standartControl"].value;
    coinStyl.weight = this.coinGroup.controls["weightControl"].value;
    coinStyl.width = this.coinGroup.controls["widthControl"].value;
    coinStyl.year = this.coinGroup.controls["yearControl"].value;
    this.coinGroup.reset();
    this.clearPaths();
    coinInf.coin = coin;
    coinInf.style = coinStyl;
    coinInf.images = imgs;
    
    this.coinInfo.push(coinInf);
    console.log(this.coinInfo.length);
  }

  getCollectionName(id:number):string{
    return this.collections.find(collection=>collection.id==id).name;
  }

  getMintedByName(id:number){
    return this.mintedBy.find(minBy=>minBy.id==id).name;  
  }

  getAuthorName(id:number):string{
    return this.authors.find(author=>author.id==id).name;
  }
  getSculptorName(id:number):string{
    return this.sculptors.find(sculptor=>sculptor.id==id).name;
  }

  showCoinById(id:number){

  }

  changeCreateMode(){
    this.createMode=!this.createMode;
    this.coinGroup.reset();
    
  }

  selectCoin(coin:Coin){

  }

  deleteCoin(id:number){

  }

}
