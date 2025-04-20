# import openai

# openai.api_type = "openrouter"
# openai.api_base = "https://api.openrouter.ai/v1"  # OpenRouter API base URL
# openai.api_version = "v1"  # OpenRouter API version
# openai.api_key= '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'  # Replace with your OpenAI API key
# def chat_with_gpt(prompt):
#     try:
#         response= openai.chat.completions.create(
#             model="openai/gpt-3.5-turbo",  # Make sure the model name matches OpenRouter format
#             messages=[
#                 {"role": "user", "content": prompt}
#             ])
#         return response.choices[0].message.content
    
#     except Exception as e:
#         return f"Error: {str(e)}"

# if __name__ == "__main__":
#     while True:
#         user_inp = input("You:\n")
#         if user_inp.lower() == "exit":
#             break
#         response = chat_with_gpt(user_inp)
#         print("Bot:\n", response)



# import openai

# openai.api_key = "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"  # Your OpenRouter API key
# openai.api_base = "https://openrouter.ai/api/v1"
# def chat_with_gpt(prompt):
#     try:
#         response = openai.ChatCompletion.create(
#             model="openai/gpt-3.5-turbo",
#             messages=[{"role": "user", "content": prompt}]
#         )
#         return response.choices[0].message["content"]
#     except Exception as e:
#         return f"Error: {str(e)}"

# if __name__ == "__main__":
#     while True:
#         user_inp = input("You:\n")
#         if user_inp.lower() == "exit":
#             break
#         response = chat_with_gpt(user_inp)
#         print("Bot:\n", response)



from openai import OpenAI

client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1",  # OpenRouter base
)

def chat_with_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",  # Make sure you are allowed to use this model
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    while True:
        user_inp = input("You:\n")
        if user_inp.lower() == "exit":
            break
        response = chat_with_gpt(user_inp)
        print("Bot:\n", response)
