"""
AI Response Quality Evaluator

A lightweight framework for evaluating AI-generated responses
across common quality dimensions.

Author: Lincoln Njogu
"""

from dataclasses import dataclass


@dataclass
class Evaluation:
    grounding: int
    relevance: int
    helpfulness: int
    naturalness: int
    instruction_adherence: int
    rationale: str = ""

    def validate(self):
        """Ensure every score is between 1 and 5."""

        scores = {
            "Grounding": self.grounding,
            "Relevance": self.relevance,
            "Helpfulness": self.helpfulness,
            "Naturalness": self.naturalness,
            "Instruction Adherence": self.instruction_adherence,
        }

        for dimension, score in scores.items():
            if not 1 <= score <= 5:
                raise ValueError(
                    f"{dimension} score must be between 1 and 5."
                )

    def overall_score(self):
        """Calculate the average quality score."""

        self.validate()

        scores = [
            self.grounding,
            self.relevance,
            self.helpfulness,
            self.naturalness,
            self.instruction_adherence,
        ]

        return round(sum(scores) / len(scores), 2)

    def report(self):
        """Generate a readable evaluation report."""

        self.validate()

        return f"""
AI RESPONSE QUALITY REPORT
--------------------------
Grounding:             {self.grounding}/5
Relevance:             {self.relevance}/5
Helpfulness:           {self.helpfulness}/5
Naturalness:           {self.naturalness}/5
Instruction Adherence: {self.instruction_adherence}/5

Overall Score: {self.overall_score()}/5

Rationale:
{self.rationale}
"""


if __name__ == "__main__":

    example = Evaluation(
        grounding=5,
        relevance=5,
        helpfulness=4,
        naturalness=4,
        instruction_adherence=5,
        rationale=(
            "The response directly addresses the user's request, "
            "remains grounded in the available context, and avoids "
            "unsupported assumptions."
        ),
    )

    print(example.report())
