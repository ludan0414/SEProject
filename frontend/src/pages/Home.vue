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
import NoteCard from "../components/NoteCard.vue";
import UserSidebar from "../components/UserSidebar.vue";

const notes = [
  {
    author: "wenhao801",
    date: "05/05 08:45",
    title: "计算机系统导论笔记",
    content:
      "涵盖计算机科学基础概念、算法、数据结构、计算理论等核心知识点，附有丰富实例和习题。",
    views: 1324,
    favorites: 1234,
    likes: 1234,
    comments: [],
  },
  {
    author: "wenhao802",
    date: "05/05 08:45",
    title: "另一个什么笔记",
    content:
      "涵盖计算机科学基础概念、算法、数据结构、计算理论等核心知识点，附有丰富实例和习题。",
    views: 1324,
    favorites: 1234,
    likes: 1234,
    comments: [],
  },
];
</script>
