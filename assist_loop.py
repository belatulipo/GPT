import openai
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # set up key
client = OpenAI()

# function to interact with the OpenAI API
def ask_openai(messages, model="gpt-4o"):
    response = client.chat.completions.create(
    #response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    return response.choices[0].message.content

# a list to maintain the conversation context
conversation_history = [{"role": "system", "content": "You are a helpful assistant."}]

def update_conversation(role, content):
    global conversation_history
    conversation_history.append({"role": role, "content": content})

# a loop to repeatedly get user input, call the OpenAI API, and display the response
def chat_with_assistant():
    print("Start chatting with the assistant (type 'exit' to stop):")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        
        update_conversation("user", user_input)
        response = ask_openai(conversation_history)
        print(f"Assistant: {response}")
        
        update_conversation("assistant", response)

if __name__ == "__main__":
        chat_with_assistant()
