import { createRouter, createWebHistory } from "vue-router";
import DefaultLayout from "../layouts/DefaultLayout.vue";
import Home from "../pages/Home.vue";
import Login from "../pages/Login.vue";
import Blog from "../pages/Blog.vue";

const routes = [
  {
    path: "/",
    component: DefaultLayout,
    children: [
      { path: "", component: Home }, // 首页
      { path: "blog/:id", component: Blog},
    ],
  },
  {
    path: "/login",
    component: Login,
  },
];

export default createRouter({
  history: createWebHistory(),
  routes,
});
