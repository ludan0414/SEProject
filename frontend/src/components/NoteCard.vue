<template>
  <div class="card">
    <div class="note-header">
      <div class="author">{{ note.author }}</div>
      <div class="date">{{ note.date }}</div>
    </div>
    <h3>{{ note.title }}</h3>
    <p>{{ note.content }}</p>

    <div class="icon-row">
      <span @click="note.views++">👁 {{ note.views }}</span>
      <span @click="toggleComment">💬 {{ note.comments.length }}</span>
      <span @click="toggleFavorite">⭐ {{ note.favorites }}</span>
      <span @click="like">👍 {{ note.likes }}</span>
    </div>

    <CommentBox v-if="showComment" :note="note" />
  </div>
</template>

<script setup>
import { ref } from "vue";
import CommentBox from "./CommentBox.vue";

const props = defineProps({ note: Object });
const showComment = ref(false);

const toggleComment = () => (showComment.value = !showComment.value);
const like = () => props.note.likes++;
const toggleFavorite = () => props.note.favorites++;
</script>

<style scoped>
.note-header {
  display: flex;
  justify-content: space-between;
  font-size: 13px;
  color: #888;
}
h3 {
  margin: 8px 0;
  color: #0057ff;
  cursor: pointer;
}
</style>
