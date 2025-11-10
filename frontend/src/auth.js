import { reactive } from "vue";

// 简单的客户端认证状态管理（无后端）
export const auth = reactive({
  // user: { name, email, avatar }
  user: null,
});

export function login(user) {
  auth.user = user;
  try {
    localStorage.setItem("auth_user", JSON.stringify(user));
  } catch (e) {
    console.warn("存储 auth_user 时出错", e);
  }
}

export function logout() {
  auth.user = null;
  try {
    localStorage.removeItem("auth_user");
  } catch (e) {
    console.warn("移除 auth_user 时出错", e);
  }
}

export function initAuth() {
  try {
    const raw = localStorage.getItem("auth_user");
    if (raw) {
      auth.user = JSON.parse(raw);
    }
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
