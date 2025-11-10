# Markdown 转 PDF 工具使用说明

## 简介

`markdown_to_pdf.py` 是一个将 Markdown 笔记文件夹转换为 PDF 文档的工具。它可以自动收集文件夹中的所有 Markdown 文件，按顺序拼接后转换为格式美观的 PDF 文档。

## 功能特性

- ✅ **递归扫描**：支持递归或非递归方式扫描文件夹
- ✅ **智能拼接**：按文件名自动排序拼接
- ✅ **中文支持**：自动检测并使用系统中文字体
- ✅ **目录生成**：自动生成可导航的目录
- ✅ **灵活配置**：支持排除特定文件/文件夹
- ✅ **格式美观**：包含标题页、页码、章节编号等

## 快速开始

### 1. 安装依赖

```bash
# Ubuntu/Debian
sudo apt-get install pandoc texlive-xetex texlive-fonts-recommended texlive-lang-chinese fonts-noto-cjk

# macOS
brew install pandoc basictex
```

### 2. 基本使用

```bash
# 转换整个文件夹
python3 markdown_to_pdf.py 线性代数

# 指定输出文件名
python3 markdown_to_pdf.py 线性代数 -o 我的线性代数笔记.pdf
```

### 3. 高级用法

```bash
# 只转换顶层文件（不递归）
python3 markdown_to_pdf.py 线性代数 --no-recursive

# 排除特定文件夹
python3 markdown_to_pdf.py 线性代数 --exclude PDFs --exclude Exam

# 保留中间文件用于调试
python3 markdown_to_pdf.py 线性代数 -t
```

## 命令行参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `folder` | 要处理的文件夹路径（必需） | - |
| `-o, --output` | 输出 PDF 文件名 | `<文件夹名>.pdf` |
| `-r, --recursive` | 递归处理子文件夹 | `true` |
| `--no-recursive` | 不递归处理子文件夹 | - |
| `-t, --temp` | 保留临时合并的 Markdown 文件 | `false` |
| `--exclude` | 排除匹配的文件/文件夹（可多次使用） | - |
| `-h, --help` | 显示帮助信息 | - |

## 默认排除的文件/文件夹

以下文件和文件夹会被自动排除：
- `.obsidian` - Obsidian 配置文件夹
- `.git` - Git 版本控制文件夹
- `.DS_Store` - macOS 系统文件
- `PDFs` - PDF 资源文件夹
- `attachments` - 附件文件夹

## 输出格式

生成的 PDF 文档包含以下部分：

1. **标题页**
   - 文档标题（文件夹名称）
   - 生成日期
   - 文件统计信息

2. **目录**
   - 自动生成，最多 3 级深度
   - 可点击跳转

3. **正文内容**
   - 每个 Markdown 文件占独立章节
   - 自动添加页眉和页码
   - 章节自动编号

## 常见问题

### Q: 为什么提示找不到 pandoc？

A: 需要先安装 pandoc 和相关的 LaTeX 工具。请参考"安装依赖"部分。

### Q: 中文显示乱码怎么办？

A: 脚本会自动检测系统中文字体。如果遇到问题，请确保安装了中文字体包（如 `fonts-noto-cjk`）。

### Q: 转换大文件夹很慢怎么办？

A: LaTeX 编译确实需要一些时间。对于大文件夹，建议：
- 使用 `--exclude` 排除不需要的文件夹
- 使用 `--no-recursive` 只处理顶层文件
- 将大文件夹拆分成多个小文件夹分别转换

### Q: 可以自定义 PDF 样式吗？

A: 当前版本使用默认样式。如需自定义，可以：
- 保留临时文件（`-t` 选项）
- 手动编辑 `.combined.md` 文件
- 使用 pandoc 的其他参数进行转换

## 示例

更多使用示例请参考 [`examples/convert_notes.sh`](convert_notes.sh)。

## 技术细节

- **语言**: Python 3.6+
- **转换引擎**: Pandoc with XeLaTeX/LuaLaTeX
- **字体检测**: fontconfig (fc-list)
- **输出格式**: PDF 1.5

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

本工具为开源工具，遵循 MIT 许可证。
