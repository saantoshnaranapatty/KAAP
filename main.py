from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import argparse
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--language", default = 'C++')
parser.add_argument("--task", default = 'return a list of numbers')
args = parser.parse_args()


llm = OpenAI()

code_prompt = PromptTemplate(
    template="Write a very short {language} function that will {task}",
    input_variables=['language', 'task'],
)

#second prompt template 
code_prompt_2 = PromptTemplate(
    template="Write a test for the {language} code :\n{code}",
    input_variables=['language', 'code']
)

code_chain = LLMChain(
    llm = llm,
    prompt = code_prompt,
    output_key= "code"
)

#second language model into which the prompt is going to be fed
code_chain_2 = LLMChain(
    llm = llm,
    prompt = code_prompt_2,
    output_key= "test"
)

#WE ARE TAKING THE OUTPUT OF CHAIN A AS THE INPUT TO CHAIN B

#SEQUENTIAL CHAIN
chain = SequentialChain(
    chains = [code_chain,code_chain_2],
    input_variables=['language', 'task'],
    output_variables=['test','code']

)

result = chain({
    "language":args.language,
    "task":args.task
}
)

print(result['code'])
print(result['test'])