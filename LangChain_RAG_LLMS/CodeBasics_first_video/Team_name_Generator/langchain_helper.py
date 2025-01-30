import streamlit as st
import os
from langchain_google_genai import GoogleGenerativeAI
from secret_key import key
from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


os.environ["GOOGLE_API_KEY"] = key

llm = GoogleGenerativeAI(model="gemini-pro", temperature=0.7)

def gen_team_name(event):
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to partisipate in {cuisine}. Suggest a fency name for this.respound with one name"
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some Profiles for this team {restaurant_name}. (i mean the skills try to make your response consised)"
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")
    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', "menu_items"]
    )
    response = chain({"cuisine": event})
    return response


if __name__ == "__main__":
    print(gen_team_name("hackathon"))
















