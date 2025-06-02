# retriever.py

def build_retriever(chroma_db, score_threshold: float = 0.5, k:int = None):
    """
    根据传入的 Chroma 数据库，构造一个 Retriever。
    目前示例使用 similarity_score_threshold；如果想用 top-k，可传入 k 参数。
    返回 retriever 对象。
    """
    if k is not None:
        retriever = chroma_db.as_retriever(search_kwargs={"k": k})
    else:
        retriever = chroma_db.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={"score_threshold": score_threshold}
        )
    return retriever
