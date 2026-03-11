import os

PROJECT_DIR = "projects"
README_FILE = "README.md"

def count_projects():
    total = 0

    for root, dirs, files in os.walk(PROJECT_DIR):
        for d in dirs:
            if d[:3].isdigit():
                total += 1

    return total


def progress_bar(percent):
    total_blocks = 40
    filled = int(percent / 100 * total_blocks)

    return "[" + "█" * filled + "░" * (total_blocks - filled) + "]"


def update_readme():
    completed = count_projects()
    percent = int((completed / 100) * 100)

    bar = progress_bar(percent)

    with open(README_FILE, "r") as f:
        content = f.read()

    content = content.replace(
        "Projects Completed: 0 / 100",
        f"Projects Completed: {completed} / 100"
    )

    content = content.replace(
        "[░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0%",
        f"{bar} {percent}%"
    )

    with open(README_FILE, "w") as f:
        f.write(content)


if __name__ == "__main__":
    update_readme()