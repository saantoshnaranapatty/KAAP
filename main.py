from langchain.llms import OpenAI

#dont forget to secure this key
api_key = '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'

llm = OpenAI(
    openai_api_key = api_key
)

result = llm('Write me a very short poem')

print(result)