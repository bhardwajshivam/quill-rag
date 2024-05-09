""" Module for testing """

from app.backend.rag_logic import Rag

def test_rag_chat_gen_default() -> None:
    """ Function for testing the rag_chat_gen()"""
    test_fn = Rag()
    test_res = test_fn.rag_chat_gen("what is the need of argumentation and generation in language models?", "This is a test editor context")
    test_flag = False
    if test_res is not None:
        test_flag = True
    assert test_flag is True

def test_rag_chat_gen_with_no_context() -> None:
    """ Function for testing the rag_chat_gen()"""
    test_fn = Rag()
    test_res = test_fn.rag_chat_gen("what is the need of argumentation and generation in language models?", "")
    test_flag = False
    if test_res is not None:
        test_flag = True
    assert test_flag is True

def test_ollama_llm() -> None:
    """ Function for testing ollama """
    test_fn = Rag()
    question = "What is LLM?"
    context = "LLM stands for Large Language Model"
    test_res = test_fn.ollama_llm(question, context, editor_content = "editor content")
    test_flag = False
    if test_res is not None:
        test_flag = True
    assert test_flag is True

def test_ollama_llm_with_empty_editor_content() -> None:
    """ Function for testing ollama """
    test_fn = Rag()
    question = "What is LLM?"
    context = "LLM stands for Large Language Model"
    test_res = test_fn.ollama_llm(question, context, editor_content = "")
    test_flag = False
    if test_res is not None:
        test_flag = True
    assert test_flag is True



# End-of-file (EOF)
