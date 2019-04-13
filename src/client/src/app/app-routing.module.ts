import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import {routesList} from './routes'

const routes: Routes = routesList;

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
