""" Module for RAG logic """

import ollama
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma


class Rag():
    """ class defining the rag(retrieval augmented generation) """

    def format_docs(self, docs):
        """ function for joining the retrieved documents"""
        return "\n\n".join(doc.page_content for doc in docs)


    def load_vector_database(self):
        """ function for calling retriever """
        embeddings = OllamaEmbeddings(model = "mistral")
        vector_store = Chroma(persist_directory = "app/data/test-vector-store",
                              embedding_function = embeddings)
        retriever = vector_store.as_retriever()
        return retriever


    def ollama_llm(self, question: str, context: str, editor_content):
        """ function for generating response using ollama """
        formatted_prompt = f"""You are a chatbot for helping users write content. Answer using
                            the folowing information. Question: {question}\n\nContext: {context}\n\nContent: {editor_content}"""
        response = ollama.chat(model = "mistral",
                               messages = [{'role': 'user', 'content': formatted_prompt}])
        return response['message']['content']


    def rag_chat_gen(self, question: str, editor_content: str):
        """ function for chat generation using rag """
        print(editor_content)
        retriever = self.load_vector_database()
        retrieved_docs = retriever.invoke(question+editor_content)
        formatted_context = self.format_docs(retrieved_docs)
        return self.ollama_llm(question, formatted_context, editor_content)


if __name__ == "__main__":
    chat = Rag()
    print(chat.rag_chat_gen(question="Name few LLMs", editor_content="This is a test "))


# End-of-file (EOF)