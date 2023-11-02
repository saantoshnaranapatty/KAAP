from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
#dont forget to secure this key
api_key = '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'

llm = OpenAI(
    openai_api_key = api_key
)

code_prompt = PromptTemplate(
    template="Write a very short {language} function that will {task}"
    input_variables=['language', 'task']
)

code_chain = LLMChain(
    llm = llm,
    prompt = code_prompt
)


result = llm('Write me a very short poem')

print(result)