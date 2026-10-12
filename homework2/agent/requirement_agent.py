from langchain_openai import ChatOpenAI
class RequirementAgent:
    def __init__(self,llm):
        self.llm=llm
    def run(self,user_input):
        prompt=f"""你是需求分析师，整理用户需求，输出结构化需求文档。用户需求：{user_input}
输出：功能需求、非功能需求、输入输出描述。"""
        res=self.llm.invoke(prompt)
        return {"stage":"requirement","content":res.content}