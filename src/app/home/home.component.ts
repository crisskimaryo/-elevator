import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { DataService } from '../services/service.service';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  cars = [];
  constructor(private router: Router, public dataService: DataService) { }


  ngOnInit() {
    this.carinfo();
  }

  details(car) {
    let info = car.id;
    console.log(info);

    this.router.navigate(['/details', info]);
    console.log('hey your click me');
  }

  carinfo() {
    return this.cars = this.dataService.info();
  }
}
