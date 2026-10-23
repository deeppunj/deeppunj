"""Rewrite the block between the RECENT markers in README.md.

Shows a "More projects" section in the same style as "Featured projects":
only repos tagged with the topic "portfolio" that have a description, not the featured ones.
The other topics of the repo are shown as tool tags.

To add a repo: on its GitHub page, About (gear icon) -> description + topic "portfolio" (+ tool topics like "power-bi").
"""
import json
import os
import re
import urllib.request

USER = "deeppunj"
TOPIC = "portfolio"

# already in "Featured projects", not listed again
FEATURED = {
    "patient-finding-synthea",
    "laser-defect-inspection-ml",
    "battery-dispatch-be",
    "sipho-coupler-study",
}

# readable titles, also the order they are shown in. repos not in here come after, newest first,
# with a title made from the repo name
TITLES = {
    "powerbi_fda_drug_shortages": "US drug shortages dashboard",
    "portfolio-projects_old": "Earlier data projects",
}

req = urllib.request.Request(
    f"https://api.github.com/users/{USER}/repos?per_page=100&sort=pushed",
    headers={"Accept": "application/vnd.github+json",
             **({"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"} if os.environ.get("GITHUB_TOKEN") else {})},
)
repos = json.load(urllib.request.urlopen(req))

# my own public repos, newest push first, without the profile repo
repos = [r for r in repos if not r["fork"] and not r["private"] and not r["archived"] and r["name"] != USER]


def title(repo):
    if repo["name"] in TITLES:
        return TITLES[repo["name"]]
    # my_repo-name -> My repo name
    return repo["name"].replace("_", " ").replace("-", " ").capitalize()


more = [r for r in repos if TOPIC in r.get("topics", []) and r["description"] and r["name"] not in FEATURED]
order = list(TITLES)
more.sort(key=lambda r: order.index(r["name"]) if r["name"] in order else len(order))  # stable: rest stays newest first

# latest activity over all my repos (featured ones too)
last_update = ""
if repos:
    latest = repos[0]
    last_update = f"Last update: [{latest['name']}]({latest['html_url']}), {latest['pushed_at'][:10]}"

lines = []
if more:
    lines += ["## More projects", ""]
    if last_update:
        lines += [last_update, ""]
    for r in more:
        lines.append(f"**[{title(r)}]({r['html_url']})**<br>")
        lines.append(r["description"].strip())
        tags = [t for t in r.get("topics", []) if t != TOPIC]
        if tags:
            lines += ["", " ".join(f"`{t}`" for t in tags)]
        lines.append("")
elif last_update:
    lines.append(last_update)

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
