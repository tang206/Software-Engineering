from langchain_openai import ChatOpenAI
class CodeAgent:
    def __init__(self,llm):
        self.llm=llm
    def run(self,state):
        design_doc=state["content"]
        prompt=f"""你是开发工程师，根据下面模块设计，生成完整可运行Python代码。设计文档：{design_doc}"""
        res=self.llm.invoke(prompt)
        return {"stage":"code","content":res.content}