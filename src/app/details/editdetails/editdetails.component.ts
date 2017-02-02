import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Router } from '@angular/router';
import { DataService } from '../../services/service.service';
@Component({
  selector: 'app-editdetails',
  templateUrl: './editdetails.component.html',
  styleUrls: ['./editdetails.component.css']
})
export class EditdetailsComponent implements OnInit, OnDestroy {
  sub;
  id;
  platenumber;
  infolist: any[];
  public datas = [];
  model;
  constructor(private route: ActivatedRoute, private dataService: DataService,private router:Router) {

  }


  ngOnInit() {
    this.carinfo()

    this.sub = this.route.params.subscribe(params => {
      this.id = params['car']; // (+) converts string 'id' to a number
      // console.log(this.id);
      // In a real app: dispatch action to load the details here.
    });




  }
  ngOnDestroy() {
    this.sub.unsubscribe();
  }

  carinfo() {
    return this.dataService.info().subscribe(data => {
      let infolist = data;
      // console.log(infolist)
      let i = infolist.filter(
        data => data.plateno === this.id);

      this.datas = i[0]
      // console.log( this.datas)
      // infolist.forEach(element => {
      //   element
      // });

    });
  }

   onback(){
    console.log('back  to details!!');
    this.router.navigate(['/details',this.id]);
  }



   onupdate(){
console.log(this.model);
    console.log('successful update!!');
  }

}
