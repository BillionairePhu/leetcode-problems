import os
import sys
import requests
from jinja2 import Template
import leetcodequeries
from leetcodetypes import *


def problem_path(problem_number: int):
    return f"ProblemSet_{problem_number//100:02d}xx/Problem_{problem_number}"

SOLUTION_TEMPLATE_PATH = "template.md"
SUPPORTED_LANG_EXT = {"cpp":".cpp", "python":".py", "python3":".py","csharp":".cs"}
def create_solution(question: Question, name: str = "solution", lang: str | None = None):
    if lang == None:
        langlist = ["python3"]
    else:
        langlist = lang.split(",")
    question_id = int(question.questionFrontendId)
    folder_name = problem_path(question_id)
    os.makedirs(folder_name, exist_ok=True)
    print(f"Generated: 📁 {folder_name}")

    solution_path = os.path.join(folder_name, "README.md")
    with open(SOLUTION_TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = Template(f.read())
        output = template.render(question = question)
    with open(solution_path, "w", encoding="utf-8") as f:
        f.write(output)
    

    found_lang = {snip.langSlug: snip for snip in question.codeSnippets}
    for i in langlist:
        if (ext := SUPPORTED_LANG_EXT.get(i)) and (snippet := found_lang.get(i)):
            code_path = os.path.join(folder_name, name + ext)
            if not os.path.exists(code_path):
                with open(code_path, 'w') as f:
                    f.write(snippet.code)
                    print(f"Generated: 📁 {code_path}.")
            else:
                print(f"Warning: {code_path} already exists.")
    print("Finished creating all files.")

def gen_daily(**kwargs):
    response = requests.post(leetcodequeries.url, headers=leetcodequeries.headers, json={
        "query": leetcodequeries.dailyquery,
        "variables": {}
    })

    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")
    print("Fetched from daily GraphQL successfully")
    daily = ActiveDailyCodingChallengeQuestion.model_validate(response.json()["data"]["activeDailyCodingChallengeQuestion"])

    create_solution(daily.question, **kwargs)

def gen_classic(problem_number: int, **kwargs):
    response = requests.post(leetcodequeries.url, headers=leetcodequeries.headers, json={
        "query": leetcodequeries.problemlistquery,
        "variables": {"categorySlug":"","skip": problem_number - 1,"limit":1,"filters":{}}
    })

    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")
    print(f"Found Problem number {problem_number}")
    problemlist = ProblemSetQuestionList.model_validate(response.json()["data"]["problemsetQuestionList"])

    slug = problemlist.questions[0].titleSlug

    response = requests.post(leetcodequeries.url, headers=leetcodequeries.headers, json={
        "query": leetcodequeries.questiondataquery,
        "variables": {"titleSlug": slug}
    })

    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")
    question = Question.model_validate(response.json()["data"]["question"])

    create_solution(question, **kwargs)

help_message = """
Usage:
    python gen-leetcode.py [command] [arguments] -k [kwargs]

Commands:
    help                Show this help message.
    daily               Generate today's LeetCode daily challenge folder.
    classic <number>    Generate folder for a classic LeetCode problem by number.

Examples:
    python gen-leetcode.py daily
    python gen-leetcode.py classic 1234
"""
def main(*args, **kwargs):
    try:
        match args[0]:
            case "help":
                print(help_message)
            case "daily":
                gen_daily(**kwargs)
            case "classic":
                problem_number = int(args[1])
                gen_classic(problem_number, **kwargs)
            case _:
                raise Exception("Invalid command")
    except Exception as e:
        print(f"\033[31mAn error occurred: {e}\033[0m")
        print(help_message)

if __name__ == "__main__":
    try:
        endargs = sys.argv.index("-k")
    except:
        endargs = len(sys.argv)
    main(*sys.argv[1:endargs], **dict(arg.split('=') for arg in sys.argv[endargs + 1:]))
