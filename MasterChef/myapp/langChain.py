from decouple import config
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate


def askme_recipe(recipe_topic):
    SECRET_KEY = config('SECRET_KEY')
    model = ChatOpenAI(openai_api_key=SECRET_KEY)
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You have to answer food releated"),
        ("user", "{topic}"),
    ])
   
    chat=model.invoke(prompt_template.invoke({"topic": recipe_topic}))
    
    return chat.content
    