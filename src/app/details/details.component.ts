import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DataService } from '../services/service.service'
@Component({
  selector: 'app-details',
  templateUrl: './details.component.html',
  styleUrls: ['./details.component.css']
})
export class DetailsComponent implements OnInit, OnDestroy {
  sub;
  id;
  platenumber;
  infolist: any[];
  public datas = [];
  constructor(private route: ActivatedRoute, private dataService: DataService) {

  }

  ngOnInit() {
    this.carinfo()
    
    this.sub = this.route.params.subscribe(params => {
      this.id = params['car']; // (+) converts string 'id' to a number
      console.log(this.id);
      // In a real app: dispatch action to load the details here.
    });




  }
  ngOnDestroy() {
    this.sub.unsubscribe();
  }

  carinfo() {
    return this.dataService.info().subscribe(data => {
      let infolist = data
console.log(infolist[3].plateno)
      let i = infolist.filter(
        data => data.plateno === this.id);
      
      this.datas=i[0]
      console.log( this.datas)
      // infolist.forEach(element => {
      //   element
      // });

    });
  }
}
