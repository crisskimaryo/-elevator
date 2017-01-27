import { Injectable } from '@angular/core';
import 'rxjs/add/operator/map';

@Injectable()
export class DataService {
  data = [
    {
      id: 1,
      plateno: 'TZcse24',
      model: 'buggat',
      owner: 'eric kessy'
    },
    {
      id: 2,
      plateno: 'Crisskimaryo',
      model: 'Range Rover',
      owner: 'Christopher kimaryo'
    },
    {
      id: 3,
      plateno: 'TajiriMuhaya',
      model: 'hummer',
      owner: 'edmund'
    },
    {
      id: 4,
      plateno: 'TZgt3',
      model: 'benz  E class',
      owner: 'Agape'
    },
    {
      id: 5,
      plateno: 'TZc524',
      model: 'Roysrosy',
      owner: 'sylis lawi'
    }
  ]
  constructor() { }

  info() {
    return this.data.map(data => data);
  }

}
