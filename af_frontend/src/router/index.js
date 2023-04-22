import { createRouter, createWebHashHistory } from "vue-router";
import LoginComponent from "../components/LoginComponent.vue";
import HomeComponent from "../components/HomeComponent.vue";
import SignUpComponent from "../components/SignUpComponent.vue";

const routes = [
  {
    name: "LoginComponent",
    component: LoginComponent,
    path: "/",
  },
  {
    name: "SignUpComponent",
    component: SignUpComponent,
    path: "/signup",
  },
  {
    name: "HomeComponent",
    component:HomeComponent,
    path:'/home'
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
