from datetime import datetime

now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

content = f"""# Auto Update

Last update:

{now}
"""

with open("README.md","w",encoding="utf8") as f:
    f.write(content)

print("README updated")
