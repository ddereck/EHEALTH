import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/pages/HomePage.vue';
import SignIn from '../views/pages/SignIn.vue';
import SignUp from '../views/pages/SignUp.vue';
import SuperAdmin from '../views/pages/SuperAdmin.vue';

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage
  },
  // Définissez les autres routes ici
  {
    path: '/SignIn',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/SignUp',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/SuperAdmin',
    name: 'SuperAdmin',
    component: SuperAdmin
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
