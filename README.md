# AI Response Quality Evaluator

A lightweight Python framework for performing structured quality evaluation and Side-by-Side (SxS) comparison of AI-generated responses.

The project demonstrates a human-in-the-loop approach to AI quality analysis. A human evaluator assesses model responses using defined quality dimensions, while the tool validates scores, calculates overall ratings, compares responses, and generates structured evaluation reports.

## 🎯 Purpose

Generative AI responses can appear convincing while still containing unsupported claims, poor assumptions, irrelevant information, or instruction-following failures.

This project provides a simple framework for evaluating those responses consistently.

It focuses on five core dimensions:

- **Grounding** — Are claims supported by the available context or evidence?
- **Relevance** — Does the response directly address the user's intent?
- **Helpfulness** — Does the response provide useful and actionable information?
- **Naturalness** — Does the response read naturally without unnecessary repetition or robotic language?
- **Instruction Adherence** — Does the response follow the user's explicit requirements?

## 🔍 Side-by-Side Evaluation

The evaluator supports comparison between **Response A** and **Response B**.

Each response receives a score from **1 to 5** across the five evaluation dimensions.

The tool then:

1. Validates the evaluation scores.
2. Calculates an overall quality score.
3. Generates a structured report for each response.
4. Compares the overall scores.
5. Identifies the preferred response or reports a tie.

## 🧠 Human-in-the-Loop Evaluation

This project intentionally does not automatically decide whether an AI response is truthful, grounded, or helpful.

These judgments require human evaluation and context.

The evaluator supplies the quality scores and written rationale, while the Python framework handles validation, aggregation, comparison, and reporting.

This design reflects the importance of human judgment in AI quality assurance and model evaluation.

## 📊 Evaluation Scale

| Score | Meaning |
|------:|---------|
| 1 | Major problems |
| 2 | Significant weaknesses |
| 3 | Acceptable but needs improvement |
| 4 | Strong response with minor issues |
| 5 | Excellent response |

## 💻 Example

```python
response_a = Evaluation(
    grounding=5,
    relevance=5,
    helpfulness=5,
    naturalness=4,
    instruction_adherence=5,
    rationale=(
        "The response directly addresses the user's request, "
        "uses the available context appropriately, and avoids "
        "unsupported assumptions."
    ),
)

response_b = Evaluation(
    grounding=3,
    relevance=4,
    helpfulness=3,
    naturalness=4,
    instruction_adherence=3,
    rationale=(
        "The response is generally relevant but introduces an "
        "unsupported assumption and does not fully satisfy the "
        "user's instruction."
    ),
)

compare_responses(response_a, response_b)
