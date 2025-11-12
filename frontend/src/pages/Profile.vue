<template>
  <div class="profile-page">
    <div class="profile-container">
      <!-- 未登录提示 -->
      <div v-if="!user" class="notice card">
        <div>当前未登录，部分信息以示例展示。</div>
        <button class="btn btn-primary" @click="goLogin">去登录</button>
      </div>

      <!-- 顶部用户信息卡 -->
      <section class="user-card card">
        <img :src="avatarUrl" alt="avatar" class="avatar" />
        <div class="user-meta">
          <h1 class="username">{{ displayName }}</h1>
          <div class="email">{{ displayEmail }}</div>
          <div class="stats">
            <div class="stat"><span class="num">{{ posts.length }}</span><span class="label">博文</span></div>
            <div class="stat"><span class="num">{{ followingCount }}</span><span class="label">关注</span></div>
            <div class="stat"><span class="num">{{ followersCount }}</span><span class="label">粉丝</span></div>
          </div>
        </div>
      </section>

      <!-- 发布的博文列表 -->
      <section class="posts">
        <h2>发布的博文</h2>
        <div v-if="posts.length === 0" class="empty">暂时还没有发布的博文</div>
        <article
          v-for="p in posts"
          :key="p.id"
          class="post card"
          role="button"
          tabindex="0"
          @click="goPost(p.id)"
          @keydown.enter="goPost(p.id)"
          @keydown.space.prevent="goPost(p.id)"
        >
          <div class="post-header">
            <h3 class="post-title" @click.stop="goPost(p.id)">{{ p.title }}</h3>
            <div class="post-date">{{ formatDate(p.createdAt) }}</div>
          </div>
          <p class="post-excerpt">{{ p.excerpt }}</p>
          <div class="post-meta">
            <span>👍 {{ p.likes }}</span>
            <span>💬 {{ p.comments }}</span>
          </div>
        </article>
      </section>

      <!-- 活跃度热力图 -->
      <section class="activity card">
        <h2>活跃度</h2>
        <div class="heatmap">
          <div v-for="(week, wIdx) in heatmapData" :key="wIdx" class="heatmap-week">
            <div
              v-for="(day, dIdx) in week"
              :key="dIdx"
              class="heatmap-cell"
              :class="`level-${day.level}`"
              :title="`${day.date}: ${day.count} 篇`"
            ></div>
          </div>
        </div>
        <div class="heatmap-legend">
          <span>Less</span>
          <div class="legend-cell level-0"></div>
          <div class="legend-cell level-1"></div>
          <div class="legend-cell level-2"></div>
          <div class="legend-cell level-3"></div>
          <div class="legend-cell level-4"></div>
          <span>More</span>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { computed, ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { auth } from '../auth';

const router = useRouter();
const user = computed(() => auth.user);

const displayName = computed(() => user.value?.username || user.value?.name || '示例用户');
const displayEmail = computed(() => user.value?.email || 'demo@example.com');
const avatarUrl = computed(() => user.value?.avatar || `https://api.dicebear.com/6.x/identicon/svg?seed=${encodeURIComponent(displayEmail.value)}`);

// 静态示例数据（后续可替换为接口返回）
const followingCount = ref(12);
const followersCount = ref(48);
const posts = ref([
  { id: 101, title: '我的第一篇博文', createdAt: '2025-11-01T10:20:00Z', likes: 12, comments: 3, excerpt: '这是一段关于课程资料整理的内容摘要……' },
  { id: 102, title: '操作系统复习笔记', createdAt: '2025-11-08T14:05:00Z', likes: 34, comments: 8, excerpt: '从进程、线程、内存管理到文件系统的系统化梳理……' },
  { id: 103, title: '计算机网络知识清单', createdAt: '2025-11-12T09:30:00Z', likes: 21, comments: 6, excerpt: '覆盖 TCP/IP、路由与交换、应用层协议的重点与易错点……' },
]);

const goLogin = () => router.push('/login');
const goPost = (id) => router.push(`/blog/${id}`);

const formatDate = (iso) => new Date(iso).toLocaleString('zh-CN', { hour12: false });

// 未登录提示并跳转到登录页
onMounted(() => {
  if (!user.value) {
    alert('请先登录后查看个人主页');
    router.push('/login');
  }
});

// 生成活跃度热力图数据（近12周，每周7天，模拟）
const heatmapData = ref([]);
function generateHeatmap() {
  const weeks = 12;
  const data = [];
  for (let w = 0; w < weeks; w++) {
    const week = [];
    for (let d = 0; d < 7; d++) {
      const count = Math.floor(Math.random() * 6); // 0-5篇
      const level = count === 0 ? 0 : Math.min(Math.ceil(count / 1.5), 4);
      const date = new Date();
      date.setDate(date.getDate() - (weeks - w) * 7 + d);
      week.push({ date: date.toLocaleDateString('zh-CN'), count, level });
    }
    data.push(week);
  }
  heatmapData.value = data;
}
generateHeatmap();
</script>

<style scoped>
.profile-page {
  background: var(--bg);
  min-height: 100vh;
}
.profile-container {
  max-width: 960px;
  margin: 0 auto;
  padding: 24px 20px 56px;
}
.notice {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #fff8e1;
  border: 1px solid #ffe0b2;
  color: #7a4b00;
  border-radius: var(--radius);
  padding: 12px 16px;
  margin-bottom: 20px;
}
.user-card {
  display: flex;
  gap: 16px;
  align-items: center;
}
.user-card .avatar {
  width: 88px;
  height: 88px;
  border-radius: 50%;
  box-shadow: var(--shadow-sm);
}
.user-meta .username { margin: 0; font-size: 24px; }
.user-meta .email { color: var(--text-muted); margin-top: 4px; }
.stats { display: flex; gap: 24px; margin-top: 10px; }
.stat { display: flex; align-items: baseline; gap: 6px; }
.stat .num { font-weight: 700; font-size: 18px; }
.stat .label { color: var(--text-muted); }

.posts { margin-top: 28px; }
.posts h2 { margin: 8px 0 12px; }
.post { padding: 14px 16px; margin-top: 12px; }
.post-header { display: flex; justify-content: space-between; align-items: baseline; gap: 12px; }
.post { cursor: pointer; }
.post-title { margin: 0; font-size: 18px; cursor: pointer; }
.post-date { color: var(--text-muted); font-size: 12px; }
.post-excerpt { color: #444; margin: 10px 0; }
.post-meta { color: #555; display: flex; gap: 12px; align-items: center; }

/* 活跃度热力图 */
.activity { margin-top: 28px; }
.activity h2 { margin: 0 0 16px; }
.heatmap { display: flex; gap: 4px; margin-bottom: 12px; overflow-x: auto; }
.heatmap-week { display: flex; flex-direction: column; gap: 4px; }
.heatmap-cell { width: 14px; height: 14px; border-radius: 3px; background: #ebedf0; transition: transform var(--transition-fast); }
.heatmap-cell:hover { transform: scale(1.15); outline: 1px solid rgba(0,0,0,0.2); }
.heatmap-cell.level-1 { background: #c6e48b; }
.heatmap-cell.level-2 { background: #7bc96f; }
.heatmap-cell.level-3 { background: #239a3b; }
.heatmap-cell.level-4 { background: #196127; }

.heatmap-legend { display: flex; align-items: center; gap: 6px; font-size: 12px; color: var(--text-muted); }
.legend-cell { width: 12px; height: 12px; border-radius: 2px; background: #ebedf0; }
.legend-cell.level-1 { background: #c6e48b; }
.legend-cell.level-2 { background: #7bc96f; }
.legend-cell.level-3 { background: #239a3b; }
.legend-cell.level-4 { background: #196127; }

@media (max-width: 640px) {
  .user-card { flex-direction: column; align-items: flex-start; }
}
</style>