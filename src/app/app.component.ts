import { Component } from '@angular/core';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app works!';
}



@Component({
  selector: 'app-empty',
  templateUrl: './empty.component.html',
  styles: ['']
})
export class EmptyComponent {}
