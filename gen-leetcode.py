import os
import sys
import shutil

md_path = "template.md"

def main():
    if len(sys.argv) != 2:
        print("Usage: python gen-leetcode.py <problem_number>")
        return

    problem_number = sys.argv[1]

    if not problem_number.isdigit():
        print("Error: Problem number must be a digit.")
        return

    folder_name = f"Problem_{problem_number}"
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

if __name__ == "__main__":
    main()
