from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
    "Hello {name}, welcome to AgriOS!"
)

result = prompt.invoke({"name": "Agaran"})

print(result)