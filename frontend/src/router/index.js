import { createRouter, createWebHistory } from "vue-router";
import DefaultLayout from "../layouts/DefaultLayout.vue";
import Home from "../pages/Home.vue";
import Login from "../pages/Login.vue";
import Register from "../pages/Register.vue"
import Blog from "../pages/Blog.vue";
import Profile from "../pages/Profile.vue";

const routes = [
  {
    path: "/",
    component: DefaultLayout,
    children: [
      { path: "", component: Home }, // 首页
  { path: "blog/:id", component: Blog},
  { path: "profile", component: Profile },
    ],
  },
  {
    path: "/login",
    component: Login,
  },
  {
    path: "/register",
    component: Register,
  }
];

export default createRouter({
  history: createWebHistory(),
  routes,
});
