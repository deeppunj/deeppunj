"""Rewrite the block between the RECENT markers in README.md.

Shows:
- a "More projects" list with only the repos I tagged with the topic "portfolio" (and that have a description),
  except the ones already in "Featured projects"
- one small line with my latest activity

To show a repo here: on its GitHub page, About (gear icon) -> add a description and the topic "portfolio".
"""
import json
import os
import re
import urllib.request

USER = "deeppunj"
TOPIC = "portfolio"

# already in "Featured projects" in the readme, so not listed again
FEATURED = {
    "patient-finding-synthea",
    "laser-defect-inspection-ml",
    "battery-dispatch-be",
    "sipho-coupler-study",
}

req = urllib.request.Request(
    f"https://api.github.com/users/{USER}/repos?per_page=100&sort=pushed",
    headers={"Accept": "application/vnd.github+json",
             **({"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"} if os.environ.get("GITHUB_TOKEN") else {})},
)
repos = json.load(urllib.request.urlopen(req))

# my own public repos, newest push first, without the profile repo
repos = [r for r in repos if not r["fork"] and not r["private"] and not r["archived"] and r["name"] != USER]

lines = []

# tagged repos with a description, not featured
more = [r for r in repos
        if TOPIC in r.get("topics", []) and r["description"] and r["name"] not in FEATURED]
if more:
    lines += ["## More projects", ""]
    for r in more:
        desc = r["description"].strip().rstrip(".")
        lines.append(f"- **[{r['name']}]({r['html_url']})**: {desc}")
    lines.append("")

if repos:
    latest = repos[0]
    lines.append(f"<sub>Latest activity: <a href=\"{latest['html_url']}\">{latest['name']}</a>, "
                 f"{latest['pushed_at'][:10]} · this section updates automatically</sub>")

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

block = "<!-- RECENT:START -->\n" + "\n".join(lines) + "\n<!-- RECENT:END -->"
new = re.sub(r"<!-- RECENT:START -->.*?<!-- RECENT:END -->", block, readme, flags=re.S)

if new == readme:
    print("no change")
else:
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new)
    print("README updated")
