import openai
openai.api_key = "" #Replace with your actual API key
prompt = "a cute cat sitting on a cushion"
response = openai.Image.create(
    prompt=prompt,
    n=1,  
    size="256x256",
    quality="standard",
)
image_url = response.data[0].url
print("Generated Image URL:", image_url)
