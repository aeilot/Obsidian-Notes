# Obsidian Notes 笔记整理工具

本仓库包含一个自动整理 Obsidian 笔记的 Python 脚本，可以按知识点分类整理笔记，并自动生成 INDEX.md 索引文件。

## 功能特性

- 📂 **自动分类**：根据文件名和内容自动将笔记分类到相应的知识点文件夹
- 📝 **生成索引**：自动创建 Obsidian 风格的 INDEX.md 文件，包含所有笔记的链接
- 🔗 **保持链接**：使用 Obsidian 双链语法，确保链接的完整性
- 🎯 **智能识别**：针对不同学科（线性代数、数学分析等）使用不同的分类规则

## 使用方法

### 基本用法

```bash
# 整理所有中文目录
python3 organize_notes.py

# 整理指定目录
python3 organize_notes.py 线性代数

# 整理多个目录
python3 organize_notes.py 线性代数 数学分析

# 模拟运行（不实际移动文件，仅预览效果）
python3 organize_notes.py --dry-run
python3 organize_notes.py -n
```

### 分类规则

#### 线性代数
- `01-向量与向量空间`：向量空间、向量组等相关笔记
- `02-矩阵理论`：矩阵运算、可逆矩阵、分块矩阵等
- `03-线性方程组`：线性方程组的解法
- `04-线性空间`：四个基本子空间等
- `05-正交性`：正交性相关内容
- `06-行列式`：行列式的计算和性质
- `07-秩与相抵`：矩阵的秩和相抵标准型
- `08-方阵理论`：方阵的幂、多项式、迹等
- `09-特征值与递推`：特征值和递推式
- `课程笔记`：课程相关的笔记
- `辅助工具`：MATLAB、数学符号等工具

#### 数学分析
- `01-集合与实数系`：集合、实数、确界等基础概念
- `02-映射与函数`：映射、函数的概念与性质
- `03-数列极限`：数列极限、收敛准则
- `04-函数极限`：函数极限、无穷小量、重要极限
- `05-函数连续性`：连续性相关内容
- `06-导数与微分`：导数和微分
- `习题集`：各种习题
- `课程笔记`：课程相关笔记
- `辅助工具`：不等式、数学工具等

## 目录结构示例

整理后的目录结构：

```
线性代数/
├── INDEX.md                    # 自动生成的索引文件
├── 01-向量与向量空间/
│   ├── Ch01 向量和矩阵.md
│   ├── 向量空间.md
│   └── ...
├── 02-矩阵理论/
│   ├── 可逆矩阵.md
│   ├── 分块矩阵.md
│   └── ...
├── 06-行列式/
│   ├── Ch05 行列式.md
│   ├── 行列式的计算.md
│   └── ...
├── 课程笔记/
│   └── Course9.15 线性代数.md
└── PDFs/                       # 原有资源文件夹保留
    └── ...
```

## INDEX.md 示例

自动生成的 INDEX.md 文件包含：

- 📚 生成时间戳
- 📖 目录结构统计
- 🔗 按分类的笔记链接（使用 Obsidian 双链格式）
- 📁 其他资源文件夹列表
- 🏷️ 标签

```markdown
# 线性代数

> 📚 本索引自动生成于 2025-10-29 05:56:47

## 📖 目录结构

**总计**: 10 个分类，26 个笔记文件

### 01-向量与向量空间

- [[01-向量与向量空间/Ch01 向量和矩阵|Ch01 向量和矩阵]]
- [[01-向量与向量空间/向量空间|向量空间]]
...

## 📁 其他资源

- **PDFs/** (5 项)

---

*tags: #线性代数*
```

## 注意事项

