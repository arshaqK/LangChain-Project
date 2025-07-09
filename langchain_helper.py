from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from key import gemini_key
import os

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=gemini_key,
    temperature=0.6
)

def generate_res_name_and_items(cuisine):
    
    prompt_temp_name = PromptTemplate(
        input_variables = ['cuisine'],
        template = "I want to open a restaurant for {cuisine} food. Suggest only one fancy name for it"
    )             

    name_chain = LLMChain(llm=llm, prompt=prompt_temp_name, output_key="restaurant_name")

    prompt_temp_items = PromptTemplate(
        input_variables = ['restaurant_name'],
        template = "Suggest some menu items for {restaurant_name}. Return it as a comma separated list"
    )             

    item_chain = LLMChain(llm=llm, prompt=prompt_temp_items, output_key="menu_items")

    chain = SequentialChain(
        chains = [name_chain, item_chain],
        input_variables = ['cuisine'],
        output_variables = ['restaurant_name', 'menu_items']
    )

    response = chain({'cuisine': cuisine})

    return response

if __name__ == '__main__':
    print(generate_res_name_and_items("Italian"))