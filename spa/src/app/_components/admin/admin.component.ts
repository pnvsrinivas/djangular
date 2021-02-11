import { Component, OnInit } from '@angular/core';
import { first } from 'rxjs/operators';

import { User } from '../../_models/user';
import { UserService } from '../../_services/user.service';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.scss']
})
export class AdminComponent implements OnInit {

  loading = false;
  users: User[] = [];

  constructor(private userService: UserService) { }

  ngOnInit() {
      this.getUsers();
  }

  getUsers() {
    this.loading = true;
    this.userService.getAll().pipe(first()).subscribe(users => {
        this.loading = false;
        this.users = users;
    });
  }

  deleteUser(id: number) {
    this.loading = true;
    this.userService.deleteById(id).subscribe(user => {
      this.loading = false;
      this.getUsers();
    })
  }

}
