import { createRouter, createWebHashHistory } from "vue-router";
import LoginView from "../views/LoginView.vue";
import HomeView from "../views/HomeView.vue";
import SignUpView from "../views/SignUpView.vue";
import ProfileView from "../views/ProfileView.vue"
import CommunityView from "../views/CommunityView"
import QuestionView from "../views/QuestionView"

const routes = [
  {
    name: "LoginView",
    component: LoginView,
    path: "/login",
  },
  {
    name: "SignUpView",
    component: SignUpView,
    path: "/signup",
  },
  {
    name: "HomeView",
    component: HomeView,
    path: '/'
  },
  {
    name: "ProfileView",
    component: ProfileView,
    path: '/profile'
  },
  {
    name: "CommunityView",
    component: CommunityView,
    path: '/community'
  },
  {
    name: "QuestionView",
    component: QuestionView,
    path: '/question'
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
