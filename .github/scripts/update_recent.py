"""Rewrite the block between the RECENT markers in README.md with the most recently pushed repos."""
import json
import os
import re
import urllib.request

USER = "deeppunj"
N = 6
SKIP = {USER}  # the profile repo itself

req = urllib.request.Request(
    f"https://api.github.com/users/{USER}/repos?per_page=100&sort=pushed",
    headers={"Accept": "application/vnd.github+json",
             **({"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"} if os.environ.get("GITHUB_TOKEN") else {})},
)
repos = json.load(urllib.request.urlopen(req))

rows = ["| Project | What it is | Language | Updated |", "|---|---|---|---|"]
for r in [r for r in repos if not r["fork"] and not r["private"] and r["name"] not in SKIP][:N]:
    desc = (r["description"] or "").replace("|", "/")
    rows.append(f"| [{r['name']}]({r['html_url']}) | {desc} | {r['language'] or ''} | {r['pushed_at'][:10]} |")

with open("README.md", encoding="utf-8") as f:
    readme = f.read()
block = "<!-- RECENT:START -->\n" + "\n".join(rows) + "\n<!-- RECENT:END -->"
new = re.sub(r"<!-- RECENT:START -->.*?<!-- RECENT:END -->", block, readme, flags=re.S)
if new == readme:
    print("no change")
else:
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new)
    print("README updated")
