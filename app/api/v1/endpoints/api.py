import os,sys
# Add the root directory to the Python path
current_script_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = (current_script_dir.split('\\app'))[0]
sys.path.append(root_dir)
from typing import List, Optional
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from app.api.v1.endpoints import chatgpt




class ChatRequest(BaseModel):
    technologies:List[str]
    difficulty:Optional[str]=""

class ChatResponse(BaseModel):
    response:str
    difficulty:str

router=APIRouter()

@router.post('/chat', response_model=ChatResponse)
async def chat(request:ChatRequest):
    """
    This is the chat endpoint which will return project ideas as per the user's technology preference and difficulty level
    """
    try:
        response,diff = chatgpt.get_project_idea(technologies=request.technologies,difficulty=request.difficulty.lower())
        return {
            'response':response,
            'difficulty':diff
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occured while processing your request")
