<template>
  <div class="container">
    <div class="main-content">
      <NoteCard v-for="(n, i) in notes" :key="i" :note="n" />
    </div>
    <div class="sidebar">
      <UserSidebar />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import NoteCard from "../components/NoteCard.vue";
import UserSidebar from "../components/UserSidebar.vue";

const notes = ref([]);

const fetchNotes = async () => {
  try {
    const res = await axios.get("http://localhost:5000/api/blogs");
    notes.value = res.data.blogs.map(b => ({
      id: b.id,
      author: b.author,
      date: new Date(b.created_at).toLocaleString(),
      title: b.title,
      content: b.summary,
      views: Math.floor(Math.random() * 2000), // 临时字段，后端未提供
      favorites: Math.floor(Math.random() * 500),
      likes: Math.floor(Math.random() * 500),
      comments: []
    }));
  } catch (err) {
    console.error("获取博客失败:", err);
  }
};

// 组件加载时调用
onMounted(fetchNotes);
</script>
