import { reactive } from "vue";

export const auth = reactive({
  user: null,
  token: null,
});

export function login(user, token) {
  auth.user = user;
  auth.token = token;
  try {
    localStorage.setItem("auth_user", JSON.stringify(user));
    localStorage.setItem("auth_token", token);
  } catch (e) {
    console.warn("存储 auth 信息时出错", e);
  }
}

export function logout() {
  auth.user = null;
  auth.token = null;
  try {
    localStorage.removeItem("auth_user");
    localStorage.removeItem("auth_token");
  } catch (e) {
    console.warn("移除 auth 信息时出错", e);
  }
}

export function initAuth() {
  try {
    const rawUser = localStorage.getItem("auth_user");
    const rawToken = localStorage.getItem("auth_token");
    if (rawUser) auth.user = JSON.parse(rawUser);
    if (rawToken) auth.token = rawToken;
  } catch (e) {
    console.warn("初始化 auth 时出错", e);
  }
}

export default {
  auth,
  login,
  logout,
  initAuth,
};
