<template>
  <nav class="navbar">
    <div class="logo">PKULab</div>
    <div class="nav-links">
      <a href="#">首页</a>
      <a href="#">热门</a>
      <a href="#">排行榜</a>
    </div>
    <div class="search-outer">
      <form class="search-bar" @submit.prevent="search">
        <input v-model="keyword" placeholder="搜索课程资料..." aria-label="搜索" />
        <button type="submit" class="search-btn" aria-label="搜索">🔍</button>
      </form>
    </div>
    <div class="user-icons">
      <span class="bell">🔔</span>
      <!-- 未登录时显示登录按钮，已登录时显示用户信息 -->
      <div class="user-area">
        <button v-if="!user" class="login-btn" @click="goLogin">登录</button>

        <div v-else class="user-info">
          <img :src="user.avatar || defaultAvatar" alt="avatar" class="avatar" />

          <!-- 下拉菜单：hover 时显示；把用户名放到菜单顶部 -->
          <div class="user-dropdown">
            <div class="dropdown-header">
              <div class="dropdown-username">{{ user.name }}</div>
              <div class="dropdown-email">{{ user.email }}</div>
            </div>
            <button class="dropdown-item" @click="goProfile">个人资料</button>
            <button class="dropdown-item" @click="doLogout">登出</button>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import { auth, logout } from "../auth";

const keyword = ref("");
const search = () => alert(`搜索: ${keyword.value}`);

const router = useRouter();
const user = computed(() => auth.user);
const defaultAvatar = 
  "https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp&s=40";

const goLogin = () => {
  router.push("/login");
};

const goProfile = () => {
  // 导航到个人资料页面（如无该路由，可自行实现或修改）
  router.push("/profile");
};

const doLogout = () => {
  logout();
  // 跳回首页
  router.push("/");
};
</script>

<style scoped>
.navbar {
  background: white;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 40px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
}

.logo {
  font-size: 22px;
  font-weight: 700;
  color: #0057ff;
}

.logo {
  /* 保持在左侧且不伸缩 */
  flex: 0 0 auto;
}

.nav-links {
  display: flex;
  align-items: center;
  /* 不参与拉伸，固定在 logo 右侧 */
  flex: 0 0 auto;
  margin-left: 16px;
}

.nav-links a {
  margin: 0 14px;
  text-decoration: none;
  color: #333;
  font-weight: 500;
}

.search-outer {
  /* 外层负责伸展并把内部搜索框大体居中 */
  display: flex;
  flex: 1 1 0%;
  justify-content: center;
  margin: 0 16px;
}

.search-bar {
  /* 内层承载视觉样式并限制最大宽度 */
  display: flex;
  align-items: center;
  position: relative;
  width: 100%;
  max-width: 520px;

  padding: 6px 8px;
  border-radius: 999px;
  border: 1px solid #e6e9ef;
  background: #fff;
  transition: box-shadow 160ms ease, border-color 160ms ease;
}

.search-bar:focus-within {
  border-color: #cbdcff;
  box-shadow: 0 8px 24px rgba(79,114,255,0.08);
}

.search-bar input {
  padding: 8px 12px;
  border: 0;
  background: transparent;
  /* 输入占据剩余空间 */
  flex: 1 1 auto;
  min-width: 0; /* 防止在 flex 容器中溢出 */
  outline: none;
}

.search-btn {
  margin-left: 8px;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: none;
  background: #0057ff;
  color: white;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 6px 18px rgba(0,87,255,0.12);
  transition: transform 120ms ease, box-shadow 120ms ease, background 120ms ease;
}

.search-btn:hover {
  transform: scale(1.04);
  background: #0046d6;
}

.user-area {
  display: inline-flex;
  align-items: center;
}

.login-btn {
  background: transparent;
  border: 1px solid #0057ff;
  color: #0057ff;
  padding: 6px 12px;
  border-radius: 8px;
  cursor: pointer;
  margin-left: 10px;
}

.avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
}

.dropdown-header {
  padding: 8px 12px;
  border-bottom: 1px solid #f0f0f5;
  margin-bottom: 6px;
}

.dropdown-username {
  font-weight: 700;
  color: #222;
}

.dropdown-email {
  font-size: 12px;
  color: #777;
  margin-top: 2px;
}

.logout-btn {
  background: #f44336;
  color: white;
  border: none;
  padding: 6px 10px;
  border-radius: 8px;
  cursor: pointer;
}

/* 新增下拉菜单样式 */
.user-info {
  position: relative; /* 使下拉菜单绝对定位相对于此容器 */
  display: inline-flex;
  align-items: center;
  cursor: default;
}

.user-dropdown {
  /* 使用 opacity + transform + visibility 做动画（避免 display 切换导致无法过渡） */
  position: absolute;
  right: 0;
  top: calc(100% + 8px);
  background: white;
  box-shadow: 0 6px 18px rgba(0,0,0,0.08);
  border-radius: 8px;
  padding: 6px;
  min-width: 140px;
  z-index: 120; /* 保证下拉在最上层，覆盖缓冲区伪元素 */

  opacity: 0;
  transform: translateY(-6px);
  visibility: hidden;
  pointer-events: none;
  transition: opacity 160ms cubic-bezier(.2,.8,.2,1), transform 160ms cubic-bezier(.2,.8,.2,1);
}

.user-info:hover .user-dropdown,
.user-info:focus-within .user-dropdown {
  opacity: 1;
  transform: translateY(0);
  visibility: visible;
  pointer-events: auto;
}

/* 在 user-info 和下拉菜单之间创建一个透明的缓冲区，避免 hover 空隙导致菜单闪烁收起 */
.user-info::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  top: 100%;
  height: 10px; /* 缓冲高度，可按需调整 8-12px */
  /* 允许接收鼠标事件以维持父元素的 :hover 状态，从而避免菜单闪烁 */
  z-index: 100; /* 放在内容之下，但低于 .user-dropdown 的 z-index */
}

.dropdown-item {
  display: block;
  width: 100%;
  text-align: left;
  padding: 8px 12px;
  background: transparent;
  border: none;
  cursor: pointer;
  color: #333;
}

.dropdown-item:hover {
  background: #f5f7ff;
}

/* 让 bell 与用户区在同一行垂直居中 */
.bell {
  margin-right: 16px;
  display: inline-flex;
  align-items: center;
}

.user-icons {
  display: flex;
  align-items: center;
  flex: 0 0 auto;
}
</style>
