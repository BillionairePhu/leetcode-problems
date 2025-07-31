import os
import sys
import shutil
import requests
from jinja2 import Template


help_message = """
Usage:
    python gen-leetcode.py [command] [arguments]

Commands:
    help                Show this help message.
    daily               Generate today's LeetCode daily challenge folder.
    classic <number>    Generate folder for a classic LeetCode problem by number.

Examples:
    python gen-leetcode.py daily
    python gen-leetcode.py classic 1234
"""

def problem_path(problem_number : int):
    return f"ProblemSet_{problem_number%100}/Problem_{problem_number}"

def gen_daily():
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
    question_id = int(question['frontendQuestionId'])
    folder_name = problem_path(question_id)

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


def gen_classic(problem_number: int):

    folder_name = problem_path(problem_number)
    os.makedirs(folder_name, exist_ok=True)

    # Generate Python file
    code_path = os.path.join(folder_name, f"solution.py")
    if not os.path.exists(code_path):
        with open(code_path, 'w') as f:
            f.write("# Write your solution here\n")
        print(f"Created: {code_path}")

    # Copy sample.md to README.md
    readme_path = os.path.join(folder_name, "README.md")
    if not os.path.exists(md_path):
        print("Error: sample.md not found in the current directory.")
        return

    if not os.path.exists(readme_path):
        shutil.copy(md_path, readme_path)
        print(f"Copied sample.md → {readme_path}")

    print(f"\n📁 {folder_name} is ready!")

md_path = "template.md"
def main():
    if len(sys.argv) == 1:
        print(help_message)
    match sys.argv[1]:
        case "help":
            print(help_message)
        case "daily":
            gen_daily()
        case "classic":
            if not sys.argv[2].isdigit():
                print("Error: Problem number must be a digit.")
                return
            problem_number = int(sys.argv[2])
            gen_classic(problem_number)

if __name__ == "__main__":
    main()