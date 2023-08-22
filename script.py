from dotenv import load_dotenv
load_dotenv()
import os

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

llm = OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'))
chat_model = ChatOpenAI()

llm.predict("hi!")

chat_model.predict("hi!")