from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
required=['SKILL.md','README.md','knowledge/curriculum.json','knowledge/foundations.md','references/answerless-exam.md','references/verification.md','references/plotting.md','references/latex-pdf.md','references/full-book.md','scripts/plot_examples.py','templates/lesson.tex']
for name in required:assert (root/name).is_file(),f'missing: {name}'
data=json.loads((root/'knowledge/curriculum.json').read_text(encoding='utf-8'))
topics=data['topics'];ids={t['id'] for t in topics}
assert len(ids)==len(topics) and len(topics)>50
assert all(t['title'] and t['section'] and t['status'] in ('index_only','draft','reviewed') for t in topics)
assert all(set(t['prerequisites'])<=ids for t in topics)
coverage=json.loads((root/'data/coverage.json').read_text(encoding='utf-8'))
assert coverage['indexed_topics']==len(topics)
print(f'PASS: {len(topics)} indexed topics; required files present; no mathematical correctness claim.')
