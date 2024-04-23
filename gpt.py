import google.generativeai as genai

query = input('Enter a prompt: ')

with open("data.txt", "r") as f1:
    info = f1.read()

template = f"{query} based on the given data: {info}"

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-pro")

response = model.generate_content(template)
print(response.text)
