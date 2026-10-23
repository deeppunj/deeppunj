"""Rewrite the block between the RECENT markers in README.md:
a line with my latest activity + a table of my other public repos (not featured), newest first."""
import json
import os
import re
import urllib.request

USER = "deeppunj"

# already shown in "Featured projects" in the readme, so not repeated in the table
# (if you feature a new repo, add its name here)
FEATURED = {
    "patient-finding-synthea",
    "laser-defect-inspection-ml",
    "battery-dispatch-be",
    "sipho-coupler-study",
}

# never shown: the profile repo itself, the old archive, and work in progress / repos without a readme yet
SKIP = {
    USER,
    "portfolio-projects_old",
    "SQL_Pandas_FaceOff",
    "Optical-Engineering-Portfolio",
}

req = urllib.request.Request(
    f"https://api.github.com/users/{USER}/repos?per_page=100&sort=pushed",
    headers={"Accept": "application/vnd.github+json",
             **({"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"} if os.environ.get("GITHUB_TOKEN") else {})},
)
repos = json.load(urllib.request.urlopen(req))

# public, own (not forked), not archived, not the profile repo; already sorted newest push first
repos = [r for r in repos if not r["fork"] and not r["private"] and not r["archived"] and r["name"] != USER]

lines = []

# latest activity over all repos (featured ones too)
if repos:
    latest = repos[0]
    lines.append(f"Latest activity: [{latest['name']}]({latest['html_url']}), {latest['pushed_at'][:10]}")
    lines.append("")

others = [r for r in repos if r["name"] not in FEATURED and r["name"] not in SKIP]
if others:
    lines += ["| Project | What it is | Updated |", "|---|---|---|"]
    for r in others:
        desc = (r["description"] or "").replace("|", "/").strip()
        lines.append(f"| [{r['name']}]({r['html_url']}) | {desc} | {r['pushed_at'][:10]} |")

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
