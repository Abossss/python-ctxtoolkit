# API Documentation

## 语言选择 / Language Selection

- [English](#english-api-documentation)
- [中文](#中文-api-文档)

---

## English API Documentation


## 1. ContextBuilder

### Description
Used to build structured, hierarchical contexts, ensuring that key information is processed with priority.

### Main Methods

#### `__init__()`
Create a context builder instance.

#### `add_core_instruction(task: str, requirements: list = None)`
Add core instruction and requirements.

**Parameters:**
- `task`: Core task instruction (string)
- `requirements`: List of task requirements (optional)

**Exceptions:**
- `TypeError`: When task is not a string or requirements is not a list
- `ValueError`: When task is an empty string

#### `add_key_info(key: str, value: str)`
Add key information.

**Parameters:**
- `key`: Information key (string)
- `value`: Information value (string)

**Exceptions:**
- `TypeError`: When key or value is not a string
- `ValueError`: When key is an empty string

#### `add_reference(content: str, title: str = None)`
Add supplementary reference content.

**Parameters:**
- `content`: Reference content (string)
- `title`: Reference title (optional, string)

**Exceptions:**
- `TypeError`: When content is not a string or title is not a string
- `ValueError`: When content is an empty string

#### `build() -> str`
Generate structured context.

**Return Value:**
- Structured context string

#### `clear()`
Clear all added content.

### Usage Example
```python
from ctxtoolkit import ContextBuilder

builder = ContextBuilder()

builder.add_core_instruction(
    "Analyze sales data and generate report",
    requirements=[
        "Include 2023 full-year data",
        "Analyze by quarter",
        "Generate visual charts"
    ]
)

builder.add_key_info("Data Source", "CSV file exported from CRM system")
builder.add_key_info("Data Volume", "100,000 sales records")

sales_data = """Date,Product,Sales Amount,Quantity
2023-01-01,Product A,10000,50
2023-01-02,Product B,15000,30
...
"""
builder.add_reference(sales_data, title="Sales Data Sample")

context = builder.build()
print(context)
```

## 2. TokenSaver

### Description
Used to reduce Token consumption in contexts through terminology compression, duplicate content merging, and summary generation.

### Main Methods

#### `__init__()`
Create a Token saver instance.

#### `add_terminology(key: str, definition: str)`
Add a single terminology definition.

**Parameters:**
- `key`: Terminology abbreviation/number (string)
- `definition`: Complete terminology definition (string)

**Exceptions:**
- `TypeError`: When key or definition is not a string
- `ValueError`: When key is an empty string

#### `add_terminologies(terms: dict)`
Add multiple terminology definitions.

**Parameters:**
- `terms`: Dictionary of terms, where key is the abbreviation/number and value is the complete definition

**Exceptions:**
- `TypeError`: When terms is not a dictionary
- `ValueError`: When terms contains invalid keys

#### `build_compact_context(instruction: str, data: list = None, rules: list = None) -> str`
Build compact context.

**Parameters:**
- `instruction`: Core instruction (string)
- `data`: List of related data (optional)
- `rules`: List of rules to follow (optional)

**Return Value:**
- Compact context string

**Exceptions:**
- `TypeError`: When instruction is not a string or data/rules is not a list
- `ValueError`: When instruction is an empty string or rules contains undefined rules

#### `merge_duplicates(content: str) -> str`
Merge duplicate content.

**Parameters:**
- `content`: Original content (string)

**Return Value:**
- Content with duplicates merged

**Exceptions:**
- `TypeError`: When content is not a string

#### `compress_terms(content: str) -> str`
Compress content using terminology table.

**Parameters:**
- `content`: Original content (string)

**Return Value:**
- Compressed content string

**Exceptions:**
- `TypeError`: When content is not a string

#### `generate_summary(content: str, max_length: int = 100, method: str = "keyphrase") -> str`
Generate content summary.

**Parameters:**
- `content`: Original content (string)
- `max_length`: Maximum summary length (default 100)
- `method`: Summary method ("keyphrase" or "first_sentences", default "keyphrase")

**Return Value:**
- Generated summary string

**Exceptions:**
- `TypeError`: When content is not a string or max_length is not an integer
- `ValueError`: When max_length is less than or equal to 0 or method is not supported

#### `clear_terminology()`
Clear the terminology table.

### Usage Example
```python
from ctxtoolkit import TokenSaver

saver = TokenSaver()

# Add terminologies
saver.add_terminologies({
    "R1": "User ID format: 8-digit number",
    "R2": "Order status: pending, paid, shipped, completed, cancelled",
    "R3": "Payment methods: WeChat Pay, Alipay, credit card"
})

# Build compact context
context = saver.build_compact_context(
    "Analyze user order data",
    data=[
        "User ID:12345678,Order ID:ORD20230001,Amount:100.00,Status:paid",
        "User ID:87654321,Order ID:ORD20230002,Amount:200.00,Status:shipped"
    ],
    rules=["R1", "R2"]
)

# Merge duplicate content
duplicate_content = """This is duplicate content.
This is duplicate content.
This is another content.
"""
merged = saver.merge_duplicates(duplicate_content)

# Generate summary
long_content = """This is a very long content used to demonstrate the summary generation function..."""
summary = saver.generate_summary(long_content, max_length=50)

print("Compact context:", context)
print("Merged content:", merged)
print("Summary:", summary)
```

## 3. AntiPollutionSystem

### Description
Used to prevent context pollution and ensure the consistency and accuracy of information.

### Main Methods

#### `__init__()`
Create an anti-pollution system instance.

#### `create_task_boundary(task_name: str, content: str) -> str`
Create task boundary.

**Parameters:**
- `task_name`: Task name (string)
- `content`: Task content (string)

**Return Value:**
- Task content string with boundaries

**Exceptions:**
- `TypeError`: When task_name or content is not a string
- `ValueError`: When task_name is an empty string

#### `mark_unverified(content: str) -> str`
Mark content as unverified.

**Parameters:**
- `content`: Content to mark (string)

**Return Value:**
- Marked content string

**Exceptions:**
- `TypeError`: When content is not a string

#### `mark_verified(content: str) -> str`
Mark content as verified.

**Parameters:**
- `content`: Content to mark (string)

**Return Value:**
- Marked content string

**Exceptions:**
- `TypeError`: When content is not a string

#### `reset_context(new_instruction: str) -> str`
Reset context.

**Parameters:**
- `new_instruction`: New instruction (string)

**Return Value:**
- Reset context string

**Exceptions:**
- `TypeError`: When new_instruction is not a string
- `ValueError`: When new_instruction is an empty string

#### `check_consistency(context1: str, context2: str) -> dict`
Check consistency between two contexts.

**Parameters:**
- `context1`: First context (string)
- `context2`: Second context (string)

**Return Value:**
- Dictionary containing consistency analysis results

**Exceptions:**
- `TypeError`: When context1 or context2 is not a string

#### `isolate_error(error_content: str, main_content: str) -> str`
Isolate error content.

**Parameters:**
- `error_content`: Error content (string)
- `main_content`: Main content (string)

**Return Value:**
- Isolated content string

**Exceptions:**
- `TypeError`: When error_content or main_content is not a string

### Usage Example
```python
from ctxtoolkit import AntiPollutionSystem

system = AntiPollutionSystem()

# Create task boundary
task_content = "Process user data and generate report"
boundary_content = system.create_task_boundary("Data Analysis Task", task_content)

# Mark content
verified_content = system.mark_verified("Verified correct information")
unverified_content = system.mark_unverified("Information that needs further verification")

# Check context consistency
context1 = "Process user data, follow rules R1, R2"
context2 = "Process user data, follow rules R1, R3"
consistency = system.check_consistency(context1, context2)

# Isolate error content
main_content = "This is the main content"
error_content = "This is error content"
isolated = system.isolate_error(error_content, main_content)

print("Task boundary:", boundary_content)
print("Verified marker:", verified_content)
print("Unverified marker:", unverified_content)
print("Consistency check:", consistency)
print("Error isolation:", isolated)
```

## 4. ToolCoordinator

### Description
Used to manage the collaboration of multiple tools, defining tool boundaries and call constraints.

### Main Methods

#### `__init__()`
Create a tool coordinator instance.

#### `register_tool(tool_name: str, description: str, capabilities: list)`
Register a tool.

**Parameters:**
- `tool_name`: Tool name (string)
- `description`: Tool description (string)
- `capabilities`: List of tool capabilities (list of strings)

**Exceptions:**
- `TypeError`: When tool_name or description is not a string, or capabilities is not a list
- `ValueError`: When tool_name is an empty string

#### `set_tool_availability(tool_name: str, is_available: bool)`
Set tool availability.

**Parameters:**
- `tool_name`: Tool name (string)
- `is_available`: Whether the tool is available (boolean)

**Exceptions:**
- `TypeError`: When tool_name is not a string or is_available is not a boolean
- `ValueError`: When tool_name is an empty string or the tool does not exist

#### `add_call_constraint(tool_name: str, constraint: callable)`
Add tool call constraint.

**Parameters:**
- `tool_name`: Tool name (string)
- `constraint`: Constraint function that returns True if callable, False otherwise

**Exceptions:**
- `TypeError`: When tool_name is not a string or constraint is not callable
- `ValueError`: When tool_name is an empty string or the tool does not exist

#### `can_call_tool(tool_name: str, context: dict = None) -> bool`
Check if the tool can be called.

**Parameters:**
- `tool_name`: Tool name (string)
- `context`: Context information (optional, dictionary)

**Return Value:**
- Whether the tool can be called (boolean)

**Exceptions:**
- `TypeError`: When tool_name is not a string or context is not a dictionary
- `ValueError`: When tool_name is an empty string

#### `define_workflow(workflow_name: str, steps: list)`
Define a workflow.

**Parameters:**
- `workflow_name`: Workflow name (string)
- `steps`: List of workflow steps, each step contains tool_name and parameters

**Exceptions:**
- `TypeError`: When workflow_name is not a string or steps is not a list
- `ValueError`: When workflow_name is an empty string or steps are missing necessary fields

#### `execute_workflow(workflow_name: str, context: dict = None) -> dict`
Execute a workflow.

**Parameters:**
- `workflow_name`: Workflow name (string)
- `context`: Context information (optional, dictionary)

**Return Value:**
- Execution result dictionary, containing success, results, total_steps, etc.

**Exceptions:**
- `TypeError`: When workflow_name is not a string or context is not a dictionary
- `ValueError`: When workflow_name is an empty string

#### `get_tool_info(tool_name: str) -> dict`
Get tool information.

**Parameters:**
- `tool_name`: Tool name (string)

**Return Value:**
- Tool information dictionary

**Exceptions:**
- `TypeError`: When tool_name is not a string
- `ValueError`: When tool_name is an empty string

#### `list_available_tools() -> list`
List available tools.

**Return Value:**
- List of available tool names

### Usage Example
```python
from ctxtoolkit import ToolCoordinator

coordinator = ToolCoordinator()

# Register tools
coordinator.register_tool(
    "Search Tool",
    "Tool for searching information",
    ["Web search", "Document search", "Keyword extraction"]
)

coordinator.register_tool(
    "Analysis Tool",
    "Tool for analyzing data",
    ["Statistical analysis", "Trend prediction", "Visualization generation"]
)

# Set call constraints
def search_constraint(context):
    return "search_keyword" in context

coordinator.add_call_constraint("Search Tool", search_constraint)

# Define workflow
workflow_steps = [
    {
        "tool_name": "Search Tool",
        "parameters": {"keyword": "Python performance optimization", "type": "document"}
    },
    {
        "tool_name": "Analysis Tool",
        "parameters": {"data": "$step_1_result"}
    }
]

coordinator.define_workflow("Search Analysis Workflow", workflow_steps)

# Execute workflow
execution_result = coordinator.execute_workflow(
    "Search Analysis Workflow",
    context={"search_keyword": "Python performance optimization"}
)

print("Execution result:", execution_result)
print("Available tools:", coordinator.list_available_tools())

---

## 中文 API 文档

### 1. ContextBuilder - 上下文构建器

#### 功能
用于构建结构化、层次分明的上下文，确保关键信息被优先处理。

#### 主要方法

##### `__init__()`
创建上下文构建器实例。

##### `add_core_instruction(task: str, requirements: list = None)`
添加核心指令和要求。

**参数：**
- `task`: 核心任务指令（字符串）
- `requirements`: 任务要求列表（可选）

**异常：**
- `TypeError`: 当task不是字符串或requirements不是列表时
- `ValueError`: 当task为空字符串时

##### `add_key_info(key: str, value: str)`
添加关键信息。

**参数：**
- `key`: 信息键（字符串）
- `value`: 信息值（字符串）

**异常：**
- `TypeError`: 当key或value不是字符串时
- `ValueError`: 当key为空字符串时

##### `add_reference(content: str, title: str = None)`
添加补充参考内容。

**参数：**
- `content`: 参考内容（字符串）
- `title`: 参考标题（可选，字符串）

**异常：**
- `TypeError`: 当content不是字符串或title不是字符串时
- `ValueError`: 当content为空字符串时

##### `build() -> str`
生成结构化上下文。

**返回值：**
- 结构化的上下文字符串

##### `clear()`
清空所有已添加的内容。

#### 使用示例
```python
from ctxtoolkit import ContextBuilder

builder = ContextBuilder()

builder.add_core_instruction(
    "分析销售数据并生成报告",
    requirements=[
        "包含2023年全年数据",
        "按季度分析",
        "生成可视化图表"
    ]
)

builder.add_key_info("数据来源", "CRM系统导出的CSV文件")
builder.add_key_info("数据量", "10万条销售记录")

sales_data = """日期,产品,销售额,数量
2023-01-01,A产品,10000,50
2023-01-02,B产品,15000,30
...
"""
builder.add_reference(sales_data, title="销售数据样本")

context = builder.build()
print(context)
```

### 2. TokenSaver - Token节省工具

#### 功能
用于减少上下文的Token消耗，通过术语压缩、重复内容合并和摘要生成等方式。

#### 主要方法

##### `__init__()`
创建Token节省器实例。

##### `add_terminology(key: str, definition: str)`
添加单个术语定义。

**参数：**
- `key`: 术语缩写（字符串）
- `definition`: 术语完整定义（字符串）

**异常：**
- `TypeError`: 当key或definition不是字符串时
- `ValueError`: 当key为空字符串时

##### `add_terminologies(terms: dict)`
批量添加术语定义。

**参数：**
- `terms`: 术语字典，键为术语缩写，值为术语完整定义

**异常：**
- `TypeError`: 当terms不是字典或字典中的值不是字符串时
- `ValueError`: 当字典中包含空键时

##### `build_compact_context(instruction: str, data: list = None, rules: list = None) -> str`
构建精简上下文。

**参数：**
- `instruction`: 核心指令（字符串）
- `data`: 相关数据列表（可选）
- `rules`: 遵循的规则列表（可选）

**返回值：**
- 精简的上下文字符串

**异常：**
- `TypeError`: 当instruction不是字符串或data/rules不是列表时
- `ValueError`: 当instruction为空字符串或rules中包含未定义的规则时

##### `merge_duplicates(content: str) -> str`
合并重复内容。

**参数：**
- `content`: 原始内容（字符串）

**返回值：**
- 合并后的内容字符串

**异常：**
- `TypeError`: 当content不是字符串时

##### `compress_terms(content: str) -> str`
使用术语表压缩内容。

**参数：**
- `content`: 原始内容（字符串）

**返回值：**
- 压缩后的内容字符串

**异常：**
- `TypeError`: 当content不是字符串时

##### `generate_summary(content: str, max_length: int = 100, method: str = "keyphrase") -> str`
生成内容摘要。

**参数：**
- `content`: 原始内容（字符串）
- `max_length`: 摘要最大长度（默认100）
- `method`: 摘要方法（"keyphrase"或"first_sentences"，默认"keyphrase"）

**返回值：**
- 生成的摘要字符串

**异常：**
- `TypeError`: 当content不是字符串或max_length不是整数时
- `ValueError`: 当max_length小于等于0或method不是支持的方法时

##### `clear_terminology()`
清空术语表。

#### 使用示例
```python
from ctxtoolkit import TokenSaver

saver = TokenSaver()

# 添加术语
saver.add_terminologies({
    "R1": "用户ID格式：8位数字",
    "R2": "订单状态：待支付、已支付、已发货、已完成、已取消",
    "R3": "支付方式：微信支付、支付宝、信用卡"
})

# 构建精简上下文
context = saver.build_compact_context(
    "分析用户订单数据",
    data=[
        "用户ID:12345678,订单号:ORD20230001,金额:100.00,状态:已支付",
        "用户ID:87654321,订单号:ORD20230002,金额:200.00,状态:已发货"
    ],
    rules=["R1", "R2"]
)

# 合并重复内容
duplicate_content = """这是一段重复内容。
这是一段重复内容。
这是另一段内容。
"""
merged = saver.merge_duplicates(duplicate_content)

# 生成摘要
long_content = """这是一段很长的内容，用于演示摘要生成功能..."""
summary = saver.generate_summary(long_content, max_length=50)

print("精简上下文:", context)
print("合并后内容:", merged)
print("摘要:", summary)
```

### 3. AntiPollutionSystem - 上下文防污染系统

#### 功能
用于防止上下文污染，确保信息的一致性和准确性。

#### 主要方法

##### `__init__()`
创建防污染系统实例。

##### `create_task_boundary(task_name: str, content: str) -> str`
创建任务边界。

**参数：**
- `task_name`: 任务名称（字符串）
- `content`: 任务内容（字符串）

**返回值：**
- 带有边界的任务内容字符串

**异常：**
- `TypeError`: 当task_name或content不是字符串时
- `ValueError`: 当task_name为空字符串时

##### `mark_unverified(content: str) -> str`
标记待验证内容。

**参数：**
- `content`: 待标记内容（字符串）

**返回值：**
- 标记后的内容字符串

**异常：**
- `TypeError`: 当content不是字符串时

##### `mark_verified(content: str) -> str`
标记已验证内容。

**参数：**
- `content`: 待标记内容（字符串）

**返回值：**
- 标记后的内容字符串

**异常：**
- `TypeError`: 当content不是字符串时

##### `reset_context(new_instruction: str) -> str`
重置上下文。

**参数：**
- `new_instruction`: 新的指令（字符串）

**返回值：**
- 重置后的上下文字符串

**异常：**
- `TypeError`: 当new_instruction不是字符串时
- `ValueError`: 当new_instruction为空字符串时

##### `check_consistency(context1: str, context2: str) -> dict`
检查两个上下文之间的一致性。

**参数：**
- `context1`: 第一个上下文（字符串）
- `context2`: 第二个上下文（字符串）

**返回值：**
- 包含一致性分析结果的字典

**异常：**
- `TypeError`: 当context1或context2不是字符串时

##### `isolate_error(error_content: str, main_content: str) -> str`
隔离错误内容。

**参数：**
- `error_content`: 错误内容（字符串）
- `main_content`: 主要内容（字符串）

**返回值：**
- 隔离后的内容字符串

**异常：**
- `TypeError`: 当error_content或main_content不是字符串时

#### 使用示例
```python
from ctxtoolkit import AntiPollutionSystem

system = AntiPollutionSystem()

# 创建任务边界
task_content = "处理用户数据并生成报告"
boundary_content = system.create_task_boundary("数据分析任务", task_content)

# 标记内容
verified_content = system.mark_verified("已验证的正确信息")
unverified_content = system.mark_unverified("需要进一步验证的信息")

# 检查上下文一致性
context1 = "处理用户数据，遵循规则R1、R2"
context2 = "处理用户数据，遵循规则R1、R3"
consistency = system.check_consistency(context1, context2)

# 隔离错误内容
main_content = "这是主要内容"
error_content = "这是错误内容"
isolated = system.isolate_error(error_content, main_content)

print("任务边界:", boundary_content)
print("验证标记:", verified_content)
print("待验证标记:", unverified_content)
print("一致性检查:", consistency)
print("错误隔离:", isolated)
```

### 4. ToolCoordinator - 工具协同管理器

#### 功能
用于管理多个工具的协同工作，定义工具边界和调用约束。

#### 主要方法

##### `__init__()`
创建工具协同管理器实例。

##### `register_tool(tool_name: str, description: str, capabilities: list)`
注册工具。

**参数：**
- `tool_name`: 工具名称（字符串）
- `description`: 工具描述（字符串）
- `capabilities`: 工具能力列表（字符串列表）

**异常：**
- `TypeError`: 当tool_name、description不是字符串或capabilities不是列表时
- `ValueError`: 当tool_name为空字符串时

##### `set_tool_availability(tool_name: str, is_available: bool)`
设置工具可用性。

**参数：**
- `tool_name`: 工具名称（字符串）
- `is_available`: 是否可用（布尔值）

**异常：**
- `TypeError`: 当tool_name不是字符串或is_available不是布尔值时
- `ValueError`: 当tool_name为空字符串或工具不存在时

##### `add_call_constraint(tool_name: str, constraint: callable)`
添加工具调用约束。

**参数：**
- `tool_name`: 工具名称（字符串）
- `constraint`: 约束函数，返回True表示可以调用，False表示不能调用

**异常：**
- `TypeError`: 当tool_name不是字符串或constraint不是可调用对象时
- `ValueError`: 当tool_name为空字符串或工具不存在时

##### `can_call_tool(tool_name: str, context: dict = None) -> bool`
检查是否可以调用工具。

**参数：**
- `tool_name`: 工具名称（字符串）
- `context`: 上下文信息（可选，字典）

**返回值：**
- 是否可以调用工具（布尔值）

**异常：**
- `TypeError`: 当tool_name不是字符串或context不是字典时
- `ValueError`: 当tool_name为空字符串时

##### `define_workflow(workflow_name: str, steps: list)`
定义工作流。

**参数：**
- `workflow_name`: 工作流名称（字符串）
- `steps`: 工作流步骤列表，每个步骤包含tool_name和parameters

**异常：**
- `TypeError`: 当workflow_name不是字符串或steps不是列表时
- `ValueError`: 当workflow_name为空字符串或步骤中缺少必要字段时

##### `execute_workflow(workflow_name: str, context: dict = None) -> dict`
执行工作流。

**参数：**
- `workflow_name`: 工作流名称（字符串）
- `context`: 上下文信息（可选，字典）

**返回值：**
- 执行结果字典，包含success、results、total_steps等字段

**异常：**
- `TypeError`: 当workflow_name不是字符串或context不是字典时
- `ValueError`: 当workflow_name为空字符串时

##### `get_tool_info(tool_name: str) -> dict`
获取工具信息。

**参数：**
- `tool_name`: 工具名称（字符串）

**返回值：**
- 工具信息字典

**异常：**
- `TypeError`: 当tool_name不是字符串时
- `ValueError`: 当tool_name为空字符串时

##### `list_available_tools() -> list`
列出可用工具。

**返回值：**
- 可用工具名称列表

#### 使用示例
```python
from ctxtoolkit import ToolCoordinator

coordinator = ToolCoordinator()

# 注册工具
coordinator.register_tool(
    "搜索工具",
    "用于搜索信息的工具",
    ["网络搜索", "文档搜索", "关键词提取"]
)

coordinator.register_tool(
    "分析工具",
    "用于分析数据的工具",
    ["统计分析", "趋势预测", "可视化生成"]
)

# 设置调用约束
def search_constraint(context):
    return "搜索关键词" in context

coordinator.add_call_constraint("搜索工具", search_constraint)

# 定义工作流
workflow_steps = [
    {
        "tool_name": "搜索工具",
        "parameters": {"关键词": "Python性能优化", "类型": "文档"}
    },
    {
        "tool_name": "分析工具",
        "parameters": {"数据": "$step_1_result"}
    }
]

coordinator.define_workflow("搜索分析工作流", workflow_steps)

# 执行工作流
execution_result = coordinator.execute_workflow(
    "搜索分析工作流",
    context={"搜索关键词": "Python性能优化"}
)

print("执行结果:", execution_result)
print("可用工具:", coordinator.list_available_tools())
```
