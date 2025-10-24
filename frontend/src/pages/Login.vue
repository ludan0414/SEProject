<template>
  <div class="login-page">
    <NavBar />

    <div class="login-container">
      <div class="login-card">
        <h2>登录</h2>

        <form @submit.prevent="handleLogin">
          <label>邮箱</label>
          <input v-model="email" type="email" placeholder="请输入邮箱" required />

          <label>密码</label>
          <div class="password-box">
            <input
              v-model="password"
              :type="showPassword ? 'text' : 'password'"
              placeholder="请输入密码"
              required
            />
            <span class="toggle" @click="showPassword = !showPassword">
              {{ showPassword ? '隐藏' : '显示' }}
            </span>
          </div>

          <a href="#" class="forgot">忘记密码？</a>

          <button type="submit" class="login-btn">登录</button>
          <button type="button" class="register-btn" @click="goRegister">注册</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
// import NavBar from "../components/NavBar.vue";

const email = ref("");
const password = ref("");
const showPassword = ref(false);

const handleLogin = () => {
  if (!email.value || !password.value) {
    alert("请输入完整信息！");
    return;
  }
  // 模拟登录逻辑
  alert(`登录成功：${email.value}`);
  window.location.href = "/";
};

const goRegister = () => {
  alert("注册功能暂未开放。");
};
</script>

<style scoped>
.login-page {
  min-height: 100vh;
  background: linear-gradient(120deg, #ff3cac, #784ba0, #2b86c5);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.login-container {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-card {
  background: #fff;
  padding: 2.5rem;
  border-radius: 16px;
  width: 360px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.login-card h2 {
  text-align: center;
  margin-bottom: 1.5rem;
}

form {
  display: flex;
  flex-direction: column;
}

label {
  margin: 0.5rem 0 0.25rem;
}

input {
  padding: 0.6rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  margin-bottom: 0.75rem;
  width: 100%;
}

.password-box {
  position: relative;
}

.password-box .toggle {
  position: absolute;
  right: 10px;
  top: 8px;
  font-size: 0.85rem;
  color: #666;
  cursor: pointer;
}

.forgot {
  text-align: right;
  font-size: 0.85rem;
  color: #666;
  margin-bottom: 1rem;
  text-decoration: none;
}

.login-btn {
  background-color: #ccc;
  border: none;
  color: #fff;
  padding: 0.6rem;
  border-radius: 999px;
  cursor: pointer;
  margin-bottom: 0.75rem;
}

.register-btn {
  background-color: #2196f3;
  border: none;
  color: white;
  padding: 0.6rem;
  border-radius: 999px;
  cursor: pointer;
}
</style>
