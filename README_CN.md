<div align="center">
    <br>
    <!-- Logo placeholder - replace with actual logo URL later -->
    <img src="https://objectstorageapi.bja.sealos.run/73p2bjxj-images/ctxtoolkit.png" width="400" alt="上下文工程工具包 Logo"/>
    <br>
</div>

<div align="center">

## 上下文工程工具包 (ctxtoolkit)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![PyPI version](https://badge.fury.io/py/ctxtoolkit.svg)](https://badge.fury.io/py/ctxtoolkit) 
[![GitHub issues](https://img.shields.io/github/issues-pr/Abossss/python-ctxtoolkit.svg)](https://GitHub.com/Abossss/python-ctxtoolkit/pull/) [![GitHub last commit](https://badgen.net/github/last-commit/Abossss/python-ctxtoolkit)](https://GitHub.com/Abossss/python-ctxtoolkit/commit/)

</div>

<div align="center">

<a href="README.md">English</a> | 简体中文

</div>

一个用于优化AI上下文管理的实用工具包，帮助解决长上下文丢内容、Token不够用、信息冗余、上下文污染等问题。

## 核心功能

### 精准上下文投喂器
- 关键信息前置优化
- 场景背景智能植入
- 结构化内容分层

### Token节省工具
- 重复内容自动合并
- 术语精简压缩
- 内容摘要生成

### 上下文防污染系统
- 错误信息隔离
- 前后术语一致性检查
- 任务边界清晰划分

### 工具协同管理器
- 工具边界定义
- 动态调用约束
- 多工具配合流程

## 📦 安装

```bash
pip install ctxtoolkit
```

## 🚀 快速开始

### 1. 精准上下文投喂

```python
from ctxtoolkit import ContextBuilder

# 创建上下文构建器
builder = ContextBuilder()

# 添加核心指令
builder.add_core_instruction(
    "优化这段Python代码的性能",
    requirements=[
        "减少内存占用",
        "提升执行速度",
        "保持原有功能不变"
    ]
)

# 添加关键信息
builder.add_key_info(
    "代码功能", "处理100万条用户日志"
)
builder.add_key_info(
    "当前瓶颈", "循环嵌套导致O(n²)复杂度"
)
builder.add_key_info(
    "可用资源", "8GB内存，4核CPU"
)

# 添加补充参考
current_code = """
def process_logs(logs):
    results = []
    for i in range(len(logs)):
        for j in range(i+1, len(logs)):
            if logs[i]['user_id'] == logs[j]['user_id']:
                results.append((logs[i], logs[j]))
    return results
"""
builder.add_reference(current_code)

# 生成优化后的上下文
optimized_context = builder.build()
print(optimized_context)
```

### 2. Token节省示例

```python
from ctxtoolkit import TokenSaver

# 创建Token节省器
saver = TokenSaver()

# 定义术语表
saver.add_terminology("R1", "输入格式：JSON对象，包含name(str)、age(int)、tags(list[str])")
saver.add_terminology("R2", "输出格式：Markdown表格，包含用户信息和标签统计")
saver.add_terminology("R3", "处理规则：过滤age>18，按tags数量降序排序")

# 处理用户数据
user_data = [
    '{"name":"张三","age":25,"tags":["Python","AI"]}',
    '{"name":"李四","age":17,"tags":["Java"]}'
]

# 生成精简上下文
compact_context = saver.build_compact_context(
    "请处理以下用户数据",
    data=user_data,
    rules=["R1", "R2", "R3"]
)
print(compact_context)
```

## 📁 项目结构

```
ctxtoolkit/
├── ctxtoolkit/               # 核心包目录
│   ├── __init__.py          # 包初始化文件
│   ├── context_builder.py   # 上下文构建器
│   ├── token_saver.py       # Token节省工具
│   ├── anti_pollution.py    # 防污染系统
│   └── tool_coordinator.py  # 工具协同管理器
├── LICENSE
├── MANIFEST.in
├── README.md
└── setup.py
```

## 📚 API 文档

API文档已迁移至 [API_DOCUMENTATION.md](API_DOCUMENTATION.md)。

## 🔧 开发

### 安装开发依赖

```bash
pip install -e .[dev]
```

### 运行测试

```bash
pytest
```

### 代码风格检查

```bash
flake8
```

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📄 许可证

[MIT License](LICENSE)