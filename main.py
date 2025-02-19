import os
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain import HuggingFacePipeline
from langchain.llms import LlamaCpp

# Retrieve OpenAI API key from environment variables
openai_key = os.getenv("OPENAI_API_KEY")

def extract_text_from_pdfs(pdf_files):
    accumulated_text = ""
    for pdf_file in pdf_files:
        pdf_reader = PdfReader(pdf_file)
        for page in pdf_reader.pages:
            accumulated_text += page.extract_text()
    return accumulated_text

def split_text(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=500,
        chunk_overlap=100,
        length_function=len
    )
    text_segments = text_splitter.split_text(text)
    return text_segments

def generate_vector_store(text_segments):
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(texts=text_segments, embedding=embeddings)
    return vector_store

def initialize_conversation_chain(vector_store):
    language_model = ChatOpenAI(api_key=openai_key)
    conversation_memory = ConversationBufferMemory(
        memory_key='conversation_history', return_messages=True)
    convo_chain = ConversationalRetrievalChain.from_llm(
        llm=language_model,
        retriever=vector_store.as_retriever(
            search_type="similarity", search_kwargs={"k": 4}),
        memory=conversation_memory,
    )
    return convo_chain

def process_user_input(user_input):
    interaction = st.session_state.conversation({'question': user_input})
    st.session_state.conversation_history = interaction['chat_history']
    for idx, message in enumerate(st.session_state.conversation_history):
        if idx % 2 == 0:
            st.write(f'You: {message.content}')
        else:
            st.write(f'Bot: {message.content}')

def app_main():
    load_dotenv()
    st.set_page_config(page_title="Document Chat Interface",
                       page_icon=":robot_face:")
    st.title("Document Chat Interface :robot_face:")

    with st.sidebar:
        st.header("Document Upload")
        pdf_files = st.file_uploader(
            "Load your PDFs and hit 'Process'", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing Documents"):
                # Extract text from PDFs
                extracted_text = extract_text_from_pdfs(pdf_files)

                # Split the text into segments
                text_segments = split_text(extracted_text)

                # Generate vector store from text segments
                vector_store = generate_vector_store(text_segments)

                # Initialize the conversation chain
                st.session_state.conversation = initialize_conversation_chain(
                    vector_store)
                
    user_input = st.text_input("Pose your queries regarding the documents:")
    if user_input:
        process_user_input(user_input)

if __name__ == '__main__':
    app_main()
