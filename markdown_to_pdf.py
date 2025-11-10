#!/usr/bin/env python3
"""
Markdown to PDF Converter
将指定文件夹内的 Markdown 文件拼接并转换为 PDF

功能:
1. 递归扫描指定文件夹中的所有 Markdown 文件
2. 按文件名排序后拼接为单个 Markdown 文件
3. 使用 pandoc 将拼接后的 Markdown 转换为 PDF

使用方法:
    python3 markdown_to_pdf.py <folder_path> [options]
    
    参数:
        folder_path         要处理的文件夹路径
    
    选项:
        -o, --output       输出 PDF 文件名 (默认: <folder_name>.pdf)
        -r, --recursive    递归处理子文件夹 (默认: 是)
        --no-recursive     不递归处理子文件夹
        -t, --temp         保留临时的合并 Markdown 文件
        --exclude PATTERN  排除匹配的文件/文件夹 (可多次使用)
        -h, --help         显示帮助信息

示例:
    # 转换 "线性代数" 文件夹
    python3 markdown_to_pdf.py 线性代数
    
    # 指定输出文件名
    python3 markdown_to_pdf.py 线性代数 -o linear_algebra.pdf
    
    # 不递归处理子文件夹
    python3 markdown_to_pdf.py 线性代数 --no-recursive
    
    # 排除某些文件夹
    python3 markdown_to_pdf.py 线性代数 --exclude .obsidian --exclude PDFs
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path
from typing import List, Set
from datetime import datetime
import argparse


class MarkdownToPDFConverter:
    """Markdown 到 PDF 转换器"""
    
    def __init__(self):
        # 默认排除的文件和文件夹
        self.default_excludes = {
            '.obsidian',
            '.git',
            '.DS_Store',
            'PDFs',
            'attachments',
        }
    
    def check_pandoc(self) -> bool:
        """检查 pandoc 是否已安装"""
        return shutil.which('pandoc') is not None
    
    def collect_markdown_files(
        self,
        folder_path: Path,
        recursive: bool = True,
        exclude_patterns: Set[str] = None
    ) -> List[Path]:
        """
        收集文件夹中的所有 Markdown 文件
        
        Args:
            folder_path: 文件夹路径
            recursive: 是否递归处理子文件夹
            exclude_patterns: 要排除的文件/文件夹模式
        
        Returns:
            排序后的 Markdown 文件路径列表
        """
        if exclude_patterns is None:
            exclude_patterns = self.default_excludes
        else:
            exclude_patterns = self.default_excludes | exclude_patterns
        
        markdown_files = []
        
        if recursive:
            # 递归遍历
            for root, dirs, files in os.walk(folder_path):
                # 过滤掉排除的文件夹
                dirs[:] = [d for d in dirs if not any(
                    pattern in d for pattern in exclude_patterns
                )]
                
                # 收集 .md 文件
                for file in files:
                    if file.endswith('.md') and not any(
                        pattern in file for pattern in exclude_patterns
                    ):
                        markdown_files.append(Path(root) / file)
        else:
            # 仅处理顶层文件夹
            for file in folder_path.glob('*.md'):
                if not any(pattern in file.name for pattern in exclude_patterns):
                    markdown_files.append(file)
        
        # 按文件路径排序
        markdown_files.sort()
        
        return markdown_files
    
    def concatenate_markdown_files(
        self,
        markdown_files: List[Path],
        output_path: Path,
        base_folder: Path
    ) -> None:
        """
        拼接多个 Markdown 文件
        
        Args:
            markdown_files: Markdown 文件列表
            output_path: 输出文件路径
            base_folder: 基础文件夹路径（用于生成相对路径）
        """
        with open(output_path, 'w', encoding='utf-8') as outfile:
            # 写入文档标题和元信息
            folder_name = base_folder.name
            outfile.write(f"---\n")
            outfile.write(f"title: {folder_name}\n")
            outfile.write(f"date: {datetime.now().strftime('%Y-%m-%d')}\n")
            outfile.write(f"---\n\n")
            outfile.write(f"# {folder_name}\n\n")
            outfile.write(f"> 本文档由 {len(markdown_files)} 个 Markdown 文件合并生成\n")
            outfile.write(f"> 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            # 写入目录
            outfile.write("\\newpage\n\n")
            outfile.write("## 目录\n\n")
            for i, md_file in enumerate(markdown_files, 1):
                relative_path = md_file.relative_to(base_folder)
                display_name = md_file.stem
                outfile.write(f"{i}. {relative_path}\n")
            outfile.write("\n")
            
            # 拼接所有 Markdown 文件
            for i, md_file in enumerate(markdown_files, 1):
                relative_path = md_file.relative_to(base_folder)
                
                # 添加分页符（除了第一个文件）
                if i > 1:
                    outfile.write("\n\\newpage\n\n")
                
                # 写入文件标题
                outfile.write(f"---\n\n")
                outfile.write(f"# 📄 {relative_path}\n\n")
                
                # 读取并写入文件内容
                try:
                    with open(md_file, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        
                        # 调整标题级别（将原文件的 # 转换为 ##）
                        lines = content.split('\n')
                        adjusted_lines = []
                        for line in lines:
                            if line.startswith('#'):
                                # 增加一级标题深度
                                adjusted_lines.append('#' + line)
                            else:
                                adjusted_lines.append(line)
                        
                        outfile.write('\n'.join(adjusted_lines))
                        outfile.write('\n\n')
                
                except Exception as e:
                    print(f"⚠️  读取文件失败 {md_file}: {e}")
                    outfile.write(f"*无法读取文件: {e}*\n\n")
        
        print(f"✓ 已拼接 {len(markdown_files)} 个文件到: {output_path}")
    
    def detect_chinese_font(self) -> str:
        """
        检测系统可用的中文字体
        
        Returns:
            字体名称
        """
        # 尝试的字体列表（按优先级）
        font_list = [
            'Noto Sans CJK SC',
            'Noto Serif CJK SC',
            'WenQuanYi Micro Hei',
            'AR PL UMing CN',
            'SimSun',
            'STSong',
        ]
        
        try:
            # 使用 fc-list 检查字体
            result = subprocess.run(
                ['fc-list', ':lang=zh'],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            available_fonts = result.stdout
            
            for font in font_list:
                if font in available_fonts:
                    return font
        except:
            pass
        
        # 如果检测失败，返回默认字体
        return 'Noto Sans CJK SC'
    
    def convert_to_pdf(
        self,
        markdown_path: Path,
        pdf_path: Path,
        engine: str = 'xelatex'
    ) -> bool:
        """
        使用 pandoc 将 Markdown 转换为 PDF
        
        Args:
            markdown_path: Markdown 文件路径
            pdf_path: 输出 PDF 文件路径
            engine: LaTeX 引擎 (pdflatex, xelatex, lualatex)
        
        Returns:
            转换是否成功
        """
        try:
            # 检测中文字体
            chinese_font = self.detect_chinese_font()
            
            # pandoc 命令
            cmd = [
                'pandoc',
                str(markdown_path),
                '-o', str(pdf_path),
                '--pdf-engine', engine,
                '-V', 'geometry:margin=1in',
                '-V', 'fontsize=12pt',
                '--toc',  # 生成目录
                '--toc-depth=3',  # 目录深度
                '--number-sections',  # 章节编号
            ]
            
            # 只有 xelatex 和 lualatex 支持 CJK 字体
            if engine in ['xelatex', 'lualatex']:
                cmd.extend([
                    '-V', f'CJKmainfont={chinese_font}',
                ])
            
            print(f"🔄 正在转换为 PDF...")
            print(f"   引擎: {engine}")
            print(f"   中文字体: {chinese_font}")
            print(f"   命令: {' '.join(cmd)}")
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300  # 5分钟超时
            )
            
            if result.returncode == 0:
                print(f"✓ PDF 生成成功: {pdf_path}")
                print(f"  文件大小: {pdf_path.stat().st_size / 1024:.2f} KB")
                return True
            else:
                print(f"✗ PDF 生成失败:")
                if result.stdout:
                    print(f"  标准输出: {result.stdout}")
                if result.stderr:
                    print(f"  错误输出: {result.stderr[:500]}")  # 限制错误输出长度
                
                # 尝试使用其他引擎
                if engine == 'xelatex':
                    print("\n尝试使用 lualatex 引擎...")
                    return self.convert_to_pdf(markdown_path, pdf_path, 'lualatex')
                
                return False
        
        except subprocess.TimeoutExpired:
            print(f"✗ PDF 转换超时（超过 5 分钟）")
            return False
        except Exception as e:
            print(f"✗ PDF 转换出错: {e}")
            return False
    
    def convert_folder(
        self,
        folder_path: str,
        output_pdf: str = None,
        recursive: bool = True,
        keep_temp: bool = False,
        exclude_patterns: Set[str] = None
    ) -> bool:
        """
        转换文件夹中的 Markdown 文件为 PDF
        
        Args:
            folder_path: 文件夹路径
            output_pdf: 输出 PDF 文件名
            recursive: 是否递归处理子文件夹
            keep_temp: 是否保留临时 Markdown 文件
            exclude_patterns: 要排除的文件/文件夹模式
        
        Returns:
            转换是否成功
        """
        folder = Path(folder_path)
        
        if not folder.exists():
            print(f"✗ 文件夹不存在: {folder_path}")
            return False
        
        if not folder.is_dir():
            print(f"✗ 路径不是文件夹: {folder_path}")
            return False
        
        # 检查 pandoc
        if not self.check_pandoc():
            print("✗ 未找到 pandoc，请先安装 pandoc")
            print("  安装方法:")
            print("    - Ubuntu/Debian: sudo apt-get install pandoc texlive-xetex")
            print("    - macOS: brew install pandoc basictex")
            print("    - Windows: 下载并安装 https://pandoc.org/installing.html")
            return False
        
        print(f"{'='*60}")
        print(f"📂 处理文件夹: {folder.name}")
        print(f"{'='*60}\n")
        
        # 收集 Markdown 文件
        print("🔍 正在收集 Markdown 文件...")
        markdown_files = self.collect_markdown_files(folder, recursive, exclude_patterns)
        
        if not markdown_files:
            print("⚠️  未找到 Markdown 文件")
            return False
        
        print(f"✓ 找到 {len(markdown_files)} 个 Markdown 文件\n")
        
        # 确定输出文件名
        if output_pdf is None:
            output_pdf = f"{folder.name}.pdf"
        
        if not output_pdf.endswith('.pdf'):
            output_pdf += '.pdf'
        
        pdf_path = Path(output_pdf)
        temp_md_path = pdf_path.with_suffix('.combined.md')
        
        # 拼接 Markdown 文件
        print("📝 正在拼接 Markdown 文件...")
        self.concatenate_markdown_files(markdown_files, temp_md_path, folder)
        print()
        
        # 转换为 PDF
        success = self.convert_to_pdf(temp_md_path, pdf_path)
        
        # 清理临时文件
        if not keep_temp and temp_md_path.exists():
            temp_md_path.unlink()
            print(f"✓ 已删除临时文件: {temp_md_path}")
        elif keep_temp:
            print(f"✓ 保留临时文件: {temp_md_path}")
        
        print(f"\n{'='*60}")
        if success:
            print(f"✅ 转换完成!")
            print(f"   输出文件: {pdf_path.absolute()}")
        else:
            print(f"❌ 转换失败")
        print(f"{'='*60}")
        
        return success


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='将文件夹内的 Markdown 文件拼接并转换为 PDF',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s 线性代数
  %(prog)s 线性代数 -o linear_algebra.pdf
  %(prog)s 线性代数 --no-recursive
  %(prog)s 线性代数 --exclude .obsidian --exclude PDFs
        """
    )
    
    parser.add_argument(
        'folder',
        help='要处理的文件夹路径'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='输出 PDF 文件名 (默认: <folder_name>.pdf)'
    )
    
    parser.add_argument(
        '-r', '--recursive',
        action='store_true',
        default=True,
        help='递归处理子文件夹 (默认)'
    )
    
    parser.add_argument(
        '--no-recursive',
        action='store_true',
        help='不递归处理子文件夹'
    )
    
    parser.add_argument(
        '-t', '--temp',
        action='store_true',
        help='保留临时的合并 Markdown 文件'
    )
    
    parser.add_argument(
        '--exclude',
        action='append',
        default=[],
        help='排除匹配的文件/文件夹 (可多次使用)'
    )
    
    args = parser.parse_args()
    
    # 处理递归选项
    recursive = not args.no_recursive if args.no_recursive else args.recursive
    
    # 转换排除模式为集合
    exclude_patterns = set(args.exclude) if args.exclude else None
    
    # 创建转换器并执行转换
    converter = MarkdownToPDFConverter()
    success = converter.convert_folder(
        args.folder,
        args.output,
        recursive,
        args.temp,
        exclude_patterns
    )
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
