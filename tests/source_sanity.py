"""Lightweight source sanity check. Not a Pine compiler."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
pairs = {"(": ")", "[": "]", "{": "}"}
closers = set(pairs.values())

def strip_line(line: str) -> str:
    out = []
    in_string = False
    escaped = False
    i = 0
    while i < len(line):
        ch = line[i]
        if in_string:
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                in_string = False
            i += 1
            continue
        if ch == '"':
            in_string = True
            i += 1
            continue
        if ch == "/" and i + 1 < len(line) and line[i + 1] == "/":
            break
        out.append(ch)
        i += 1
    return "".join(out)

for path in sorted((ROOT / "indicators").glob("*.pine")):
    stack = []
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        clean = strip_line(line)
        for ch in clean:
            if ch in pairs:
                stack.append((ch, lineno))
            elif ch in closers:
                assert stack, f"{path.name}:{lineno}: unexpected {ch}"
                op, open_line = stack.pop()
                assert pairs[op] == ch, f"{path.name}:{lineno}: {op} from {open_line} closed by {ch}"
    assert not stack, f"{path.name}: unclosed delimiters {stack}"

print("PASS: source delimiters / basic sanity")