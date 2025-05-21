import os
from openai import OpenAI
from datetime import datetime


# Read in HTML
html = None
with open("index.html", "r", encoding="utf-8") as file:
    html = file.read()

date = datetime.now().strftime("%Y-%m-%d")

prompt = f"""
Please search the web for the 7 top AI news articles from today ({date}).

Only use articles from major news corps.

Use this content to update the below HTML: article summaries, titles, links and favicons.

Also update the date string at the top of the feed.

All articles must be real and from today ({date}) and links must be working.

Do not otherwise alter the HTML.

Respond only with the HTML.

{html}
"""

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Create a response with web search tool
response = client.responses.create(
    model="gpt-4o",
    input=prompt,
    tools=[{"type": "web_search"}]
)

# Extract the content from the response
output = response.output[1].content[0].text

# Write the content to index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(output)

