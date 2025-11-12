<template>
  <div class="login-app-page">
    <NavBar></NavBar>
    <div class="login-page">
      <div class="login-container">
        <div class="login-card">
          <h2>登录</h2>

          <form @submit.prevent="handleLogin">
            <label>用户名</label>
            <input v-model="username" type="text" placeholder="请输入用户名" required />

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
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { login, auth } from "../auth";
import NavBar from "../components/NavBar.vue";

// 如果已登录，直接跳回首页
const router = useRouter();
if (auth.user) router.push("/");

const username = ref("");
const password = ref("");
const showPassword = ref(false);
const handleLogin = async () => {
  if (!username.value || !password.value) {
    alert("请输入完整信息！");
    return;
  }

  try {
    const res = await fetch("http://localhost:5000/api/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: username.value, // 后端要求 username
        password: password.value,
      }),
    });

    const data = await res.json();

    if (!res.ok) {
      alert(data.error || "登录失败");
      return;
    }

    // 登录成功：保存 token 和 user
    login(data.user, data.token);

    router.push("/");
  } catch (err) {
    console.error("登录请求失败", err);
    alert("服务器连接失败");
  }
};

const goRegister = () => {
  router.push("/register");
};
</script>

<style scoped>
*,
*::before,
*::after {
  box-sizing: border-box;
}

.login-app-page {
  display: flex;
  flex-direction: column;
  min-height: 100vh; /* 整个页面最小高度是屏幕高度 */
}

.login-page {
  flex: 1;
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
  width: 440px;
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
  display: inline; 
  font-size: 0.85rem;
  color: #666;
  text-decoration: none;
  margin-bottom: 1em;
  cursor: pointer;
  align-self: flex-end; /* 让文字靠右 */
}

.login-btn {
  background-color: #2196f3;
  border: none;
  color: #fff;
  padding: 0.6rem;
  border-radius: 999px;
  cursor: pointer;
  margin-bottom: 0.75rem;
  transition: background-color 0.3s;
}

.login-btn:hover {
  background-color: #1976d2;
}

.register-btn {
  background-color: #ccc;
  border: none;
  color: #333;
  padding: 0.6rem;
  border-radius: 999px;
  cursor: pointer;
  transition: background-color 0.3s;
}
.register-btn:hover {
  background-color: #bbb;
}
</style>
