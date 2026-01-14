# 更新日志

## [0.1.1] - 2024-01-14

### 🐛 问题修复

- 修复了PyPI上传问题
- 改进了包分发文件

## [0.1.0] - 2024-01-14

### 🎉 初始发布

ctxtoolkit是一个用于优化AI上下文管理的实用工具包，帮助解决长上下文中的内容丢失、令牌不足、信息冗余和上下文污染等问题。

### ✨ 核心功能

#### 1. 上下文构建器（Context Builder）
- 关键信息优先级优化
- 智能场景背景整合
- 结构化内容分层
- 支持添加核心指令和要求
- 支持关键信息管理
- 支持补充参考内容

#### 2. 令牌节省器（Token Saver）
- 自动重复内容合并
- 术语压缩
- 内容摘要生成
- 支持术语管理
- 支持构建紧凑上下文

#### 3. 防污染系统（Anti-Pollution System）
- 错误信息隔离
- 术语一致性检查
- 清晰的任务边界定义
- 支持内容验证标记
- 支持上下文重置

#### 4. 工具协调器（Tool Coordinator）
- 工具边界定义
- 动态调用约束
- 多工具协作工作流
- 支持工具注册和可用性管理
- 支持工作流定义和执行

### 🛠️ 技术特性

- **类型安全**：完整的类型注释支持
- **无外部依赖**：轻量级设计，不需要额外依赖
- **英文友好**：支持英文文档和错误信息
- **易于扩展**：模块化设计，易于扩展功能
- **测试覆盖**：全面的单元测试确保功能可靠性

### 📖 文档

- 完整的API文档
- 详细的使用示例
- 项目结构说明

### 📦 安装

```bash
pip install ctxtoolkit
```

### 🚀 使用示例

```python
# 示例1：使用ContextBuilder构建结构化上下文
from ctxtoolkit import ContextBuilder

builder = ContextBuilder()
builder.add_core_instruction("优化Python代码性能", requirements=["减少内存使用", "提高执行速度"])
builder.add_key_info("当前瓶颈", "嵌套循环导致O(n²)复杂度")
context = builder.build()

# 示例2：使用TokenSaver减少上下文令牌消耗
from ctxtoolkit import TokenSaver

saver = TokenSaver()
saver.add_terminology("R1", "输入格式：JSON对象")
saver.add_terminology("R2", "输出格式：Markdown表格")
compact_context = saver.build_compact_context("处理数据", rules=["R1", "R2"])
```

### 📄 许可证

MIT许可证