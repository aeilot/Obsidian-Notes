#!/usr/bin/env python3
"""
Obsidian Notes Organizer
自动整理 Obsidian 笔记，创建 INDEX.md 和子文件夹结构

功能:
1. 扫描指定目录中的 Markdown 文件
2. 根据文件名自动分类到子文件夹
3. 生成 Obsidian 风格的 INDEX.md 索引文件
4. 保持文件链接的完整性

使用方法:
    python3 organize_notes.py [目录名称]
    
    如果不指定目录，将处理所有中文命名的目录
"""

import os
import re
import shutil
from pathlib import Path
from typing import Dict, List, Tuple
from datetime import datetime


class ObsidianNotesOrganizer:
    """Obsidian 笔记组织器"""
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        
        # 按照知识点分类的规则 - 线性代数
        self.linear_algebra_rules = [
            # 向量与向量空间
            (r'向量空间|向量组', '01-向量与向量空间', 'Vectors and Vector Spaces'),
            (r'Ch01|向量和矩阵', '01-向量与向量空间', 'Vectors and Vector Spaces'),
            # 矩阵
            (r'矩阵|可逆矩阵|分块矩阵', '02-矩阵理论', 'Matrix Theory'),
            (r'Ch02|线性方程组|消元法', '03-线性方程组', 'Linear Equations'),
            (r'Ch03|子空间', '04-线性空间', 'Linear Spaces'),
            (r'Ch04|正交', '05-正交性', 'Orthogonality'),
            # 行列式
            (r'行列式|Ch05', '06-行列式', 'Determinants'),
            # 秩相关
            (r'秩|相抵', '07-秩与相抵', 'Rank and Equivalence'),
            # 方阵相关
            (r'方阵', '08-方阵理论', 'Square Matrix Theory'),
            # 特征值与递推
            (r'特征|递推', '09-特征值与递推', 'Eigenvalues and Recurrence'),
            # 课程笔记
            (r'^Course\d+\.\d+', '课程笔记', 'Course Notes'),
            # 工具与其他
            (r'MATLAB|数域|求和符号', '辅助工具', 'Auxiliary Tools'),
        ]
        
        # 按照知识点分类的规则 - 数学分析
        self.math_analysis_rules = [
            # 集合与实数
            (r'集合|实数|确界|连续统|有理数', '01-集合与实数系', 'Sets and Real Numbers'),
            # 映射与函数
            (r'映射|函数的概念|函数的性质|函数的运算|对合函数|反三角函数', '02-映射与函数', 'Mappings and Functions'),
            # 数列极限
            (r'数列极限|收敛准则|康托尔', '03-数列极限', 'Sequence Limits'),
            # 函数极限
            (r'函数极限|重要极限|无穷小量|无穷大量', '04-函数极限', 'Function Limits'),
            # 连续性
            (r'连续性|闭区间上的连续函数', '05-函数连续性', 'Continuity'),
            # 导数与微分
            (r'导数|微分', '06-导数与微分', 'Derivatives and Differentials'),
            # 不等式与其他工具
            (r'不等式|双阶乘|区间的条件', '辅助工具', 'Auxiliary Tools'),
            # 课程笔记 (不含习题)
            (r'^Course9\.15 关于', '课程笔记', 'Course Notes'),
            # 习题按知识点分
            (r'习题.*集族|证明题', '01-集合与实数系', 'Sets and Real Numbers'),
            (r'习题.*补充', '习题集', 'Exercise Collection'),
        ]
        
        # C++程序设计规则
        self.cpp_rules = [
            (r'.*', '基础知识', 'Fundamentals'),
        ]
        
        # 不应该移动的文件和文件夹
        self.exclude_patterns = [
            'INDEX.md',
            '.obsidian',
            'PDFs',
            'EXT',
            'Exam',
            '.DS_Store',
            'TOC.base',
            '.canvas',
        ]
    
    def should_exclude(self, name: str) -> bool:
        """检查文件或文件夹是否应该被排除"""
        for pattern in self.exclude_patterns:
            if pattern in name:
                return True
        return False
    
    def get_rules_for_directory(self, directory_name: str) -> List[Tuple[str, str, str]]:
        """根据目录名称获取对应的分类规则"""
        if '线性代数' in directory_name:
            return self.linear_algebra_rules
        elif '数学分析' in directory_name:
            return self.math_analysis_rules
        elif 'C++' in directory_name:
            return self.cpp_rules
        else:
            # 默认规则
            return [
                (r'^Ch\d+', '章节笔记', 'Chapter Notes'),
                (r'^Course', '课程笔记', 'Course Notes'),
                (r'.*', '笔记', 'Notes'),
            ]
    
    def categorize_file(self, filename: str, directory_name: str) -> Tuple[str, str]:
        """
        根据文件名对文件进行分类
        返回: (文件夹名称, 文件夹描述)
        """
        basename = os.path.splitext(filename)[0]
        
        # 获取当前目录的分类规则
        rules = self.get_rules_for_directory(directory_name)
        
        for pattern, folder_name, description in rules:
            if re.search(pattern, basename):
                return folder_name, description
        
        # 默认分类
        return '其他', 'Others'
    
    def scan_directory(self, directory: Path) -> Dict[str, List[str]]:
        """
        扫描目录中的 Markdown 文件并分类
        返回: {分类文件夹: [文件列表]}
        """
        categorized_files = {}
        
        if not directory.exists():
            print(f"⚠️  目录不存在: {directory}")
            return categorized_files
        
        # 扫描所有 .md 文件
        for file_path in directory.glob('*.md'):
            if self.should_exclude(file_path.name):
                continue
            
            folder_name, _ = self.categorize_file(file_path.name, directory.name)
            
            if folder_name not in categorized_files:
                categorized_files[folder_name] = []
            
            categorized_files[folder_name].append(file_path.name)
        
        # 对每个分类中的文件进行排序
        for folder in categorized_files:
            categorized_files[folder].sort()
        
        return categorized_files
    
    def create_subfolders(self, directory: Path, categories: Dict[str, List[str]]) -> None:
        """创建子文件夹"""
        for folder_name in categories.keys():
            folder_path = directory / folder_name
            if not folder_path.exists():
                folder_path.mkdir(parents=True, exist_ok=True)
                print(f"✓ 创建文件夹: {folder_path.relative_to(self.base_path)}")
    
    def move_files(self, directory: Path, categories: Dict[str, List[str]], dry_run: bool = False) -> None:
        """将文件移动到对应的子文件夹"""
        for folder_name, files in categories.items():
            folder_path = directory / folder_name
            
            for filename in files:
                src = directory / filename
                dst = folder_path / filename
                
                if src.exists() and src != dst:
                    if dry_run:
                        print(f"  [模拟] 移动: {filename} -> {folder_name}/")
                    else:
                        try:
                            shutil.move(str(src), str(dst))
                            print(f"  ✓ 移动: {filename} -> {folder_name}/")
                        except Exception as e:
                            print(f"  ✗ 移动失败 {filename}: {e}")
    
    def generate_index(self, directory: Path, categories: Dict[str, List[str]]) -> str:
        """生成 Obsidian 风格的 INDEX.md 内容"""
        dir_name = directory.name
        
        # 生成索引内容
        lines = [
            f"# {dir_name}",
            "",
            f"> 📚 本索引自动生成于 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "## 📖 目录结构",
            ""
        ]
        
        # 统计信息
        total_files = sum(len(files) for files in categories.values())
        lines.append(f"**总计**: {len(categories)} 个分类，{total_files} 个笔记文件")
        lines.append("")
        
        # 按分类生成链接
        for folder_name, files in sorted(categories.items()):
            lines.append(f"### {folder_name}")
            lines.append("")
            
            for filename in files:
                # Obsidian 风格链接: [[folder/filename|显示名称]]
                display_name = os.path.splitext(filename)[0]
                link = f"[[{folder_name}/{display_name}|{display_name}]]"
                lines.append(f"- {link}")
            
            lines.append("")
        
        # 添加其他已存在的文件夹链接
        lines.append("## 📁 其他资源")
        lines.append("")
        
        existing_folders = []
        for item in directory.iterdir():
            if item.is_dir() and not self.should_exclude(item.name) and item.name not in categories:
                existing_folders.append(item.name)
        
        if existing_folders:
            for folder in sorted(existing_folders):
                # 检查文件夹中是否有文件
                folder_path = directory / folder
                files_count = len(list(folder_path.glob('*')))
                if files_count > 0:
                    lines.append(f"- **{folder}/** ({files_count} 项)")
                else:
                    lines.append(f"- **{folder}/**")
        else:
            lines.append("*暂无其他资源*")
        
        lines.append("")
        
        # 添加标签
        lines.append("---")
        lines.append("")
        lines.append(f"*tags: #{dir_name}*")
        
        return "\n".join(lines)
    
    def create_index_file(self, directory: Path, categories: Dict[str, List[str]], dry_run: bool = False) -> None:
        """创建 INDEX.md 文件"""
        index_path = directory / "INDEX.md"
        content = self.generate_index(directory, categories)
        
        if dry_run:
            print(f"\n[模拟] 将创建 INDEX.md:")
            print("=" * 60)
            print(content)
            print("=" * 60)
        else:
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"\n✓ 创建索引文件: {index_path.relative_to(self.base_path)}")
    
    def organize_directory(self, directory: Path, dry_run: bool = False) -> None:
        """组织单个目录"""
        print(f"\n{'='*60}")
        print(f"📂 处理目录: {directory.name}")
        print(f"{'='*60}")
        
        # 扫描并分类文件
        categories = self.scan_directory(directory)
        
        if not categories:
            print("⚠️  未找到需要组织的 Markdown 文件")
            return
        
        print(f"\n发现 {sum(len(files) for files in categories.values())} 个文件，分为 {len(categories)} 类:")
        for folder_name, files in sorted(categories.items()):
            print(f"  • {folder_name}: {len(files)} 个文件")
        
        # 创建子文件夹
        if not dry_run:
            self.create_subfolders(directory, categories)
        
        # 移动文件
        print(f"\n{'移动文件' if not dry_run else '模拟移动文件'}:")
        self.move_files(directory, categories, dry_run)
        
        # 生成索引
        self.create_index_file(directory, categories, dry_run)
        
        print(f"\n✅ 目录 {directory.name} 组织完成!")
    
    def find_chinese_directories(self) -> List[Path]:
        """查找所有包含中文字符的目录"""
        chinese_dirs = []
        
        for item in self.base_path.iterdir():
            if not item.is_dir():
                continue
            
            if self.should_exclude(item.name):
                continue
            
            # 检查是否包含中文字符
            if re.search(r'[\u4e00-\u9fff]', item.name):
                chinese_dirs.append(item)
        
        return sorted(chinese_dirs)
    
    def organize_all(self, dry_run: bool = False) -> None:
        """组织所有中文目录"""
        chinese_dirs = self.find_chinese_directories()
        
        if not chinese_dirs:
            print("未找到包含中文名称的目录")
            return
        
        print(f"找到 {len(chinese_dirs)} 个中文目录:")
        for d in chinese_dirs:
            print(f"  • {d.name}")
        
        for directory in chinese_dirs:
            self.organize_directory(directory, dry_run)


def main():
    """主函数"""
    import sys
    
    # 获取脚本所在目录作为基础路径
    base_path = Path(__file__).parent
    
    organizer = ObsidianNotesOrganizer(base_path)
    
    # 解析命令行参数
    dry_run = '--dry-run' in sys.argv or '-n' in sys.argv
    
    if dry_run:
        print("🔍 运行模式: 模拟运行 (不会实际修改文件)")
        print("   要执行实际操作，请移除 --dry-run 或 -n 参数\n")
    
    # 过滤掉选项参数
    args = [arg for arg in sys.argv[1:] if not arg.startswith('-')]
    
    if len(args) > 0:
        # 处理指定的目录
        for dir_name in args:
            directory = base_path / dir_name
            if directory.exists() and directory.is_dir():
                organizer.organize_directory(directory, dry_run)
            else:
                print(f"⚠️  目录不存在或不是目录: {dir_name}")
    else:
        # 处理所有中文目录
        organizer.organize_all(dry_run)


if __name__ == '__main__':
    main()
