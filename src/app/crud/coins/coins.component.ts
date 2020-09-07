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
import {CoinSculptor} from 'src/app/classes/coinSculptor';
import {CoinAuthor} from 'src/app/classes/coinAuthor';
import { typeWithParameters } from '@angular/compiler/src/render3/util';





@Component({
  selector: 'app-coins',
  templateUrl: './coins.component.html',
  styleUrls: ['./coins.component.css']
})
export class CoinsComponent implements OnInit {

  coins:Coin[]=[{id:1, collection:1, name:"Coin1", mintedBy:1},
  {id:2, collection:2, name:"Coin21", mintedBy:1}];

  collections:Collection[]=[{id:1, name:"Collection1", category:1},
  {id:2, name:"Collection2", category:2}];
  authors:Author[]=[{id:1, name:"Author1"}];
  sculptors:Sculptor[]=[{id:1, name:"Sculptor1"}];
  mintedBy:MintedBy[]=[{id:1, name:"Belarus"}];
  

  coinsStyles:CoinStyle[]=[{id:1, year:1999, coin:1, shape:1,
     quality:1, edge:1, material:1, standart:"Standart", denomination:"Denomination",
      mintage:1, additional_name:"NaN", km_number:"Number", is_rare:false, is_substyle:false,
    weight:10, length:30, width:40},
    {id:2, year:1988, coin:2, shape:1,
      quality:1, edge:1, material:1, standart:"Standart", denomination:"Denomination",
       mintage:1, additional_name:"NaN", km_number:"Number", is_rare:true, is_substyle:true,
     weight:10, length:30, width:40}
  ]
  
  shapes: Shape[]=[{id:1, name:"Shape1"}];
  qualities : Quality[]=[{id:1, name:"Quality1"}];
  edges : Edge[]=[{id:1, name:"Edge1"}];
  materials : Material[]=[{id:1, name:"Material1"}];

  subStyles:SubStyle[]=[{id:1, parent_coin:1, substyle_coin:2 }];
  note = new Note;
  images:Image[]=[{id:1, side:"front", coin_style:1, path:"https://dh.img.tyt.by/n/zamirovskiy/06/b/04_pushkinskaya_20200815_zam_tutby_phsl.jpg"},
  {id:2, side:"back", coin_style:1, path:"https://dh.img.tyt.by/n/buryakina/08/c/photo_2020-08-15_16-32-09.jpg"}];

  selectedCoin=new Coin();
  createMode:Boolean=false;
  editMode:Boolean=false;
  

