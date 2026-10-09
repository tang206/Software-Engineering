from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory

load_dotenv()

# 1. 定义工具：读取本地代码文件（满足作业至少一个工具的硬性要求）
@tool
def read_code_file(file_path: str) -> str:
    """
    读取本地代码文件内容，当用户提供文件路径时调用此工具
    Args:
        file_path: 代码文件的本地路径，例如 test_code.py
    Returns:
        文件中的代码文本
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"错误：文件 {file_path} 不存在，请检查路径。"
    except Exception as e:
        return f"读取文件失败：{str(e)}"

tools = [read_code_file]

# 2. LLM初始化
llm = ChatOpenAI(
    model="glm-4-flash",
    temperature=0.2
)

# 3. Prompt模板
prompt = ChatPromptTemplate.from_messages([
    ("system", """你是代码解释Agent。
你的任务：
1. 如果用户输入是文件路径，调用read_code_file工具读取代码。
2. 获取代码后，完成：①整体功能说明 ②关键逻辑讲解 ③为代码添加注释。
3. 如果代码有明显问题，简单提醒。
4. 回答简洁清晰。"""),
    ("placeholder", "{chat_history}"),
    ("user", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# 4. 记忆组件，保存对话上下文
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# 5. 构建Agent
agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory, verbose=True)

# 6. 命令行交互入口（作业要求：命令行交互）
def main():
    print("===== 代码解释Agent =====")
    print("支持两种输入：①直接粘贴代码 ②输入本地代码文件路径")
    print("输入 exit 退出程序\n")
    while True:
        user_input = input(">>> 请输入：")
        if user_input.strip().lower() == "exit":
            print("Agent退出")
            break
        res = agent_executor.invoke({"input": user_input})
        print("\n【Agent输出】")
        print(res["output"])
        print("-" * 60 + "\n")

if __name__ == "__main__":
    main()