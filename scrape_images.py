import requests
from bs4 import BeautifulSoup
import openai
from io import BytesIO
from PIL import Image

# Scraping images using requests, beautifullsoup4 and the openai API.
# Choose a thing to search for. Example is "dog".

url = "https://www.example.com"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

# Set up OpenAI API credentials.
openai.api_key = "YOUR-KEY"

for img in soup.find_all("img"):
    img_url = img.get("src")
    
    img_content = requests.get(img_url).content
    
    response = openai.Image.create(images=[BytesIO(img_content)])
    image_data = response['data'][0]
    
    # Check if the image contains a dog and display it.
    if "dog" in image_data['concepts']:
        Image.open(BytesIO(img_content)).show()
