# vectorstore.py
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from config import OPENAI_API_KEY, OPENAI_API_BASE

def build_vectorstore(documents, persist_directory: str = None):
    """
    将传入的 Document 列表做向量化并构建 Chroma 数据库。
    如果需要持久化，可传入 persist_directory。
    返回 Chroma 实例。
    """
    # 1. 构造 OpenAIEmbeddings：使用从 .env 里读取的 KEY / BASE
    embeddings_model = OpenAIEmbeddings(
        model="text-embedding-3-small",
        openai_api_key=OPENAI_API_KEY,
        openai_api_base=OPENAI_API_BASE
    )

    # 2. 用 Chroma.from_documents 构造向量库
    if persist_directory:
        db = Chroma.from_documents(
            documents,
            embeddings_model,
            persist_directory=persist_directory
        )
    else:
        db = Chroma.from_documents(documents, embeddings_model)

    return db
