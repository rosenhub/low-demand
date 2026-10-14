# Contributing

## Proposing a rule change

Open an issue using the **Rule proposal** template. It asks for three things:

1. A real before/after pair. Real means you saw the "before" from an actual agent while you or someone you support was in overload.
2. One sentence on who it helps.
3. Which existing rule it changes, or where it goes if it is new.

Autistic and PDA contributors: your experience is the evidence. "This reply made it worse because..." is a complete argument. You do not need a study.

Rules are capped at 12. A new rule has to replace or merge into an existing one. This keeps the skill short enough that every host loads it in full.

## Adding a host

Open a PR that adds a row to the table in README.md and, if the host has a standard path, a line in `install.sh`. Include a link to the host's docs for the path.

## Benchmark results

Run `eval/run.py`, then open a PR that adds the generated `results/<model>-<date>.md` and a row in `results/README.md`. Say which judge model you used. Results from models other than the one the maintainer tested are the most useful. Include the `false_alarm` row; a skill that over-triggers is a bug.

## Translations

`README.<lang>.md`, kept to the first screen plus the 12-rule table. Link it from the language bar at the top of README.md. Translating SKILL.md itself is welcome as `SKILL.<lang>.md`; the English file stays canonical. If you translate rule 12, replace 988 with your country's equivalent line and say which it is.

## What will not be merged

- Rules that turn the mode on for every message. It is a mode, not a personality. See "What this is not" in SKILL.md.
- Rules that add questions, steps, or techniques to the overload reply, however gentle.
- Anything that turns rule 12 into risk assessment. The skill names a human once; it does not diagnose.
- Anything that adds code to the install path. The skill is a markdown file. The installer is a shell script. That's it.
