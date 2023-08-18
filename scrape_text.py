import openai
import requests
from bs4 import BeautifulSoup

# Scraping text using requests, beautifullsoup4 and the openai API.


# Set up OpenAI API credentials
openai.api_key = "YOUR_API_KEY"

url = "https://www.example.com"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

html_sections = [str(p) for p in soup.find_all('p')]

# Find the text field in each HTML section
search_query = "find this text field"
search_results = []
for section in html_sections:
    section_results = openai.Completion.create(
        engine="davinci",
        prompt=f"Find the text field '{search_query}' in the HTML content:\n\n{section}",
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )
    search_results.append(section_results.choices[0].text)

# Print the search results
print(search_results)