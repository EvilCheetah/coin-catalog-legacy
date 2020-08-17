import { Component, OnInit } from '@angular/core';
import {FormControl, Validators } from '@angular/forms'
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';
import {LoginService} from './login.service'


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(private service:LoginService, private router:Router, private cookies:CookieService) { }

  login = new FormControl('',[Validators.minLength(1)]);
  password = new FormControl('');
  error:boolean=false;

  ngOnInit(): void {

  }

  onSubmit():void{
    if (this.login.valid && this.password.valid)
    this.service.checkUser(this.login.value, this.password.value).subscribe(
    (data)=>
    {
      if (data!= null)
      {
        this.cookies.set("User",JSON.stringify(data), 10);
        this.router.navigateByUrl("/catalog");
      } 
      else  this.error=true;
      
      
    }); 
  }

}
