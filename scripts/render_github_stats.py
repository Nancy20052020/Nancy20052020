#!/usr/bin/env python3
"""Render all-time public GitHub stats cards for the profile README.

The hosted stats image only counts the last year unless it falls back to
GitHub's commit search, which undercounts the contribution graph. This sums
contribution years instead, which is the total shown on the profile graph.
"""

from __future__ import annotations

import json
import os
import subprocess
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

LOGIN = "Nancy20052020"
ROOT = Path(__file__).resolve().parents[1]
OUT_LIGHT = ROOT / "assets" / "github-stats-light.png"
OUT_DARK = ROOT / "assets" / "github-stats-dark.png"

THEMES = {
    "light": {
        "bg": (247, 241, 230),
        "title": (107, 63, 160),
        "label": (61, 41, 20),
        "value": (61, 41, 20),
        "icon": (184, 134, 11),
        "line": (230, 214, 184),
    },
    "dark": {
        "bg": (22, 17, 28),
        "title": (230, 211, 163),
        "label": (247, 241, 230),
        "value": (247, 241, 230),
        "icon": (212, 177, 90),
        "line": (62, 48, 78),
    },
}


def api(query: str, variables: dict | None = None) -> dict:
    payload = json.dumps({"query": query, "variables": variables or {}}).encode()
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        req = urllib.request.Request(
            "https://api.github.com/graphql",
            data=payload,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
                "User-Agent": "nancy-profile-stats",
            },
        )
        with urllib.request.urlopen(req) as response:
            body = json.load(response)
    else:
        cmd = ["gh", "api", "graphql", "--input", "-"]
        body = json.loads(subprocess.check_output(cmd, input=payload))
    if body.get("errors"):
        raise SystemExit(json.dumps(body["errors"], indent=2))
    return body["data"]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
        if bold
        else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/macos/Inter-SemiBold.ttf"
        if bold
        else "/usr/share/fonts/truetype/macos/Inter-Regular.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def stats() -> dict[str, int]:
    created = api(
        """
        query($login: String!) {
          user(login: $login) { createdAt }
        }
        """,
        {"login": LOGIN},
    )["user"]["createdAt"]
    start = datetime.fromisoformat(created.replace("Z", "+00:00"))
    now = datetime.now(timezone.utc)
    commits = 0
    cursor = start
    while cursor < now:
        end = min(cursor + timedelta(days=360), now)
        window = api(
            """
            query($login: String!, $from: DateTime!, $to: DateTime!) {
              user(login: $login) {
                contributionsCollection(from: $from, to: $to) {
                  totalCommitContributions
                }
              }
            }
            """,
            {
                "login": LOGIN,
                "from": cursor.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "to": end.strftime("%Y-%m-%dT%H:%M:%SZ"),
            },
        )["user"]["contributionsCollection"]["totalCommitContributions"]
        commits += window
        cursor = end

    summary = api(
        """
        query($login: String!) {
          user(login: $login) {
            pullRequests { totalCount }
            issues { totalCount }
            repositories(first: 100, ownerAffiliations: OWNER, isFork: false) {
              nodes { stargazerCount }
            }
          }
        }
        """,
        {"login": LOGIN},
    )["user"]
    stars = sum(repo["stargazerCount"] for repo in summary["repositories"]["nodes"])
    return {
        "commits": commits,
        "prs": summary["pullRequests"]["totalCount"],
        "issues": summary["issues"]["totalCount"],
        "stars": stars,
    }


def draw_icon(
    draw: ImageDraw.ImageDraw,
    kind: str,
    x: int,
    y: int,
    color: tuple[int, int, int],
    scale: int,
) -> None:
    stroke = max(2, 2 * scale)

    def p(dx: float, dy: float) -> tuple[int, int]:
        return (int(x + dx * scale), int(y + dy * scale))

    if kind == "star":
        draw.regular_polygon((p(11, 12)[0], p(11, 12)[1], 9 * scale), 5, rotation=270, outline=color, width=stroke)
    elif kind == "commit":
        draw.ellipse((*p(2, 3), *p(20, 21)), outline=color, width=stroke)
        draw.line((*p(11, 7), *p(11, 16)), fill=color, width=stroke)
        draw.line((*p(7, 11), *p(15, 11)), fill=color, width=stroke)
    elif kind == "pr":
        draw.ellipse((*p(2, 2), *p(9, 9)), outline=color, width=stroke)
        draw.ellipse((*p(13, 2), *p(20, 9)), outline=color, width=stroke)
        draw.ellipse((*p(13, 14), *p(20, 21)), outline=color, width=stroke)
        draw.line((*p(5, 9), *p(5, 16)), fill=color, width=stroke)
        draw.line((*p(5, 16), *p(13, 17)), fill=color, width=stroke)
        draw.line((*p(16, 9), *p(16, 14)), fill=color, width=stroke)
    elif kind == "issue":
        draw.ellipse((*p(2, 2), *p(20, 20)), outline=color, width=stroke)
        draw.ellipse((*p(9, 6), *p(13, 10)), fill=color)
        draw.line((*p(11, 12), *p(11, 16)), fill=color, width=stroke)


def render(theme_name: str, numbers: dict[str, int]) -> Image.Image:
    theme = THEMES[theme_name]
    scale = 2
    width, height = 450 * scale, 195 * scale
    image = Image.new("RGB", (width, height), theme["bg"])
    draw = ImageDraw.Draw(image)
    title_font = font(18 * scale, bold=True)
    label_font = font(14 * scale, bold=True)
    value_font = font(14 * scale, bold=True)

    draw.text((25 * scale, 18 * scale), "GitHub stats", font=title_font, fill=theme["title"])
    draw.line((25 * scale, 52 * scale, 425 * scale, 52 * scale), fill=theme["line"], width=scale)

    rows = [
        ("star", "Total stars", f"{numbers['stars']:,}"),
        ("commit", "Total commits (all time)", f"{numbers['commits']:,}"),
        ("pr", "Total pull requests", f"{numbers['prs']:,}"),
        ("issue", "Total issues", f"{numbers['issues']:,}"),
    ]
    for index, (kind, label, value) in enumerate(rows):
        y = (68 + index * 28) * scale
        draw_icon(draw, kind, 25 * scale, y, theme["icon"], scale)
        draw.text((54 * scale, y), label, font=label_font, fill=theme["label"])
        value_width = value_font.getlength(value)
        draw.text((425 * scale - value_width, y), value, font=value_font, fill=theme["value"])
    return image


def main() -> None:
    numbers = stats()
    print(json.dumps(numbers))
    OUT_LIGHT.parent.mkdir(parents=True, exist_ok=True)
    render("light", numbers).save(OUT_LIGHT, "PNG", optimize=True)
    render("dark", numbers).save(OUT_DARK, "PNG", optimize=True)
    print(f"wrote {OUT_LIGHT.name} and {OUT_DARK.name}")


if __name__ == "__main__":
    main()
