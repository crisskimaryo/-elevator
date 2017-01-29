import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs/add/operator/map';

@Injectable()
export class DataService {
  data = [];
  constructor(public http: Http) { }

  info() {
    return this.http.get('./assets/data.json')
      .map(res => res.json());
  }

  save(datas) {
    return this.http.post('./assets/data.json', datas);
  }
}
