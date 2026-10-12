# Simple Workflow MVP 设计文档
## 项目简介
本项目实现Mini SE软件流程工作流，由需求Agent、设计Agent、编码Agent顺序协作，完成从自然语言需求到代码生成的端到端流程。

## 工作流流程
用户输入需求 → RequirementAgent（解析结构化需求）→ DesignAgent（模块设计）→ CodeAgent（生成代码）
采用顺序执行，上一个Agent输出作为下一个Agent输入，全局state保存流程状态，实现Agent消息传递。

## Agent职责
1. RequirementAgent：接收原始自然语言，整理结构化需求文档
2. DesignAgent：读取需求文档，完成软件模块划分与接口设计
3. CodeAgent：读取设计文档，生成可运行代码

## 状态管理
使用全局state字典保存每一步输出，字段包含stage当前阶段、content当前阶段结果，实现Agent间数据共享。

## 可扩展性
新增Agent只需要新建Agent类，加入agents列表即可；调整流程顺序只需要修改agents数组顺序，不需要改动调度核心。

## 技术栈
Python + LangChain + 智谱GLM LLM