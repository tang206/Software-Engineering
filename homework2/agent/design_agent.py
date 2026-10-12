from langchain_openai import ChatOpenAI
class DesignAgent:
    def __init__(self,llm):
        self.llm=llm
    def run(self,state):
        req_doc=state["content"]
        prompt=f"""你是软件设计师，基于下面需求文档，输出简易模块设计。需求文档：{req_doc}
输出：模块划分、模块职责、模块接口。"""
        res=self.llm.invoke(prompt)
        return {"stage":"design","content":res.content}