# loader.py
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_split_pdf(pdf_path: str, chunk_size: int = 200, chunk_overlap: int = 100):
    """
    加载 PDF 并按字符递归切分为若干 Document（带 start_index）。
    返回列表：[Document, Document, ...]
    """
    loader = PyPDFLoader(pdf_path)
    pages = loader.load_and_split()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        add_start_index=True,
    )

    documents = []
    for page in pages:
        documents.extend(text_splitter.create_documents([page.page_content]))

    return documents
