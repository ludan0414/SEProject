<template>
  <div class="blog-container">
    <!-- 文章标题 -->
    <h1 class="blog-title">计算机系统导论笔记</h1>

    <!-- 作者信息 -->
    <div class="blog-author">
      <img src="https://i.pravatar.cc/48" alt="author avatar" />
      <div>
        <div>wenhao801</div>
        <div>发布于 2025年5月5日 08:45</div>
      </div>
    </div>

    <!-- 文章内容 -->
    <div class="blog-content">
      <p>
        本文主要总结了计算机系统的基本概念，包括处理器架构、内存层次结构、输入输出系统等内容。
      </p>
      <p>
        计算机系统是硬件与软件共同组成的复杂体系，它通过编译、链接、运行等阶段实现高级语言到机器执行的过程。
      </p>

      <h2>一、计算机系统层次结构</h2>
      <p>
        从上到下主要包括应用程序层、操作系统层、硬件抽象层、硬件层等。每一层通过接口与下层通信。
      </p>

      <h2>二、内存层次结构</h2>
      <p>
        现代计算机使用缓存（Cache）和虚拟内存机制提高访问效率，同时保证系统的可扩展性。
      </p>
    </div>

    <!-- 评论区 -->
    <div class="comment-section">
      <h2>评论区</h2>

      <!-- 输入框 -->
      <div class="comment-input">
        <textarea
          v-model="newComment"
          placeholder="写下你的评论..."
          rows="3"
        ></textarea>
        <button @click="addComment">发表评论</button>
      </div>

      <!-- 评论列表 -->
      <div
        v-for="(comment, index) in comments"
        :key="index"
        class="comment-item"
      >
        <div class="comment-user">
          <img :src="comment.avatar" />
          <span class="comment-user-name">{{ comment.user }}</span>
        </div>

        <div class="comment-text">{{ comment.text }}</div>

        <div class="comment-actions">
          <button @click="likeComment(index)">👍 {{ comment.likes }}</button>
          <button @click="toggleReply(index)">💬 回复</button>
        </div>

        <!-- 回复输入框 -->
        <div v-if="comment.showReplyBox" class="reply-box">
          <textarea
            v-model="comment.replyText"
            placeholder="回复..."
            rows="2"
          ></textarea>
          <button @click="submitReply(index)">回复</button>
        </div>

        <!-- 回复列表 -->
        <div v-if="comment.replies.length" class="reply-list">
          <div
            v-for="(reply, rIndex) in comment.replies"
            :key="rIndex"
            class="reply-item"
          >
            <span class="reply-user">{{ reply.user }}：</span>{{ reply.text }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
// 局部引入 blog.css
import "../assets/blog.css";

const newComment = ref("");
const comments = ref([
  {
    user: "Alice",
    avatar: "https://i.pravatar.cc/40?img=1",
    text: "写得很清楚，尤其是内存层次结构那部分！",
    likes: 2,
    replies: [],
    showReplyBox: false,
    replyText: "",
  },
  {
    user: "Bob",
    avatar: "https://i.pravatar.cc/40?img=2",
    text: "建议加上缓存一致性部分的讲解～",
    likes: 0,
    replies: [],
    showReplyBox: false,
    replyText: "",
  },
]);

const addComment = () => {
  if (!newComment.value.trim()) return;
  comments.value.push({
    user: "You",
    avatar: "https://i.pravatar.cc/40?img=3",
    text: newComment.value,
    likes: 0,
    replies: [],
    showReplyBox: false,
    replyText: "",
  });
  newComment.value = "";
};

const likeComment = (index) => {
  comments.value[index].likes++;
};

const toggleReply = (index) => {
  comments.value[index].showReplyBox = !comments.value[index].showReplyBox;
};

const submitReply = (index) => {
  const c = comments.value[index];
  if (!c.replyText.trim()) return;
  c.replies.push({ user: "You", text: c.replyText });
  c.replyText = "";
  c.showReplyBox = false;
};
</script>
