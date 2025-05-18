from pydantic import BaseModel

class ResponseModel(BaseModel):
	"""LLM output"""
	answer: str