1. **备份**：运行脚本前建议先备份你的笔记
2. **模拟运行**：第一次使用建议先用 `--dry-run` 选项查看效果
3. **链接更新**：脚本会移动文件，Obsidian 的内部链接会自动更新（如果使用相对路径链接）
4. **保留文件**：以下文件和文件夹不会被移动或修改：
   - `.obsidian` 目录
   - `PDFs` 目录
   - `EXT` 目录
   - `Exam` 目录
   - `.DS_Store` 文件
   - `.canvas` 文件
   - `TOC.base` 文件

## 自定义分类规则

如需为其他学科添加分类规则，可以编辑 `organize_notes.py` 文件中的分类规则部分。

## 环境要求

- Python 3.6+
- 标准库（无需额外依赖）

## Markdown 转 PDF 工具

本仓库还包含一个将 Markdown 文件转换为 PDF 的工具 `markdown_to_pdf.py`。

### 功能特性

- 📂 **自动收集**：递归或非递归扫描文件夹中的所有 Markdown 文件
- 📑 **智能拼接**：按文件名排序拼接所有 Markdown 文件
- 📄 **PDF 转换**：使用 pandoc 将拼接后的 Markdown 转换为 PDF
- 🎨 **中文支持**：自动检测并使用系统中可用的中文字体
- 🔧 **灵活配置**：支持自定义输出文件名、排除模式等

### 使用方法

#### 基本用法

```bash
# 转换文件夹为 PDF
python3 markdown_to_pdf.py 线性代数

# 指定输出文件名
python3 markdown_to_pdf.py 线性代数 -o linear_algebra.pdf

# 不递归处理子文件夹（只处理顶层文件）
python3 markdown_to_pdf.py 线性代数 --no-recursive

# 排除特定文件夹
python3 markdown_to_pdf.py 线性代数 --exclude .obsidian --exclude PDFs

# 保留临时的合并 Markdown 文件
python3 markdown_to_pdf.py 线性代数 -t
```

更多示例请参考 [`examples/convert_notes.sh`](examples/convert_notes.sh)。

#### 命令行选项

- `folder_path`: 要处理的文件夹路径（必需）
- `-o, --output`: 输出 PDF 文件名（默认：`<folder_name>.pdf`）
- `-r, --recursive`: 递归处理子文件夹（默认启用）
- `--no-recursive`: 不递归处理子文件夹
- `-t, --temp`: 保留临时的合并 Markdown 文件
- `--exclude PATTERN`: 排除匹配的文件/文件夹（可多次使用）
- `-h, --help`: 显示帮助信息

### 环境要求

- Python 3.6+
- pandoc（PDF 转换引擎）
- XeLaTeX 或 LuaLaTeX（用于中文支持）

#### 安装依赖

**Ubuntu/Debian:**
```bash
sudo apt-get install pandoc texlive-xetex texlive-fonts-recommended texlive-lang-chinese fonts-noto-cjk
```

**macOS:**
```bash
brew install pandoc basictex
```

**Windows:**
下载并安装 [pandoc](https://pandoc.org/installing.html) 和 [MiKTeX](https://miktex.org/)

### 工作原理

1. **收集文件**：扫描指定文件夹，按文件名排序收集所有 Markdown 文件
2. **拼接文件**：将所有 Markdown 文件拼接成一个临时文件，并添加文档标题和目录
3. **转换 PDF**：使用 pandoc 和 XeLaTeX 引擎将 Markdown 转换为 PDF
4. **清理临时文件**：转换完成后删除临时文件（除非使用 `-t` 选项）

### 注意事项

1. **中文字体**：脚本会自动检测系统中可用的中文字体（优先使用 Noto Sans CJK SC）
2. **排除模式**：默认排除 `.obsidian`、`.git`、`.DS_Store`、`PDFs`、`attachments` 等文件夹
3. **转换时间**：大文件夹的转换可能需要几分钟时间，请耐心等待
4. **标题调整**：原 Markdown 文件中的标题会自动增加一级（`#` 变为 `##`），以保持文档结构

## 许可证

本工具为开源工具，欢迎使用和改进。
