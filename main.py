# main.py
import os
from config import OPENAI_API_KEY, OPENAI_API_BASE
from loader import load_and_split_pdf
from vectorstore import build_vectorstore
from retriever import build_retriever
from prompt import get_prompt

from langchain_openai import ChatOpenAI

def main():
    # 1. 加载并切分 PDF → Document 列表
    pdf_path = "/root/autodl-tmp/ragtest/langchain_rag/Transformer_interview.pdf"
    documents = load_and_split_pdf(pdf_path)

    # 2. 向量化并构建 Chroma 数据库（内存模式，不持久化）
    chroma_db = build_vectorstore(documents)

    # 3. 构造 Retriever（以相似度阈值 0.5 为例）
    retriever = build_retriever(chroma_db, score_threshold=0.5)

    # 4. 定义查询（query）
    query = "如何降低 Transformer 的 Feedforward 层的参数数量？"

    # 5. 用 Retriever 拿到相关 Document（这里用 invoke）
    docs = retriever.invoke(query)
    if not docs:
        print("未检索到任何文档片段，可能阈值太高或数据库为空。")
        return

    # 6. 取一个文档片段来组装 Prompt（你也可以把前 N 个拼接起来）
    info_chunk = docs[0].page_content  # 或者你想拼接多个

    # 7. 构造 Prompt
    prompt = get_prompt(info=info_chunk, question=query)
    print("=== 调用 LLM 前的 Prompt ===")
    print(prompt)
    print("=" * 50)

    # 8. 调用 ChatOpenAI 生成回答
    chat_model = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        openai_api_key=OPENAI_API_KEY,
        openai_api_base=OPENAI_API_BASE
    )

    response = chat_model.invoke(prompt)
    print("=== LLM 返回 ===")
    print(response.content)

if __name__ == "__main__":
    main()
