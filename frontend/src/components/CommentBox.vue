<template>
  <div class="comment-section">
    <input
      v-model="text"
      placeholder="发表你的评论..."
      class="comment-input"
    />
    <button @click="submitComment">发表评论</button>

    <div class="comment-list" v-if="note.comments.length">
      <div
        v-for="(c, i) in note.comments"
        :key="i"
        class="comment-item"
      >
        <strong>{{ c.user }}</strong>: {{ c.text }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
const props = defineProps({ note: Object });
const text = ref("");

const submitComment = () => {
  if (text.value.trim()) {
    props.note.comments.push({ user: "你", text: text.value });
    text.value = "";
  }
};
</script>

<style scoped>
.comment-section {
  margin-top: 10px;
}
.comment-input {
  width: 80%;
  padding: 5px;
  border: 1px solid #ddd;
  border-radius: 6px;
}
.comment-item {
  margin-top: 4px;
  font-size: 14px;
}
</style>
