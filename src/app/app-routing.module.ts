import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {LoginComponent} from './login/login.component';
import {CatalogComponent} from './catalog/catalog.component';
import {ProfileComponent} from './profile/profile.component';
import {CoinInfoComponent} from './coin-info/coin-info.component'



const routes: Routes = [
  {path:"", redirectTo:"/login", pathMatch:"full"},
  {path:"login", component:LoginComponent},
  {path:"catalog", component:CatalogComponent},
  {path:"profile", component:ProfileComponent},
  {path:"coinInfo", component:CoinInfoComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
