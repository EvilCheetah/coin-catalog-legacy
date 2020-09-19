import { Component, OnInit } from '@angular/core';
import {FormControl, Validators} from '@angular/forms';
import {CategoriesService} from './categories.service';
import {Country} from 'src/app/classes/country';
import {Category} from 'src/app/classes/category';

@Component({
  selector: 'app-categories',
  templateUrl: './categories.component.html',
  styleUrls: ['./categories.component.css']
})
export class CategoriesComponent implements OnInit {

  constructor(private service:CategoriesService) { }

  categories:Category[]=[
    
  ];

  selectedCategory=new Category();
  createMode:boolean=false;

  countries:Country[]=[
    
  ];

  countryControl=new FormControl('',[Validators.required, Validators.minLength(1)]);
  nameControl=new FormControl('',[Validators.required, Validators.minLength(1)] );

  ngOnInit(): void {
    this.loadCategories();
    this.loadCountries();
  }
  loadCategories(){
    this.service.getAllCategories().subscribe((data)=>this.categories=data);
  }
  loadCountries(){
    this.service.getAllCountries().subscribe((data)=>this.countries=data)
  }

  getCountryName(id:number):string{
    return this.countries.find(cn=>cn.id==id).name;
  }

  selectCategory(category:Category){
    this.countryControl.setValue(category.country);
    this.nameControl.setValue(category.name);
    this.selectedCategory=category;
  }

  changeCreateMode()
  {
    this.cancelEdit();
    this.countryControl=new FormControl('', [Validators.minLength(1), Validators.required]);
    this.nameControl=new FormControl('', [Validators.minLength(1), Validators.required]);
    this.createMode=!this.createMode;
  }

  cancelEdit()
  {
    this.countryControl=new FormControl('', [Validators.minLength(1), Validators.required]);
    this.nameControl=new FormControl('', [Validators.minLength(1), Validators.required]); 
    this.selectedCategory=new Category();
  }

  saveEdit(){
    if (this.countryControl.valid && this.nameControl.valid)
    {
      let category = new Category();
      category.id = this.selectedCategory.id;
      category.country=this.countryControl.value;
      category.name = this.countryControl.value;
      this.service.editCategory(category).subscribe(()=>
      {
        this.loadCategories();
        this.cancelEdit();
      });
    }
  }

  createCategory(){
    if (this.countryControl.valid && this.nameControl.valid)
    {
      let category = new Category();
      category.country=this.countryControl.value;
      category.name = this.countryControl.value;
      this.service.createCategory(category).subscribe(()=>this.loadCategories());
      this.changeCreateMode();
    }
  }

  deleteCategory(id:number){
    this.service.deleteCategory(id).subscribe(()=>this.loadCategories());
  }


}
