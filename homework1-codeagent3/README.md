# 代码解释 Agent
## 项目简介
本项目基于 LangChain 实现一个简单的智能 Agent，具备工具调用能力。用户可以输入本地代码文件路径，Agent 将调用自定义文件读取工具加载代码，再通过大语言模型对代码进行解析、添加注释并说明功能；也可以直接粘贴代码文本进行分析。

## 环境依赖
- Python >=3.10
- langchain==0.2.16
- langchain-openai
- python-dotenv

安装命令：
pip install langchain==0.2.16 langchain-openai python-dotenv

## 配置说明
在 .env 文件中配置智谱大模型信息：
OPENAI_API_KEY=mykey
OPENAI_BASE_URL=https://open.bigmodel.cn/api/paas/v4

## 运行方式
1.打开终端，进入项目目录 week1
2.执行命令:python main.py
3.在控制台输入：
输入代码文件路径，例如 test_code.py，Agent 自动读取文件并解析代码
也可以直接粘贴代码文本进行分析
输入 exit 退出程序

## 核心原理
1.自定义工具 read_code_file：接收文件路径，读取本地文件内容，捕获文件不存在、读取异常等错误。
2.Agent 决策：判断用户输入是文件路径，自动调用文件读取工具获取代码。
3.LLM 分析：将读取到的代码送入大模型，输出代码功能说明、逐行解释、指出代码可优化点。
4.对话记忆：保留本次对话上下文，支持多轮交互。

## 测试示例
测试文件 test_code.py 是冒泡排序实现。输入 test_code.py，Agent 会读取代码，输出：
1.整体功能介绍
2.代码逐行讲解
3.代码缺陷与优化建议