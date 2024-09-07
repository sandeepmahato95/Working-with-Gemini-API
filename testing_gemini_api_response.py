# Modules to install:
# pip install google-generativeai langchain-google-genai python-dotenv

# You can run the following command in your terminal to install these modules:
# pip install google-generativeai langchain-google-genai python-dotenv

import google.generativeai as genai
import os
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
result = llm.invoke(" Who is Vikram Sarabhai in 25 words")
print(result.content)

# Output:
# Vikram Sarabhai was an Indian physicist, mathematician, and astronomer who is considered the father of India's space program.