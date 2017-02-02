import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import 'rxjs/add/operator/map';

@Injectable()
export class DataService {
  data = [];
  constructor(public http: Http) { }

  info() {
    // return this.http.get('./assets/data.json')
    return this.http.get('http://localhost:8000/sb_api1/car/?format=json')
      .map(res => res.json());
  }

  save(datas) {
 
    let headers = new Headers();
    headers.append('Content-Type', 'application/json')
    let options = new RequestOptions({ headers: headers, method: 'post' });

    console.log(datas);
    // return this.http.post('./assets/data.json', datas);

    return this.http.post('http://localhost:8000/sb_api1/car/', datas, { headers: headers })
      .map(res => res.json())

  }
}
