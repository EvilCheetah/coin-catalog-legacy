import { BrowserModule} from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import  {HttpClientModule} from '@angular/common/http';
import { ReactiveFormsModule } from '@angular/forms';
import {FormsModule} from '@angular/forms';
import { AppComponent } from './app.component';
import { CookieService } from 'ngx-cookie-service';
import { AppRoutingModule } from './app-routing.module';
import { LoginComponent } from './login/login.component';
import { CatalogComponent } from './catalog/catalog.component';
import { ProfileComponent } from './profile/profile.component';
import { CoinInfoComponent } from './coin-info/coin-info.component';
import { CrudComponent } from './crud/crud.component';
import {AuthorsComponent} from './crud/authors/authors.component';
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


@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    CatalogComponent,
    ProfileComponent,
    CoinInfoComponent,
    CrudComponent,
    AuthorsComponent,
    CategoriesComponent,
    EdgesComponent,
    MaterialsComponent,
    QualitiesComponent,
    ShapesComponent,
    CoinsComponent,
    CollectionsComponent,
    CountriesComponent,
    RegionsComponent,
    UsersComponent

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [CookieService],
  bootstrap: [AppComponent]
})
export class AppModule { }
