import { Component, OnInit } from '@angular/core';
import {DataService} from '../services/service.service'
@Component({
  selector: 'app-registation',
  templateUrl: './registation.component.html',
  styleUrls: ['./registation.component.css']
})
export class RegistationComponent implements OnInit {
datas={}
plateNumber
modeltype
name
  constructor(public dataservice:DataService) { }

  ngOnInit() {
  }

save(){
  this.datas={
    id:"",
    plateno:this.plateNumber,
    model:this.modeltype,
    owner:this.name
  }
this.dataservice.save(this.datas)
console.log(this.datas);
console.log("done");

}
}
