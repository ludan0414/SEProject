import { createApp } from "vue";
import App from "./App.vue";
import "./style.css";
import router from "./router"; 
import { initAuth } from "./auth";

import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'

// 初始化本地存储中的认证状态
initAuth();

const app = createApp(App);
app.use(router); // ✅ 启用路由
app.use(mavonEditor);
app.mount("#app");
