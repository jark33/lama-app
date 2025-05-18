from ollama import chat
from ollama import ChatResponse

def predict(question:str) -> str:
	response: ChatResponse = chat(
	  model='llama3.2',messages=[
	  {
		'role':'user',
		'content': question,
		},
	 ])
	 
	return  response.message.content	
