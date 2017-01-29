import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { DataService } from '../services/service.service';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  public carlist;

  constructor(private router: Router, public dataService: DataService) { }


  ngOnInit() {
    this.carinfo();
  }

  details(car) {
    let info = car.plateno;
    let cars = car;
    console.log(info);

    this.router.navigate(['/details', info]);

  }

  carinfo() {
    return this.dataService.info().subscribe(data => {
      this.carlist=data;
      
    });
  }
}
