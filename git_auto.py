from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path


CATEGORY_MAP = {
    "array": "array",
    "binary tree": "binary-tree",
    "frequency_map": "frequency-map",
    "greedy algorithm": "greedy",
    "leetcode": "leetcode",
    "linked list": "linked-list",
    "queue": "queue",
    "recursion": "recursion",
    "sliding window": "sliding-window",
    "stack": "stack",
    "strings": "strings",
}

LEETCODE_FILENAME = re.compile(r"^(?P<number>\d+)\.\s*(?P<title>.+?)\.py$", re.IGNORECASE)

TOPIC_MAP = {
    "array": "array",
    "arrays": "array",
    "binary tree": "binary tree",
    "binary trees": "binary tree",
    "frequency_map": "frequency map",
    "greedy algorithm": "greedy",
    "linked list": "linked list",
    "queue": "queue",
    "recursion": "recursion",
    "sliding window": "sliding window",
    "stack": "stack",
    "string": "string",
    "strings": "string",
}


def run_git(args: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=cwd,
        text=True,
        capture_output=True,
        check=False,
    )


def normalize_category(path: str) -> str:
    first_part = Path(path).parts[0].lower() if Path(path).parts else ""
    if first_part in CATEGORY_MAP:
        return CATEGORY_MAP[first_part]

    normalized = first_part.replace("_", " ").strip()
    return CATEGORY_MAP.get(normalized, "update")


def normalize_topic(folder_name: str) -> str:
    normalized = folder_name.lower().replace("_", " ").strip()
    return TOPIC_MAP.get(normalized, normalized or "update")


def build_leetcode_message(changed_paths: list[str], difficulty: str) -> str | None:
    for path in changed_paths:
        parts = Path(path).parts
        if not parts:
            continue

        filename = parts[-1]
        match = LEETCODE_FILENAME.match(filename)
        if not match:
            continue

        number = match.group("number")
        folder = parts[0] if len(parts) > 1 else "leetcode"
        topic = normalize_topic(folder)
        return f"leetcode : {number} topic {topic} difficulty {difficulty} solved"

    return None


def build_message(changed_paths: list[str], difficulty: str) -> str:
    leetcode_message = build_leetcode_message(changed_paths, difficulty)
    if leetcode_message:
        return leetcode_message

    categories = [normalize_category(path) for path in changed_paths]
    category = Counter(categories).most_common(1)[0][0] if categories else "update"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"{category}: auto commit {timestamp}"


def prompt_difficulty(default: str = "medium") -> str:
    valid_difficulties = {"easy", "medium", "hard"}

    while True:
        response = input(f"Enter difficulty [easy/medium/hard] (default: {default}): ").strip().lower()
        if not response:
            return default
        if response in valid_difficulties:
            return response

        print("Please enter easy, medium, or hard.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Stage, commit, and push changes.")
    parser.add_argument("-m", "--message", help="Override the generated commit message.")
    parser.add_argument(
        "--difficulty",
        choices=["easy", "medium", "hard"],
        default=None,
        help="Difficulty used in the auto-generated LeetCode commit message.",
    )
    parser.add_argument("--no-push", action="store_true", help="Commit without pushing.")
    args = parser.parse_args()

    difficulty = args.difficulty or prompt_difficulty()

    repo_root = Path(__file__).resolve().parent

    status_result = run_git(["status", "--porcelain"], repo_root)
    if status_result.returncode != 0:
        sys.stderr.write(status_result.stderr)
        return status_result.returncode

    changed_lines = [line for line in status_result.stdout.splitlines() if line.strip()]
    if not changed_lines:
        print("No changes to commit.")
        return 0

    add_result = run_git(["add", "-A"], repo_root)
    if add_result.returncode != 0:
        sys.stderr.write(add_result.stderr)
        return add_result.returncode

    changed_paths = []
    for line in changed_lines:
        path = line[3:].strip()
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        changed_paths.append(path)

    message = args.message or build_message(changed_paths, difficulty)

    commit_result = run_git(["commit", "-m", message], repo_root)
    if commit_result.returncode != 0:
        sys.stderr.write(commit_result.stdout)
        sys.stderr.write(commit_result.stderr)
        return commit_result.returncode

    print(commit_result.stdout.strip())

    if args.no_push:
        print("Push skipped by request.")
        return 0

    push_result = run_git(["push"], repo_root)
    if push_result.returncode != 0:
        sys.stderr.write(push_result.stdout)
        sys.stderr.write(push_result.stderr)
        return push_result.returncode

    print(push_result.stdout.strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())