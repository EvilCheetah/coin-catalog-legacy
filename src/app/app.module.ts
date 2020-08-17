import { BrowserModule } from '@angular/platform-browser';
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


@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    CatalogComponent,
    ProfileComponent,
    CoinInfoComponent,
    CrudComponent
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
