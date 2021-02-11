import { Role } from './role';

export class User {
    id: number;
    firstName?: string;
    lastName?: string;
    username: string;
    role: Role;
    token?: string;
    date_joining: string;
    is_active: boolean;
}