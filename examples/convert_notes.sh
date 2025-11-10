#!/bin/bash
# 示例脚本：批量转换笔记文件夹为 PDF
# Example script: Batch convert note folders to PDF

# 转换单个文件夹
# Convert a single folder
echo "Converting 线性代数..."
python3 ../markdown_to_pdf.py "../线性代数" -o "线性代数_完整笔记.pdf"

# 转换特定子文件夹
# Convert specific subfolder
echo "Converting 线性代数/01-向量与向量空间..."
python3 ../markdown_to_pdf.py "../线性代数/01-向量与向量空间" -o "向量与向量空间.pdf"

# 不递归处理子文件夹（仅处理顶层文件）
# Non-recursive mode (only top-level files)
echo "Converting top-level files only..."
python3 ../markdown_to_pdf.py "../线性代数" --no-recursive -o "线性代数_顶层笔记.pdf"

# 排除特定文件夹
# Exclude specific folders
echo "Converting with exclusions..."
python3 ../markdown_to_pdf.py "../线性代数" \
    --exclude .obsidian \
    --exclude PDFs \
    --exclude Exam \
    -o "线性代数_核心内容.pdf"

# 保留临时合并的 Markdown 文件用于调试
# Keep temporary combined markdown for debugging
echo "Converting and keeping temp file..."
python3 ../markdown_to_pdf.py "../线性代数/01-向量与向量空间" \
    -t \
    -o "向量空间_debug.pdf"

echo "Done!"
