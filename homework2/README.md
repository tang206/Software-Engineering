# Simple Workflow MVP - Mini SE流程
## 环境安装
pip install -r requirements.txt
## 配置
在.env填入智谱OPENAI_API_KEY和BASE_URL
## 运行
python main.py
输入软件需求，自动顺序执行需求解析、模块设计、代码生成。

## 项目说明
3个Agent顺序协作，完成端到端软件工程简易流水线，实现Agent消息传递、状态共享。