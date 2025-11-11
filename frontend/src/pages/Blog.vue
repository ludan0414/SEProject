<template>
   <div class="blog-container" v-if="blog">
    <!-- 文章标题 -->
    <h1 class="blog-title">{{ blog.title }}</h1>

    <!-- 作者信息 -->
    <div class="blog-author">
      <img src="https://i.pravatar.cc/48" alt="author avatar" />
      <div>
        <div>{{ blog.author.username }}</div>
        <div>发布于 {{ formatDate(blog.created_at) }}</div>
      </div>
    </div>

    <!-- 文章内容 -->
    <div class="blog-content markdown-body" ref="contentContainer" v-html="htmlContent"></div>

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

  <!-- 加载状态 -->
  <div v-else class="loading">加载中...</div>
</template>

<script setup>
import { ref, onMounted, nextTick } from "vue";
import { useRoute } from "vue-router";
import { renderMarkdown } from '../utils/markdown'
import '../assets/typora-vue-theme/vue-scoped.css' // ✅ Markdown 样式

import axios from "axios";
import "../assets/blog.css";

const route = useRoute();
const blog = ref(null);
const htmlContent = ref('');
const newComment = ref("");
const contentContainer = ref(null);

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

// 获取博客详情
const fetchBlog = async () => {
  const id = route.params.id;
  try {
    const res = await axios.get(`http://localhost:5000/api/blogs/${id}`);
    blog.value = res.data;
    console.log(blog.value.content);
    htmlContent.value = renderMarkdown(blog.value.content);

    await nextTick();
    addCopyButtons();
    console.log(contentContainer.value);
    renderMathInElement(contentContainer.value);
  } catch (err) {
    console.error("获取博客详情失败:", err);
  }
};

// 格式化时间
const formatDate = (isoString) => {
  const d = new Date(isoString);
  return d.toLocaleString("zh-CN", { hour12: false });
};

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

function addCopyButtons() {
  const pres = document.querySelectorAll('pre.hljs')
  pres.forEach(pre => {
    // 避免重复添加
    if (pre.querySelector('.code-copy-btn')) return;

    const btn = document.createElement('button');
    btn.className = 'code-copy-btn';
    btn.textContent = 'Copy';

    // 点击事件
    btn.addEventListener('click', () => {
      const code = pre.querySelector('code').innerText
      navigator.clipboard.writeText(code).then(() => {
        btn.textContent = 'Copied!';
        setTimeout(() => { btn.textContent = 'Copy' }, 1200);
      })
    })

    pre.prepend(btn)
  })
}

function renderMathInElement(container) {
  if(window.MathJax) {
    window.MathJax.typesetPromise([container])
  }
}

onMounted(fetchBlog);
</script>
