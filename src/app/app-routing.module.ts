import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {LoginComponent} from './login/login.component';
import {CatalogComponent} from './catalog/catalog.component';
import {ProfileComponent} from './profile/profile.component';
import {CoinInfoComponent} from './coin-info/coin-info.component'
import {CrudComponent} from './crud/crud.component';
import {CategoriesComponent} from './crud/categories/categories.component';
import {EdgesComponent} from './crud/characteristics/edges/edges.component';
import {MaterialsComponent} from './crud/characteristics/materials/materials.component';
import {QualitiesComponent} from './crud/characteristics/qualities/qualities.component';
import {ShapesComponent} from './crud/characteristics/shapes/shapes.component';
import {CoinsComponent} from './crud/coins/coins.component';
import {CollectionsComponent} from './crud/collections/collections.component';
import {CountriesComponent} from './crud/countries/countries.component';
import {RegionsComponent} from './crud/regions/regions.component';
import {UsersComponent} from './crud/users/users.component';
import { ArtistsComponent } from './crud/authors/artists/artists.component';
import { SculptorsComponent } from './crud/authors/sculptors/sculptors.component';



const routes: Routes = [
  {path:"", redirectTo:"/login", pathMatch:"full"},
  {path:"login", component:LoginComponent},
  {path:"crud", component:CrudComponent, children:
  [
    {path:'artists', component:ArtistsComponent},
    {path:'sculptors', component:SculptorsComponent},
    {path:'categories', component:CategoriesComponent},
    {path:'edges', component:EdgesComponent},
    {path:'materials', component:MaterialsComponent},
    {path:'qualities', component:QualitiesComponent},
    {path:'shapes', component:ShapesComponent},
    {path:'coins', component:CoinsComponent},
    {path:'collections', component:CollectionsComponent},
    {path:'coutries', component:CountriesComponent},
    {path:'regions', component:RegionsComponent},
    {path:'users', component:UsersComponent},

  ]},
  {path:"catalog", component:CatalogComponent},
  {path:"profile", component:ProfileComponent},
  {path:"coinInfo", component:CoinInfoComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
