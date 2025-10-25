<template>
  <nav class="navbar">
    <div class="logo">PKULab</div>
    <div class="nav-links">
      <a href="#">首页</a>
      <a href="#">热门</a>
      <a href="#">排行榜</a>
    </div>
    <div class="search-bar">
      <input v-model="keyword" placeholder="搜索课程资料..." />
      <button @click="search">🔍</button>
    </div>
    <div class="user-icons">
      <span>🔔</span>
      <span>👤</span>
    </div>
  </nav>
</template>

<script setup>
import { ref } from "vue";
const keyword = ref("");
const search = () => alert(`搜索: ${keyword.value}`);
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

.nav-links a {
  margin: 0 14px;
  text-decoration: none;
  color: #333;
  font-weight: 500;
}

.search-bar {
  display: flex;
  align-items: center;
}

.search-bar input {
  padding: 6px 10px;
  border-radius: 8px 0 0 8px;
  border: 1px solid #ddd;
}

.search-bar button {
  border: none;
  background: #0057ff;
  color: white;
  padding: 7px 12px;
  border-radius: 0 8px 8px 0;
}

.user-icons span {
  margin-left: 12px;
  font-size: 20px;
}
</style>
