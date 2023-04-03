#Import required modules to test if they are installed
import time
import importlib.util as iutil
import os

master_start = time.time()
modules = ['PyPDF2', 'langchain', 'openai', 'faiss', 'dotenv']

print('Checking for required modules...')

for mods in modules:
    if iutil.find_spec(mods) is None:
        print('Installing ' + mods + '.')
        if modules == 'faiss':
            os.system('pip install faiss-cpu')
        else:
            os.system('pip install ' + mods)
    else:
        print(mods + ' is installed.')

print('All required modules are installed.')

#https://harishgarg.com/writing/build-a-chatgpt-for-your-pdf-documents/#:~:text=Easiest%20Guide%20to%20build%20a%20chatGPT%20for%20your,...%207%20Create%20embeddings%20...%208%20Conclusion%20

# import the modules
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
# load .env file
from dotenv import load_dotenv
from pathlib import Path
import pickle

payload = Path(r'C:\Users\Dylan\Desktop\Python\OPENAIAPI.env')
env = load_dotenv(dotenv_path = payload)

interestedPDF = PdfReader(r"C:\Users\Dylan\Downloads\Power SCADA Operation 2020 System Guide.pdf")

raw_text = ""

for i, page in enumerate(interestedPDF.pages):
    text = page.extract_text()
    if text:
        raw_text += text

text_splitter = CharacterTextSplitter(        
    separator = "\n",
    chunk_size = 1000,
    chunk_overlap  = 200,
    length_function = len,
)
texts = text_splitter.split_text(raw_text)

print(len(texts))

embeddings = OpenAIEmbeddings()

with open(r'C:\Users\Dylan\Desktop\Python\PSO2020.pkl', 'wb') as f:
    pickle.dump(embeddings, f)


master_end = time.time()

print('Script completed in ', round(master_end-master_start,4), ' seconds.')

#this does not render what you are looking for. You need to read in the pdf as a text file then slice into chunks, summerize each chunk, merge the chunks into one text file, what a new summary from the merged chunks of text, generate key notes from the summary, create step by step guide from the key notes
# maybe look into more PDF to ChatGPT examples? You know that one lady... maybe she can help.
# https://www.allabtai.com/how-to-summarize-a-pdf-with-gpt-3/
# https://www.allabtai.com/how-to-summarize-a-large-text-with-gpt-3/
# https://www.allabtai.com/how-to-create-multiple-types-of-content-from-youtube-video-with-gpt-3-and-python/
#Maybe you can connect with a programmer? 