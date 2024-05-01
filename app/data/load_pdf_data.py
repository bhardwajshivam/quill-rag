""" Module for loading data and creating a vector DB """

from os import path
from glob import glob
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
embeddings = OllamaEmbeddings(model="mistral")

list_data = []

def find_ext(dr: str, ext: str):
    """ function for extracting pdf file names from the data directory. """
    x = glob(path.join(dr,"*.{}".format(ext)))
    return x

# creating a list consisting names of pdf files
list_data = find_ext("app/data/pdf-data", "pdf")
loader = PyPDFLoader(list_data[0])
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap = 200)
docs = loader.load_and_split(text_splitter)
splits = text_splitter.split_documents(docs)
embeddings = OllamaEmbeddings(model="mistral")

# initializing vector_store with the first pdf file
vector_store = Chroma.from_documents(documents = splits, embedding = embeddings,
                                     persist_directory="app/data/vector-store")
vector_store.persist()

# looping through the other pdfs and adding embeddings to our vector store
for i in range(1, len(list_data)):
    try:
        cur_pdf = list_data[i]
        loader = PyPDFLoader(cur_pdf)
        print(i+1,"/76")
        new_docs = loader.load_and_split(text_splitter)
        vector_store.add_documents(new_docs)
        vector_store.persist()
    except ValueError:
        print("Look into the file")

# End-of-file (EOF)