  coinGroup:FormGroup= new FormGroup(
    {
      collectionControl:new FormControl("", [Validators.minLength(1), Validators.required]),
      nameControl:new FormControl("", [Validators.minLength(1), Validators.required]),
      mintedByControl:new FormControl("", [Validators.minLength(1), Validators.required]),
      authorControl:new FormControl(""),
      sculptorControl:new FormControl(""),
      authorFrontControl:new FormControl(""),
      sculptorFrontControl:new FormControl(""),
      authorBackControl:new FormControl(""),
      sculptorBackControl:new FormControl(""),
      authorEdgeControl:new FormControl(""),
      sculptorEdgeControl:new FormControl(""),
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
      multipleControl:new FormControl(""),
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
  
  allCoinAuthors:CoinAuthor[]=[{id:1, coin:1, author:1, side:'front'},
  {id:2, coin:1, author:1, side:'back'}, {id:3, coin:2, author:1}];

  allCoinSculptors:CoinSculptor[]=[{id:1, coin:1, sculptor:1, side:'front'},
  {id:2, coin:1, sculptor:1, side:'back'}, {id:3, coin:2, sculptor:1}];

  coinAuthors:CoinAuthor[]=[];
  coinSculptors:CoinSculptor[]=[];    
  coinInfo:CoinInfo[]=[];
  selectedId:number;
  

  constructor(private service:CoinsService) { }

  ngOnInit(): void {
    this.note.id=1;
    this.note.description="This is fucking description";
    //this.loadValues();
    this.coinGroup.controls['multipleControl']
    .valueChanges
    .subscribe((val)=>{
      if (val!=this.coinGroup.controls['multipleControl'].value)
      {
        this.coinAuthors=[];
        this.coinSculptors=[];
      }
    })
    
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

  addNewSculptor(sculptor:number, side?:string){
    var coinSculptor = new CoinSculptor();
    coinSculptor.sculptor = sculptor;
    if (side) coinSculptor.side=side;
    this.coinSculptors.push(coinSculptor);
    
  }

  addNewAuthor(author:number, side?:string){
    
    var coinAuthor = new CoinAuthor();
    coinAuthor.author = author;
    if (side) coinAuthor.side=side;
    this.coinAuthors.push(coinAuthor);
    
  }

  filterCoinAuthors(side:string):CoinAuthor[]{
    return this.coinAuthors.filter(aut=>aut.side==side);
  }

  filterCoinSculptors(side:string):CoinSculptor[]{
    
    return this.coinSculptors.filter(scu=>scu.side==side);
  }

  hasSculptor(side?:string):Sculptor[]{
    if (side==null)
      return this.sculptors.filter(sc=>this.coinSculptors.find(id=>id.sculptor==sc.id && id.side==side)==null);
    else
      return this.sculptors.filter(sc=>this.coinSculptors.find(id=>id.sculptor==sc.id && id.side==side)==null); 
  }

  hasAuthor(side?:string):Author[]{
    if (side==null)
      return this.authors.filter(au=>this.coinAuthors.find(id=>id.author==au.id)==null);
    else
      return this.authors.filter(sc=>this.coinAuthors.find(id=>id.author==sc.id && id.side==side)==null);   
  }

  removeSculptor(index:number){
    this.coinSculptors.splice(index,1);
  }

  removeAuthor(index:number){
    this.coinAuthors.splice(index,1);
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
    
    let note = new Note();
    
    note.description = this.coinGroup.controls["noteControl"].value;
    coin.collection = this.coinGroup.controls["collectionControl"].value;
    coin.mintedBy = this.coinGroup.controls["mintedByControl"].value;
    coin.name = this.coinGroup.controls["nameControl"].value;
    coinStyl.is_rare = this.coinGroup.controls["rareControl"].value;
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
    coinStyl.edge = this.coinGroup.controls["edgeControl"].value;
    coinStyl.denomination = this.coinGroup.controls["denominationControl"].value;
    coinStyl.additional_name = this.coinGroup.controls["additionalNameControl"].value;
    this.coinGroup.reset();
    this.clearPaths();
    coinInf.coin = coin;
    coinInf.style = coinStyl;
    coinInf.images = imgs;
    coinInf.coinAuthors=this.coinAuthors;
    coinInf.coinSculptors = this.coinSculptors;
    coinInf.note = note;

    this.coinInfo.push(coinInf);
    
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

  updateStyle(){
    
    let imgs:Image[]=[
      {side:"Front", file:this.frontFile},
      {side:"Back", file:this.backFile},
      {side:"Edge", file:this.edgeFile}
    ];
    
    
    this.coinInfo[this.selectedId].images[0].file=this.frontFile;
    this.coinInfo[this.selectedId].images[1].file=this.backFile;
    this.coinInfo[this.selectedId].images[2].file=this.edgeFile;
    this.coinInfo[this.selectedId].note.description = this.coinGroup.controls["noteControl"].value;
    this.coinInfo[this.selectedId].coin.collection = this.coinGroup.controls["collectionControl"].value;
    this.coinInfo[this.selectedId].coin.mintedBy = this.coinGroup.controls["mintedByControl"].value;
    this.coinInfo[this.selectedId].coin.name = this.coinGroup.controls["nameControl"].value;
    this.coinInfo[this.selectedId].style.is_rare = this.coinGroup.controls["rareControl"].value;
    this.coinInfo[this.selectedId].style.km_number = this.coinGroup.controls["kmNumberControl"].value;
    this.coinInfo[this.selectedId].style.length = this.coinGroup.controls["lengthControl"].value;
    this.coinInfo[this.selectedId].style.material = this.coinGroup.controls["materialControl"].value;
    this.coinInfo[this.selectedId].style.mintage = this.coinGroup.controls["mintageControl"].value;
    this.coinInfo[this.selectedId].style.quality = this.coinGroup.controls["qualityControl"].value;
    this.coinInfo[this.selectedId].style.shape = this.coinGroup.controls["shapeControl"].value;
    this.coinInfo[this.selectedId].style.standart = this.coinGroup.controls["standartControl"].value;
    this.coinInfo[this.selectedId].style.weight = this.coinGroup.controls["weightControl"].value;
    this.coinInfo[this.selectedId].style.width = this.coinGroup.controls["widthControl"].value;
    this.coinInfo[this.selectedId].style.year = this.coinGroup.controls["yearControl"].value;
    this.coinInfo[this.selectedId].style.edge = this.coinGroup.controls["edgeControl"].value;
    this.coinInfo[this.selectedId].style.denomination = this.coinGroup.controls["denominationControl"].value;
    this.coinInfo[this.selectedId].style.additional_name = this.coinGroup.controls["additionalNameControl"].value;
    this.coinInfo[this.selectedId].coinAuthors=this.coinAuthors;
    this.coinInfo[this.selectedId].coinSculptors = this.coinSculptors;
    
  }

  showCoinById(id:number){
    
    this.coinGroup.controls["collectionControl"].setValue(this.coinInfo[id].coin.collection);
    this.coinGroup.controls["noteControl"].setValue(this.coinInfo[id].note.description);
    this.coinGroup.controls["mintedByControl"].setValue(this.coinInfo[id].coin.mintedBy);
    this.coinGroup.controls["nameControl"].setValue(this.coinInfo[id].coin.name);
    this.coinGroup.controls["edgeControl"].setValue(this.coinInfo[id].style.edge);
    this.coinGroup.controls["denominationControl"].setValue(this.coinInfo[id].style.denomination);
    this.coinGroup.controls["additionalNameControl"].setValue(this.coinInfo[id].style.additional_name);
    this.coinGroup.controls["rareControl"].setValue(this.coinInfo[id].style.is_rare);
    this.coinGroup.controls["kmNumberControl"].setValue(this.coinInfo[id].style.km_number);
    this.coinGroup.controls["lengthControl"].setValue(this.coinInfo[id].style.length);
    this.coinGroup.controls["materialControl"].setValue(this.coinInfo[id].style.material);
    this.coinGroup.controls["mintageControl"].setValue(this.coinInfo[id].style.mintage);
    this.coinGroup.controls["qualityControl"].setValue(this.coinInfo[id].style.quality);
    this.coinGroup.controls["shapeControl"].setValue(this.coinInfo[id].style.shape);
    this.coinGroup.controls["standartControl"].setValue(this.coinInfo[id].style.standart);
    this.coinGroup.controls["weightControl"].setValue(this.coinInfo[id].style.weight);
    this.coinGroup.controls["widthControl"].setValue(this.coinInfo[id].style.width);
    this.coinGroup.controls["yearControl"].setValue(this.coinInfo[id].style.year);
    this.coinAuthors = this.coinInfo[id].coinAuthors;
    this.coinSculptors = this.coinInfo[id].coinSculptors;
    this.images = this.coinInfo[id].images;
    if (this.coinInfo[id].coinAuthors.some(aut=>aut.side!=null) ||
        this.coinInfo[id].coinSculptors.some(scu=>scu.side!=null)
        )
          this.coinGroup.controls["multipleControl"].setValue(true);
    if (this.images[0]!=null)
      this.frontPath = this.images[0].path;
    if (this.images[1]!=null)
      this.backPath = this.images[1].path;
    if (this.images[2]!=null)
      this.edgePath = this.images[2].path;
  }

  changeCreateMode(){
    this.createMode=!this.createMode;
    if (this.editMode) this.editMode=false;
    this.coinAuthors=[];
    this.coinSculptors=[];    
    this.coinInfo=[];
    this.coinGroup.reset();
    this.clearPaths();
   
    
  }

  selectCoin(coin:Coin){

    this.changeCreateMode();
    let coinInf = new CoinInfo();
    coinInf.coin = coin;
    coinInf.style = this.coinsStyles.find(st=>st.coin==coin.id); //= this.service.getCoinsStyleById(coin.id);
    coinInf.note = this.note; //service.getNote(coin.id);
    coinInf.coinAuthors = this.allCoinAuthors.filter(aut=>aut.coin == coin.id);// = this.service.getCoinAuthorsById(coin.id);
    coinInf.coinSculptors = this.allCoinSculptors.filter(scu=>scu.coin == coin.id);// = this.service.getCoinSculptorsById(coin.id);
    coinInf.images = this.images.filter(img=>img.coin_style == coinInf.style.id); // = this.service.getImagesById(coin.id);
    this.coinInfo.push(coinInf);
    /*this.service.getSubstylesById(coin.id).subscribe(styles=>
      {
        styles.forEach(sub=>
          {
            coinInf = new CoinInfo();
            coinInf.coin = this.coins.find(c=>c.id==sub.substyle_coin);
            coinInf.style = this.coinsStyles.find(st=>st.coin==sub.substyle_coin); // = this.service.getCoinsStyleById(sub.substyle_coin);
            coinInf.note = this.note; //service.getNote(sub.substyle_coin);
            coinInf.coinAuthors = this.allCoinAuthors.filter(aut=>aut.coin == sub.substyle_coin); // = this.service.getCoinAuthorsById(sub.substyle_coin);
            coinInf.coinSculptors = this.allCoinSculptors.filter(scu=>scu.coin == sub.substyle_coin); // = this.service.getCoinSculptorsById(sub.substyle_coin);
            coinInf.images = this.images.filter(img=>img.coin_style == coinInf.style.id); // = this.service.getImagesById(sub.substyle_coin);
            this.coinInfo.push(coinInf);
          }
          )
      }
      )*/

    this.subStyles.filter(sub=>sub.parent_coin==coin.id).forEach(
      sub=>{
        coinInf = new CoinInfo();
        coinInf.coin = this.coins.find(c=>c.id==sub.substyle_coin);
        coinInf.style = this.coinsStyles.find(st=>st.coin==sub.substyle_coin);
        coinInf.note = this.note; //service.getNote(sub.substyle_coin);
        coinInf.coinAuthors = this.allCoinAuthors.filter(aut=>aut.coin == sub.substyle_coin);
        coinInf.coinSculptors = this.allCoinSculptors.filter(scu=>scu.coin == sub.substyle_coin);
        coinInf.images = this.images.filter(img=>img.coin_style == coinInf.style.id);
        this.coinInfo.push(coinInf);
        
      }
      );

    this.editMode = true;
    this.showCoinById(0);  
    

  }

  loadValues(){
    this.service.getAllAuthors().subscribe(author=>this.authors=author);
    this.service.getAllCoins().subscribe(coins=>this.coins=coins);
    this.service.getAllCollections().subscribe(coll=>this.collections=coll);
    this.service.getAllEdges().subscribe(edge=>this.edges=edge);
    this.service.getAllMaterials().subscribe(mat=>this.materials=mat);
    this.service.getAllMintedBy().subscribe(mb=>this.mintedBy=mb);
    this.service.getAllQualities().subscribe(qual=>this.qualities=qual);
    this.service.getAllSculptors().subscribe(scu=>this.sculptors=scu);
    this.service.getAllShapes().subscribe(sha=>this.shapes=sha);
    
    
  }

  updateCoin(){
    
    this.service.updateCoin(this.coinInfo).subscribe(()=>
    {
      this.service.getAllCoins();
      this.changeCreateMode();
      this.editMode=false;
    }
    );
  }
  
  createCoin(){
    
    this.service.createCoin(this.coinInfo).subscribe(()=>
    {
      this.service.getAllCoins();
      this.changeCreateMode();
    }
    )
  }

  deleteCoin(id:number){
    this.service.deleteCoin(id).subscribe(()=>
    {
      this.service.getAllCoins();
    }
    )

  }

}
