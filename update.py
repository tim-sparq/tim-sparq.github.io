import os
from openai import OpenAI
from datetime import datetime


# Read in HTML
data = None
with open("data.json", "r", encoding="utf-8") as file:
    data = file.read()

date = datetime.now().strftime("%Y-%m-%d")

prompt = f"""
Please search the web for the top 7 AI news articles from today ({date}).

Only use articles from major news corps. Don't use sites with paywalls.

Use this content to update the below JSON: article summaries, titles, links and favicons.

Don't modify the view counts - these are just placeholders for now.

All articles must be real and from today ({date}) and links must be working.

Do not otherwise alter the JSON.

Respond only with the JSON. Do not include your usual ```json format tags.

{data}
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
with open("data.json", "w", encoding="utf-8") as f:
    f.write(output)
