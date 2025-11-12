const fs = require('fs');
const path = require('path');
const postcss = require('postcss');
const prefixSelector = require('postcss-prefix-selector');
const postcssImport = require('postcss-import');

const inputFile = path.resolve(__dirname, 'vue.css');
const outputFile = path.resolve(__dirname, 'vue-scoped.css');
const css = fs.readFileSync(inputFile, 'utf-8');

postcss([
  postcssImport(), // 处理 @import
  prefixSelector({
    prefix: '.markdown-body',
    transform(prefix, selector, prefixedSelector) {
      if (/^(html|body|:root)/.test(selector)) return prefix;
      return prefixedSelector;
    }
  })
])
.process(css, { from: inputFile, to: outputFile })
.then(result => {
  fs.writeFileSync(outputFile, result.css);
  console.log(`✅ 转换完成: ${outputFile}`);
})
.catch(err => {
  console.error('❌ 转换失败:', err);
});
