# Job Resume Tailor

`job-resume-tailor` is an Agent Skill for evidence-based job-fit analysis, interview preparation, and resume tailoring. It turns a resume and a job description into a structured application decision and, when requested, a set of role-specific application materials.

The skill is designed for OpenAI Codex and other agents that support the Agent Skills format.

## What It Can Do

### Job-fit analysis

- Parse resumes and job descriptions into structured evidence.
- Evaluate responsibilities and qualifications line by line.
- Calculate a transparent 100-point match score.
- Separate direct evidence, transferable experience, and unsupported gaps.
- Identify fatal, material, and manageable risks.
- Recommend whether to prioritize, explore, or skip a role.

### Interview preparation

- Build a concise candidate positioning statement.
- Map resume evidence to the target role.
- Develop STAR stories without inventing details.
- Predict behavioral and role-specific questions.
- Prepare thoughtful questions for the interviewer.
- Create a gap-mitigation and final preparation plan.

### Mock interviews

- Run behavioral, role-specific, case, or mixed interviews.
- Ask one question at a time.
- Evaluate relevance, structure, evidence, metrics, and clarity.
- Provide concrete feedback after each answer.

### Resume tailoring

- Reorganize truthful resume content around the target role.
- Align terminology with the job description when supported by evidence.
- Strengthen bullets using action, scope, method, and result.
- Produce classic, modern, or minimal HTML resumes.
- Prioritize ATS-safe structure by default.
- Generate an expanded or annotated version on request.

### Additional workflows

- Compare up to five roles in one batch.
- Research companies, markets, products, and competitors.
- Analyze skills gaps and career-transition positioning.
- Benchmark compensation using current sources.
- Draft cover letters and improve LinkedIn positioning.
- Archive application artifacts and maintain an application tracker.
- Track local resume versions without publishing private history.

## Design Principles

- **Evidence first:** important claims must be supported by the resume, job description, or attributed research.
- **No fabrication:** the skill never invents achievements, metrics, credentials, dates, or skills.
- **Candid scoring:** a low match score is treated as useful decision support.
- **User control:** tailored resumes are generated only after explicit approval.
- **Privacy:** personal application history and local version data are not intended for public distribution.

## Installation

Install with the Skills CLI:

```bash
npx skills add liheyuting/job-resume-tailor
```

You can also clone the repository and place the skill in a directory discovered by your agent.

## Example Prompts

```text
Analyze this job against my resume and tell me whether I should apply.
```

```text
Compare these three positions and rank them by fit and interview probability.
```

```text
Prepare me for the interview using only evidence from my resume.
```

```text
Tailor my resume for this role, but do not change any facts or invent metrics.
```

```text
Run a mixed mock interview for this position and give feedback after each answer.
```

## Typical Output

A standard analysis includes:

1. Executive fit summary.
2. Transparent match score and confidence rating.
3. Responsibility-by-responsibility comparison.
4. Qualification-by-qualification comparison.
5. Strengths, risks, and evidence gaps.
6. Positioning strategy.
7. Clear application recommendation.
8. Optional next steps for interviews, research, or resume tailoring.

## Repository Contents

```text
job-resume-tailor/
├── SKILL.md
├── README.md
├── LICENSE
└── agents/
    └── openai.yaml
```

`SKILL.md` contains the operational instructions used by the agent. `README.md` is the human-facing overview. `agents/openai.yaml` provides Codex interface metadata.

## Privacy Notice

Do not commit real resumes, contact information, job-application archives, or `data/versions.json` files containing personal application history to a public repository. Keep those files local unless the owner explicitly authorizes publication.

## License

MIT License. See [LICENSE](LICENSE).
