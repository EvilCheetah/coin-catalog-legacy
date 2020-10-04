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
import { Side } from 'src/app/classes/side';






@Component({
  selector: 'app-coins',
  templateUrl: './coins.component.html',
  styleUrls: ['./coins.component.css']
})
export class CoinsComponent implements OnInit {

  coins:Coin[]=[];

  collections:Collection[]=[];
  authors:Author[]=[];
  sculptors:Sculptor[]=[];
  mintedBy:MintedBy[]=[];
  sides:Side[]=[];

  coinsStyles:CoinStyle[]=[]
  
  shapes: Shape[]=[];
  qualities : Quality[]=[];
  edges : Edge[]=[];
  materials : Material[]=[];

  subStyles:SubStyle[]=[];
  note = new Note;
  images:Image[]=[];

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
      lengthControl:new FormControl("", []),
      widthControl:new FormControl("", [ Validators.required]),
      thicknessControl:new FormControl("", [Validators.required]),
      noteControl:new FormControl("")
    }
  );
  
  paths:any[]=[];
  
  files:File[]=[];
  
  allCoinAuthors:CoinAuthor[]=[];

  allCoinSculptors:CoinSculptor[]=[];

  coinAuthors:CoinAuthor[]=[];
  coinSculptors:CoinSculptor[]=[];    
  coinInfo:CoinInfo[]=[];
  selectedId:number;
  sideId:number;
  

  constructor(private service:CoinsService) { }

  ngOnInit(): void {
    this.loadValues();
    this.sides.forEach(side => {
      this.coinGroup.addControl('author'+side.name+'Control', new FormControl());
      this.coinGroup.addControl('sculptor'+side.name+'Control', new FormControl())
    });
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
    this.paths.forEach(path=>path="assets/images/add.png");
    this.files.forEach(file=>file=null);

    
    
  }

  previewFile(event){
    this.files[this.sideId]=<File>event.target.files[0];
    var reader = new FileReader();
    reader.readAsDataURL(this.files[this.sideId]);
    reader.onload=((fl)=>{
      this.paths[this.sideId]=reader.result;
    })
  }
 
  addNewSculptor(sculptor:number, side?:number){
    var coinSculptor = new CoinSculptor();
    coinSculptor.sculptor = sculptor;
    if (side) coinSculptor.side=side;
    this.coinSculptors.push(coinSculptor);
  }

  addNewAuthor(author:number, side?:number){
    var coinAuthor = new CoinAuthor();
    coinAuthor.author = author;
    if (side) coinAuthor.side=side;
    this.coinAuthors.push(coinAuthor);
  }

  filterCoinAuthors(side:number):CoinAuthor[]{
    return this.coinAuthors.filter(aut=>aut.side==side);
  }

  filterCoinSculptors(side:number):CoinSculptor[]{
    
    return this.coinSculptors.filter(scu=>scu.side==side);
  }

  hasSculptor(side?:number):Sculptor[]{
    if (side==null)
      return this.sculptors.filter(sc=>this.coinSculptors.find(id=>id.sculptor==sc.id && id.side==side)==null);
    else
      return this.sculptors.filter(sc=>this.coinSculptors.find(id=>id.sculptor==sc.id && id.side==side)==null); 
  }

  hasAuthor(side?:number):Author[]{
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
    /*let imgs:Image[]=[
      {side:"Front", file:this.frontFile},
      {side:"Back", file:this.backFile},
      {side:"Edge", file:this.edgeFile}
    ];*/
    
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
    this.files.forEach(
      (file, index)=>coinInf.images.push(new Image(this.sides[index].id, file))
      )
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
    
    this.coinInfo[this.selectedId].images=[];
    this.files.forEach(
      (file, index)=>this.coinInfo[this.selectedId].images.push(new Image(this.sides[index].id, file))
      )
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
    this.images.forEach(image => {
      if (image.path) this.paths.push(image.path)     
    });      
    
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
    this.coinInfo.push(this.getCoinInfo(coin));
    this.service.getSubstylesById(coin.id).subscribe(styles=>
      {
        styles.forEach(sub=>
          {
            this.service.getCoinById(sub.substyle_coin)
            .subscribe(coin=>this.coinInfo.push(this.getCoinInfo(coin)));
          }
          )
      }
      );
      /*
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
      );*/

    this.editMode = true;
    this.showCoinById(0);  
    

  }

  getCoinInfo(coin:Coin):CoinInfo{
    let coinInf = new CoinInfo();
    coinInf.coin = coin;
    this.service.getCoinsStyleById(coin.id).subscribe(style=>
      {
        coinInf.style=style;
        this.service.getNoteByStyleId(style.id).subscribe(note=>coinInf.note=note);
      });
    
    this.service.getCoinAuthorsById(coin.id).subscribe(ca=>coinInf.coinAuthors=ca);
    this.service.getCoinSculptorsById(coin.id).subscribe(cs=>coinInf.coinSculptors=cs);
    this.service.getImagesById(coin.id).subscribe(img=>coinInf.images=img);
    return coinInf;
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
    this.service.getAllSides().subscribe(side=>this.sides=side);
    
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
