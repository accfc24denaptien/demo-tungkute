import subprocess
from datetime import datetime

# Lấy 20 commit gần nhất
result = subprocess.run(
    ["git", "log", "--pretty=format:%h|%ad|%s", "--date=short", "-20"],
    capture_output=True,
    text=True,
    check=True
)

lines = result.stdout.splitlines()

content = "# Changelog\n\n"

for line in lines:
    commit, date, message = line.split("|", 2)
    content += f"- **{date}** `{commit}` {message}\n"

with open("CHANGELOG.md", "w", encoding="utf-8") as f:
    f.write(content)

print("CHANGELOG updated")
