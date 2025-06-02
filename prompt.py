# prompt.py
from langchain.prompts import PromptTemplate

PROMPT_TEMPLATE = """
你是一个问答机器人。
你的任务是根据下述给定的已知信息回答用户问题。
确保你的回复完全依据下述已知信息。不要编造答案。
如果下述已知信息不足以回答用户的问题，请直接回复"我无法回答您的问题"。
已知信息：
{info}
用户问：
{question}
请用中文回答用户问题。
"""

def get_prompt(info: str, question: str) -> str:
    """
    使用 PromptTemplate 生成完整 prompt 字符串。
    """
    template = PromptTemplate.from_template(PROMPT_TEMPLATE)
    return template.format(info=info, question=question)
