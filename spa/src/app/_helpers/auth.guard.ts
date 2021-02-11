import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, UrlTree, Router } from '@angular/router';
import { Observable } from 'rxjs';
import { AuthenticationService } from '../_services/authentication.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {

  constructor(private router: Router, private authService: AuthenticationService) {  }

  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {
      const user = this.authService.userValue;
      if(user) {
        // check if route is restricted by role
        if(route.data.roles && route.data.roles.indexOf(user.role) == -1){
          this.router.navigate(['/']);
          return false;
        }

        // authorized so return true
        return true;        
      }
      
      this.router.navigate(['/login'], { queryParams: { returnUrl: state.url } });
      return false;
  }
  
}
