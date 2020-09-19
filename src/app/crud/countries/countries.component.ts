import { Component, OnInit } from '@angular/core';
import {FormControl, Validators} from '@angular/forms';
import {CountriesService} from './countries.service';
import {Region} from 'src/app/classes/region'
import {Country} from 'src/app/classes/country';

@Component({
  selector: 'app-countries',
  templateUrl: './countries.component.html',
  styleUrls: ['./countries.component.css']
})
export class CountriesComponent implements OnInit {

  constructor(private service:CountriesService) { }

  regions:Region[]=[];

  countries:Country[]=[];

  regionControl= new FormControl('',[Validators.required, Validators.minLength(1)]);

  nameControl = new FormControl('',[Validators.required, Validators.minLength(1)]);

  selectedCountry:Country = new Country();

  createMode:boolean=false;

  ngOnInit(): void {
    this.loadCountries();
    this.loadRegions();
  }

  loadCountries(){
    this.service.getAllCountries().subscribe((data)=>this.countries=data);
  }

  loadRegions(){
    this.service.getAllRegions().subscribe((data)=>this.regions=data);
  }

  changeCreateMode(){
    this.cancelEdit();
    this.createMode = !this.createMode;
    this.regionControl= new FormControl('',[Validators.required, Validators.minLength(1)]);
    this.nameControl = new FormControl('',[Validators.required, Validators.minLength(1)]);
  }

  getRegionName(id:number):string{
    return this.regions.find(region=>region.id==id).name;
  }

  selectCountry(country:Country){
    this.selectedCountry=country;
    this.nameControl.setValue(country.name);
    this.regionControl.setValue(country.region);
  }

  cancelEdit(){
    this.selectedCountry = new Country();
    this.regionControl= new FormControl('',[Validators.required, Validators.minLength(1)]);
    this.nameControl = new FormControl('',[Validators.required, Validators.minLength(1)]);
  }

  deleteCountry(id:number){
    this.service.deleteCountry(id).subscribe(()=>this.loadCountries());
  }

  createCountry(){
    let country = new Country();
    country.name = this.nameControl.value;
    country.region = this.regionControl.value;
    this.service.createCountry(country).subscribe(()=>
    {
      this.loadCountries();
      this.changeCreateMode();
    })
  }

  saveEdit(){
    let country = new Country();
    country.id = this.selectedCountry.id;
    country.name = this.nameControl.value;
    country.region = this.regionControl.value;
    this.service.editCountry(country).subscribe(()=>
    {
      this.loadCountries();
      this.cancelEdit();
    })
  }

}
