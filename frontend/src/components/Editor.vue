<template>
  <mavon-editor v-model="content" />
</template>

<script setup>
import { ref } from 'vue'

const content = ref('# 写点什么吧 ✨')
</script>
