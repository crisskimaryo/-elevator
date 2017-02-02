import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { HomeComponent } from './home/home.component';

import { EmptyComponent } from './app.component';
import { RegistationComponent } from './registation/registation.component';
import { LoginComponent } from './login/login.component';
import { DetailsComponent } from './details/details.component';
import { EditdetailsComponent } from './details/editdetails/editdetails.component';

const routes: Routes = [
    { path: '', redirectTo: 'index', pathMatch: 'full' },
    { path: 'index', component: EmptyComponent },
    { path: 'home', component: HomeComponent },
    { path: 'registation', component: RegistationComponent },
    { path: 'details/:car', component: DetailsComponent },
    { path: 'details/edit/:car', component: EditdetailsComponent },
    { path: 'login', component: LoginComponent },
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule],
    providers: []
})

export class RoutingModule { }