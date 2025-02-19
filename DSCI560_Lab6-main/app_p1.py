import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
from langchain import HuggingFacePipeline
from langchain.llms import LlamaCpp


def get_pdf_text(pdf_docs):
    # Your Code here
    return


def get_text_chunks(text):
    #Your Code here
    return


def get_vectorstore(text_chunks):
    # your code here
    # Create a vectorStore and return it
    return


def get_conversation_chain(vectorstore):
    
    # create conversation_chain for OpenAI llm, Hugging Face and Llama llm
    return conversation_chain


def handle_userinput(user_question, conversation):
    # Put your code here


def main():
    pdf_docs = ['file1', 'file2']

    # get pdf text

    # get the text chunks

    # create vector store

    # create conversation chain

    # code for getting user questions and answering them


if __name__ == '__main__':
    main()