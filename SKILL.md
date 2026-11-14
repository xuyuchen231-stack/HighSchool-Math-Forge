---
name: highschool-math-forge
description: Chinese senior-high-school mathematics tutoring, rigorous independent exam solving, zero-prerequisite explanations, LaTeX mathematical typesetting, Python/SymPy verification, and mathematically accurate reproducible diagrams.
---
# HighSchool-Math-Forge

## Scope
A reusable Agent Skill for Chinese high-school mathematics and Gaokao papers, including algebra, functions, geometry, trigonometry, sequences, probability/statistics, calculus, vectors, and mathematical modeling. Follow the actual province/year examination syllabus; do not assume all provinces share one paper. Knowledge indexes are not finished lessons.

## Required workflows
1. **Read source**: inspect every original paper page, including charts, diagrams, answer blanks and subquestions. Inventory questions before solving. Never reconstruct unreadable expressions by guesswork.
2. **Solve independently**: for each problem state givens, unknowns, domain restrictions, core theorem, derivation, and answer. Distinguish necessary from sufficient conditions, prove both directions when needed, and handle boundary/equality cases.
3. **Verify**: use a second algebraic or geometric approach where feasible. SymPy or numerical tests are *supporting checks*, not substitutes for proofs. Reject extraneous roots and check units, intervals and end points. See `references/verification.md`.
4. **Teach from zero**: explain prerequisites in natural Chinese, show why a formula applies, expand omitted transformations, illustrate a worked example and a variant. Explain all options and all subquestions. See `references/knowledge-standard.md`.
5. **Draw correctly**: use Python Matplotlib, SymPy, or appropriate geometry tools; derive coordinates and labels from equations rather than inventing visual data. Clearly distinguish exact diagrams from schematics, with parameter values, units and source. See `references/plotting.md`.
6. **Compose**: use LaTeX as the canonical mathematical source (`amsmath`, `amssymb`, `mathtools`, `geometry`, `fontspec`/`ctex` with XeLaTeX or LuaLaTeX). Include intact original exam when authorized, then fully explained solutions and lessons. See `references/latex-pdf.md`.
7. **Inspect**: compile, render every page, inspect clipping/line breaks/figure accuracy and verify page/question inventory. Never call incomplete work 'final'.

## Routing
- Full answerless exam -> `references/answerless-exam.md` and `references/full-book.md`.
- Individual lesson -> `references/knowledge-standard.md` and `knowledge/foundations.md`.
- Graphing or geometry -> `references/plotting.md` and `scripts/plot_examples.py`.
- LaTeX/PDF -> `references/latex-pdf.md` and `templates/lesson.tex`.
- Quality assurance -> `references/verification.md` and `scripts/validate.py`.

## Strict acceptance gates
- Every question, option, figure and subpart present and accounted for; source ambiguities explicitly flagged.
- No unproved mathematical claims, false generalizations, missing domains, fabricated data, or decorative but incorrect diagrams.
- Every formula typeset in LaTeX, with readable notation and no unexplained step leaps for weak students.
- Original paper preserved in the PDF when supplied/authorized; graph evidence directly annotated where relevant.
- Any mathematical diagram generated from reproducible code with recorded assumptions and parameters.
- Knowledge coverage reported honestly: `index_only` does not mean reviewed.
- A failed verification or missing source prevents final delivery.

## Tool compatibility
Python 3, SymPy, NumPy, Matplotlib, optional SciPy, and a TeX distribution with XeLaTeX/LuaLaTeX are recommended. In ChatGPT use file/Python/PDF tools; in Codex or Claude Code use the same repository instructions. If an execution dependency is unavailable, state the limitation; do not claim a compiled PDF or validated plot.
