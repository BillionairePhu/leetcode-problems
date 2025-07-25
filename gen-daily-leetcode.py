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

data = response.json()['data']['activeDailyCodingChallengeQuestion']
question = data['question']
question['link'] = data['link']
question['acRate'] = round(question['acRate'], 2)
folder_name = f"Problem_{question['frontendQuestionId']}"

os.makedirs(folder_name, exist_ok=True)

# Step 2: Load the markdown template
md_path = os.path.join(folder_name, "README.md")
with open("template.md", "r", encoding="utf-8") as f:
  template = Template(f.read())
output = template.render(**question)
with open(md_path, "w", encoding="utf-8") as f:
  f.write(output)
  
# Step 3: Generate Python code file
code_path = os.path.join(folder_name, "solution.py")
if not os.path.exists(code_path):
  with open(code_path, 'w') as f:
    f.write("# Write your solution here\n")

print(f"Generated: 📁 {folder_name}")