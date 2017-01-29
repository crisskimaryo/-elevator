import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
error;
  constructor(private router: Router) {
    this.error=false;
   }

  ngOnInit() {
    let menu = false;
  }
  registercar() {
    this.router.navigate(['/registation']);
  }
  home() {
    this.router.navigate(['/home']);

  }
  login(log, menu, form) {
   
    if (form.value.credential.password == "breezeboy" && form.value.credential.email =="crisskimaryo@gmail.com") {
      this.router.navigate(['/home']);
      menu.hidden = false;
      log.hidden = true;
       this.error=false;
    }
    else{
     this.error=true;
      console.log("log in fails")
     
    }

  }
  logout(log, menu) {
    this.router.navigate(['/index']);
    log.hidden = false;
    menu.hidden = true;
  }


}
