# ai-assignment-agent 🤖

A conversational AI teaching assistant for CS students that explains programming assignments without giving away the solution.

## What It Does

Students paste in their assignment prompt and a description of what they're trying to do. The agent explains the concept, breaks down the problem, and guides their thinking — without writing the code for them. The goal is to support learning, not shortcut it.

## How It Works

The agent uses a two-layer prompting approach:

1. **System prompt**: a set of instructions given to Gemini that define the agent's behavior: stay educational, never produce direct code solutions, keep explanations CS-appropriate
2. **User prompt**: the student's actual assignment description and question

This combination constrains the model's output so it operates within academic integrity guidelines regardless of how the student phrases their input.

## What I Built and Learned

- Integrated the **Gemini Flash API** (evaluated GPT-4o and Claude prior to selecting Gemini for this use case)
- Designed and iterated on **system prompts** to reliably prevent code generation while keeping responses genuinely helpful
- Implemented basic **error handling** and **testing** to catch edge cases in API responses
- Learned how API request/response cycles work in practice, including how prompt structure affects output quality

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core application logic |
| Gemini Flash API | Language model backend |
| Gemini API SDK | API integration |

## Scope & Future Plans

Currently a solo project built as a focused exploration of AI agent design and API integration. Designed with CS students in mind but intended to scale across other disciplines where guided explanation (not answer generation) is the goal.

## Context

Built as a solo course project at the University of Washington Bothell. The core design challenge was not just making the agent helpful — it was making it reliably *not too* helpful.

