import MarkdownIt from 'markdown-it'
import hljs from 'highlight.js'
import 'highlight.js/styles/github-dark.css'  // 可换主题


// 创建 MarkdownIt 实例
const md = new MarkdownIt({
  html: true,
  linkify: true,
  typographer: true,
  highlight: (str, lang) => {
    let highlighted
    if (lang && hljs.getLanguage(lang)) {
      highlighted = hljs.highlight(str, { language: lang }).value
    } else {
      highlighted = hljs.highlightAuto(str).value
    }

    // 为每行添加行号
    const lines = highlighted.split(/\r?\n/).map((line, index) => {
      return `<span class="line" data-line="${index + 1}">${line}</span>`
    }).join('\n')

    return `<pre class="hljs"><code>${lines}</code></pre>`
  }
})

export function renderMarkdown(content) {
  return md.render(content || '')
}
