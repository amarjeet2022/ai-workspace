# from app.models.chat import ChatRequest

# def chat(request: ChatRequest):

#     user_message = request.message
#     # Here you can implement your chat logic, for example, sending the message to a chatbot model and getting a response.
#     # For demonstration purposes, let's just echo the user's message.
#     reply = f"You said: {user_message}"
#     return {
#         "reply": reply
#     }
from app.models.chat import ChatRequest

def chat(request: ChatRequest):
    user_message = request.message
    reply= f"Your Prompt is: {user_message}"
    return{
        "reply": reply
    }


