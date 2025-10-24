// vite.config.mjs
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    port: 5173,
    historyApiFallback: true, // ✅ 确保浏览器刷新不丢路由
  },
})
