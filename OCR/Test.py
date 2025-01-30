import openai

# Set your API key

openai.api_key = "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"

# send request 
response = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages = [
        {"role" : "user", "content" : "You are helpful assistant"}
    ]
)
print(response["choices"][0]["message"]["content"])