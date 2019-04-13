
import {HomeComponent} from './home/home.component'
import {AuthComponent} from './auth/auth.component'
import {EntryListComponent} from './entry-list/entry-list.component'
import {EntriesComponent} from './entries/entries.component'

export const routesList = [
    { path: '', component: HomeComponent},
    { path: 'entries', component: EntriesComponent},
    { path: 'list', component: EntryListComponent},
    { path: 'auth', component: AuthComponent},
]