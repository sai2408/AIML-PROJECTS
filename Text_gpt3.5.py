
import openai

openai.api_key = "api" 

prompt = "Write a creative story about traveling to Mars."

response = openai.Completion.create(
    engine="gpt-3.5-turbo-instruct",  
    prompt=prompt,
    max_tokens=150,  
    n=1,
)

generated_text = response.choices[0].text.strip()
print("Generated Text:\n", generated_text)
