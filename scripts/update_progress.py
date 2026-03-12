import os
import re

PROJECT_DIR = "projects"
PROGRESS_FILE = "progress.md"


def get_completed_projects():
    completed = set()

    for root, dirs, files in os.walk(PROJECT_DIR):
        for d in dirs:
            if re.match(r"\d{3}-", d):
                number = int(d[:3])
                completed.add(number)

    return completed


def update_progress():
    completed_projects = get_completed_projects()

    with open(PROGRESS_FILE, "r") as f:
        lines = f.readlines()

    new_lines = []

    for line in lines:
        match = re.match(r"\|\s*(\d+)\s*\|", line)

        if match:
            day = int(match.group(1))

            if day in completed_projects:
                line = re.sub(r"⏳|🚧", "✅", line)

        new_lines.append(line)

    with open(PROGRESS_FILE, "w") as f:
        f.writelines(new_lines)


if __name__ == "__main__":
    update_progress()