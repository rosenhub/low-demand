#!/usr/bin/env python3
"""
Deterministic demand lint. No API key needed.

Checks a response for the patterns the skill bans and that can be detected
without a judge: filler openers/closers, breathe/calm-down directives (rule 6),
feeling-narration (rule 7), instructions and suggestions (rule 4), cheer
(rule 5), plus two measured checks: any question mark (rule 3) and any
numbered step (rule 4).

Usage:
    python lint.py response.md [more.md ...]
    python lint.py --json response.md
    cat response.md | python lint.py -

Exit code is the number of files with at least one finding (max 1 per file),
so it works as a CI gate.
"""
import json
import re
import sys

FILLER = [
    r"\bgreat question\b", r"\bgood question\b", r"\babsolutely!?\b", r"\bcertainly!?\b",
    r"\bi'?d be happy to\b", r"\bhappy to help\b", r"\bof course!\b",
    r"\bhope (this|that) helps\b", r"\blet me know if\b", r"\bfeel free to\b",
    r"\bdon'?t hesitate\b", r"\bthanks for (asking|reaching out|sharing)\b",
    r"\bi hope you find\b", r"\bas an ai\b",
]

BREATHE_CALM = [
    r"\bcalm down\b", r"\bstay calm\b", r"\btry to (stay|be|remain) calm\b",
    r"\btake a (slow|few) breath", r"\bdeep breath", r"\bbreathe in\b",
    r"\bbreathing exercise", r"\bbox breathing\b", r"\bground(ing)? (yourself|exercise|technique)\b",
    r"\brelax\b", r"\bjust relax\b", r"\bcount to (ten|10)\b",
]

FEELING_NARRATION = [
    r"\bi understand how you feel\b", r"\bi understand (that )?(you'?re|you are|this is)\b",
    r"\bi (can )?(hear|see|sense|tell) (that )?you'?re (feeling|frustrated|upset|anxious|stressed|overwhelmed)\b",
    r"\byou (seem|sound|must be|must feel) (really |so |very )?(frustrated|upset|anxious|stressed|overwhelmed|exhausted|angry)\b",
    r"\bthat must be (so |really |very )?(hard|difficult|frustrating|exhausting|overwhelming)\b",
    r"\bit'?s (completely |totally )?(okay|valid|normal|understandable) to feel\b",
    r"\byour feelings are valid\b", r"\bi know (this|that|it) (is|feels|can be) (hard|frustrating|overwhelming)\b",
]

INSTRUCTION_SUGGESTION = [
    r"\bhave you tried\b", r"\byou should\b", r"\byou could try\b", r"\byou might (want to )?try\b",
    r"\btry (to |taking |stepping |writing |reaching |making |focusing )", r"\bit (might|may|can|could) help to\b",
    r"\bhere are some (steps|things|ideas|suggestions|tips)\b", r"\bhere'?s what (i'?d|i would|you can) do\b",
    r"\blet'?s break (this|it) down\b", r"\bbreak (this|it) down\b", r"\bone step at a time\b",
    r"\bstep (away|back) from\b", r"\bconsider (taking|reaching|talking|writing)\b",
    r"\bmake a (short |quick )?list\b", r"\breach out to\b", r"\bdrink some water\b",
    r"\bwhen you'?re ready, (we|let'?s|you)\b", r"\bwhenever you'?re ready\b",
]

CHEER = [
    r"\bit'?s going to be (okay|ok|alright|fine)\b", r"\bit'?ll be (okay|ok|alright|fine)\b",
    r"\bdon'?t worry\b", r"\byou'?ve got this\b", r"\byou can do (this|it)\b",
    r"\bwe'?ll (get through|figure) (this|it) (out )?together\b", r"\bwe'?ll figure (this|it) out\b",
    r"\bthis too shall pass\b", r"\bhang in there\b", r"\bstay positive\b", r"\bbrighter days\b",
    r"\byou'?re (not alone|stronger than)\b", r"\bbetter days\b", r"\bsilver lining\b",
    r"[\U0001F300-\U0001FAFF☀-➿]",
]

CHECKS = [
    ("C5 filler", FILLER),
    ("C4 breathe/calm down", BREATHE_CALM),
    ("C4 feeling narration", FEELING_NARRATION),
    ("C3 instruction/suggestion", INSTRUCTION_SUGGESTION),
    ("C4 cheer", CHEER),
]


def lint(text: str) -> dict:
    findings = []
    low = text.lower()
    for label, patterns in CHECKS:
        for pat in patterns:
            for m in re.finditer(pat, low):
                findings.append({"check": label, "match": text[m.start():m.end()], "pos": m.start()})
    # measured checks: any question mark (rule 3), any numbered step (rule 4)
    for m in re.finditer(r"\?", text):
        findings.append({"check": "C3 question mark", "match": text[max(0, m.start()-20):m.end()].strip(), "pos": m.start()})
    for m in re.finditer(r"(?m)^\s*(\d+[.)]|step \d+)", low):
        findings.append({"check": "C3 numbered step", "match": text[m.start():m.end()].strip(), "pos": m.start()})
    findings.sort(key=lambda f: f["pos"])
    words = len(text.split())
    questions = text.count("?")
    steps = len(re.findall(r"(?m)^\s*(\d+[.)]|step \d+)", low))
    return {
        "words": words,
        "questions": questions,
        "numbered_steps": steps,
        "findings": findings,
        "clean": not findings,
    }


def main(argv):
    as_json = "--json" in argv
    paths = [a for a in argv if not a.startswith("--")]
    if not paths:
        print(__doc__)
        return 2
    failed = 0
    out = {}
    for p in paths:
        text = sys.stdin.read() if p == "-" else open(p, encoding="utf-8").read()
        r = lint(text)
        out[p] = r
        if not r["clean"]:
            failed += 1
        if not as_json:
            status = "CLEAN" if r["clean"] else f"{len(r['findings'])} finding(s)"
            print(f"{p}: {status}  [{r['words']} words, {r['questions']} question(s), "
                  f"{r['numbered_steps']} numbered step(s)]")
            for f in r["findings"]:
                print(f"    {f['check']:<26} \"{f['match']}\"")
    if as_json:
        print(json.dumps(out, indent=2))
    return min(failed, 1)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
