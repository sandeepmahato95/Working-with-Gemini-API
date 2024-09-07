'''
Modules to install:
1. google-generativeai 
2. langchain-google-genai 
3. python-dotenv

You can run the following command in your terminal to install these modules:
pip install google-generativeai langchain-google-genai python-dotenv

Note: You need to have a Google API key to use this module.
You can get your Google API key by following these steps:
1. Go to the https://aistudio.google.com/app/apikey

2. Create an API key and save it in your .env file.
GOOGLE_API_KEY='your_generatedapi_key
'''

import google.generativeai as genai
import os
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
result = llm.invoke(" Who is Vikram Sarabhai in 25 words")
print(result.content)

# Output as Gemini API response:
# Vikram Sarabhai was an Indian physicist, mathematician, and astronomer who is considered the father of India's space program.