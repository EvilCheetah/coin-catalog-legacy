import { Component, OnInit } from '@angular/core';
import {FormControl, Validators} from '@angular/forms';
import {CollectionsService} from './collections.service';
import {Collection} from 'src/app/classes/collection'
import {Category} from 'src/app/classes/category';

@Component({
  selector: 'app-collections',
  templateUrl: './collections.component.html',
  styleUrls: ['./collections.component.css']
})
export class CollectionsComponent implements OnInit {

  constructor(private service:CollectionsService) { }

  collections:Collection[]=[];

  categories:Category[]=[];

  categoryControl= new FormControl('',[Validators.required, Validators.minLength(1)]);

  nameControl = new FormControl('',[Validators.required, Validators.minLength(1)]);

  selectedCollection:Collection = new Collection();

  createMode:boolean=false;

  ngOnInit(): void {
    this.loadCollection();
    this.loadCategories();
  }
  loadCollection(){
    this.service.getAllCollections().subscribe((data)=>this.collections=data);
  }
  loadCategories(){
    this.service.getAllCategories().subscribe((data)=>this.categories=data);
  }
  changeCreateMode(){
    this.cancelEdit();
    this.createMode = !this.createMode;
    this.categoryControl= new FormControl('',[Validators.required, Validators.minLength(1)]);
    this.nameControl = new FormControl('',[Validators.required, Validators.minLength(1)]);
  }

  getCategoryName(id:number):string{
    return this.categories.find(category=>category.id==id).name;
  }

  selectCollection(collection:Collection){
    this.selectedCollection=collection;
    this.nameControl.setValue(collection.name);
    this.categoryControl.setValue(collection.category);
  }

  cancelEdit(){
    this.selectedCollection = new Collection();
    this.categoryControl= new FormControl('',[Validators.required, Validators.minLength(1)]);
    this.nameControl = new FormControl('',[Validators.required, Validators.minLength(1)]);
  }

  deleteCollection(id:number){
    this.service.deleteCollection(id).subscribe(()=>this.loadCollection());
  }

  createCollection(){
    let collection = new Collection();
    collection.name = this.nameControl.value;
    collection.category = this.categoryControl.value;
    this.service.createCollection(collection).subscribe(()=>
    {
      this.loadCollection();
      this.changeCreateMode();
    })
  }

  saveEdit(){
    let collection = new Collection();
    collection.id = this.selectedCollection.id;
    collection.name = this.nameControl.value;
    collection.category = this.categoryControl.value;
    this.service.editCollection(collection).subscribe(()=>
    {
      this.loadCollection();
      this.cancelEdit();
    })
  }
}

