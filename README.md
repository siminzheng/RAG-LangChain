本项目通过使用LangChain实现一个RAG检索增强生成实例，大模型版本为gpt3.5-turbo,向量嵌入模型为text-embedding-3-small，调用的是OpenAI官方api接口


项目结构为：

```text
RAG-LangChain/
├── .env
├── .gitignore
├── requirements.txt
├── config.py
├── loader.py
├── vectorstore.py
├── retriever.py
├── prompt.py
└── main.py


.env：存放环境变量（API Key、Base URL 等）。

.gitignore：忽略 .env 和其他不需要提交的文件。

requirements.txt：列出项目依赖。

config.py：加载并暴露环境变量。

loader.py：负责文档加载与切分（PDF → 文本 chunk).

vectorstore.py：负责向量化并构建 Chroma 数据库。

retriever.py：封装检索器（Retriever）。

prompt.py：定义 Prompt 模板。

main.py：主入口，组织各模块，运行 RAG 查询。

使用步骤
安装依赖

bash
复制
编辑
cd langchain_rag
pip install -r requirements.txt
**填写 .env **
把你的实际 OPENAI_API_KEY 和 OPENAI_API_BASE 填进去。

运行 main.py

bash
复制
编辑
python main.py
你会看到打印的 Prompt 内容，以及 LLM 返回的答案。
