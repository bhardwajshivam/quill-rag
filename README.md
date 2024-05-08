# Quill RAG : An editor with RAG based chat functionality.

## Abstract
This project introduces the Quill RAG system, an innovative editor application that allows users to write and ask questions simultaneously. The frontend of the application is built using Reflex, a Python wrapper for React. The backend incorporates RAG (Retrieval-Augmented Generation) technology, enhancing the user experience by providing intelligent responses. The vector database, created using Chroma, contains references from the paper "Exploring the Potential of Large Language Models in Computational Argumentation." The project aims to increase interaction while writing content with the help of a chatbot that answers questions related to the text. The RAG system pulls out relevant documents from the vector database using the written context as well as the question asked by the user and ollama helps generate a relevant response.

## Contents
1. Overview
2. Modelling
    * Ollama
    * Reflex.dev
3. Getting Started
    * Structure
4. Environment Setup
    * Python Environment
5. Dataset
6. Acknowledgements
7. Research Notice

## Built with
* Reflex
* Ollama
* Chroma

# Overview
The Quill RAG system revolutionizes the way users interact with text, enabling seamless writing and querying. Its architecture comprises a frontend developed with Reflex, empowering users with a dynamic and responsive interface. Meanwhile, the backend leverages RAG technology for intelligent content generation and retrieval.

## Modelling


### Ollama
Ollama, in the context of the Quill RAG system, stands as a versatile tool for leveraging local large language models (LLMs). By harnessing local LLMs, Ollama empowers the system to process and interpret user queries with heightened contextuality and relevance. Through seamless integration with local LLMs, Ollama facilitates the extraction of nuanced insights and generates responses that are tailored to the specific domain or dataset at hand. In this project, Ollama uses Mistral-7B as the LLM to generate response.

### Reflex.dev
Reflex.dev forms the frontend framework of the Quill RAG system. It offers a user-friendly environment for composing text and posing questions via chatbot, ensuring a smooth and intuitive experience.

## Getting Started
1. Clone the repository
```
git clone git@github.com:bhardwajshivam/quill-rag.git
```

2. Create a virtual environment
```
virtualenv -p python3 venv
```

3. Activate virtual env
```
source venv/bin/activate
```

4. Install required libraries
```
pip install -r requirements.txt
```

5. Move to app directory
```
cd app
```

6. Run application using reflex
```
reflex run
```

## Environment Setup


### Python environment
* python 3.11
* Required Packages: ollama, reflex, chroma, langchain, chromadb, sqlite3-binary, pytest

## Dataset

The dataset used in the Quill RAG system comprises references from the paper "Exploring the Potential of Large Language Models in Computational Argumentation." This comprehensive collection enriches the system's knowledge base, enabling informed responses to user inquiries.

## Acknowledgements

We extend our gratitude to the authors of "Exploring the Potential of Large Language Models in Computational Argumentation" for their valuable contributions to the field.


## Research Notice

The ideas presented in this repository are part of academic research. Please do not use the novel ideas presented in a research setting without permission from the authors.