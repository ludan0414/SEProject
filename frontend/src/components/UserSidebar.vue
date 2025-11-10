<template>
  <div class="card user-card">
    <img src="/src/assets/avatar.jpg" class="avatar" />
    <h4>{{ user.name }}</h4>
    <p>发布 {{ user.posts }} · 关注 {{ user.following }} · 粉丝 {{ user.followers }}</p>

    <div class="recent">
      <h5>最近笔记</h5>
      <ul>
        <li v-for="(r, i) in user.recentNotes" :key="i">
          🔧 {{ r.title }} · 👁 {{ r.views }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
const user = {
  name: "1080ahnew",
  posts: 123,
  following: 456,
  followers: 789,
  recentNotes: [
    { title: "这个笔记教你如何拆弹", views: 123456 },
    { title: "更适合北大宝宝体质的", views: 123456 },
    { title: "CW-EX-8 摆完挂机简", views: 123456 },
  ],
};
</script>

<style scoped>
.avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  margin-bottom: 10px;
}
.user-card {
  text-align: center;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  font-size: 14px;
  text-align: left;
  margin-bottom: 4px;
}
</style>
