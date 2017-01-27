import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit() {
    let menu = false;
  }
  registercar() {
    this.router.navigate(['/registation']);
  }
  home() {
    this.router.navigate(['/home']);

  }
  login(log, menu) {
    this.router.navigate(['/home']);
    menu.hidden = false;
    log.hidden = true;
  }
  logout(log, menu) {
  this.router.navigate(['/index']);
    log.hidden = false;
    menu.hidden = true;
  }


}
