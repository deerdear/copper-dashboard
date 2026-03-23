#!/usr/bin/env python3
"""Replace the INLINE_DATA blob in index.html with current market_data.json."""
import json
import re
from pathlib import Path

root = Path(__file__).parent
html_path = root / "index.html"
json_path = root / "market_data.json"

data = json.loads(json_path.read_text())
blob = json.dumps(data, separators=(",", ":"))

html = html_path.read_text()
html = re.sub(
    r'const INLINE_DATA=\{.*?\};',
    f'const INLINE_DATA={blob};',
    html,
    count=1,
    flags=re.DOTALL,
)
html_path.write_text(html)
print(f"Inlined {len(blob)} bytes into index.html")
