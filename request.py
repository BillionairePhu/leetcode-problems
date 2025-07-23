import requests
import json
from jinja2 import Template
import os

# Step 1: Fetch data from LeetCode
url = "https://leetcode.com/graphql/"
headers = {
    "accept": "*/*",
    "content-type": "application/json",
}

payload = {
    "query": """
    query questionOfToday {
      activeDailyCodingChallengeQuestion {
        date
        userStatus
        link
        question {
          titleSlug
          title
          translatedTitle
          acRate
          difficulty
          freqBar
          frontendQuestionId: questionFrontendId
          isFavor
          paidOnly: isPaidOnly
          status
          hasVideoSolution
          hasSolution
          topicTags {
            name
            id
            slug
          }
        }
      }
    }
    """,
    "variables": {},
    "operationName": "questionOfToday"
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code != 200:
    raise Exception(f"Failed to fetch data: {response.status_code}")
print(response.json())

data = response.json()['data']['activeDailyCodingChallengeQuestion']
question = data['question']
question['link'] = data['link']
question['acRate'] = round(question['acRate'], 2)

# Step 2: Load the markdown template
with open("template.md", "r", encoding="utf-8") as f:
    template = Template(f.read())

# Step 3: Render the template with data
output = template.render(**question)

# Step 4: Save the rendered markdown
filename = f"{question['frontendQuestionId']}.md"
with open(filename, "w", encoding="utf-8") as f:
    f.write(output)

print(f"Generated: {filename}")