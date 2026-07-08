# from fastapi import APIRouter
# from app.models.chat import ChatRequest
# from app.services.chat_service import chat

# router = APIRouter()
 
#  @router.post("/chat")
#  def chat_api(request: ChatRequest):
#    return chat(request)

from fastapi import APIRouter
from app.models.chat import ChatRequest
from app.services.chat_service import chat

router = APIRouter()

@router.post("/chat")
def chat_api(request: ChatRequest):
    return chat(request)