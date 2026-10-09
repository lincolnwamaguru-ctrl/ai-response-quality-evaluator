"""
AI Response Quality Evaluator

A lightweight framework for evaluating and comparing AI-generated
responses across common quality dimensions.

Author: Lincoln Njogu
"""

from dataclasses import dataclass


@dataclass
class Evaluation:
    """Stores quality scores and evaluator rationale for one AI response."""

    grounding: int
    relevance: int
    helpfulness: int
    naturalness: int
    instruction_adherence: int
    rationale: str = ""

    def validate(self):
        """Ensure every quality score is between 1 and 5."""

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

    def report(self, label="Response"):
        """Generate a readable report for one response."""

        self.validate()

        return f"""
{label.upper()} QUALITY REPORT
--------------------------------
Grounding:             {self.grounding}/5
Relevance:             {self.relevance}/5
Helpfulness:           {self.helpfulness}/5
Naturalness:           {self.naturalness}/5
Instruction Adherence: {self.instruction_adherence}/5

Overall Score: {self.overall_score()}/5

Rationale:
{self.rationale}
"""


def compare_responses(response_a, response_b):
    """
    Compare two evaluated AI responses and return the preferred response.
    """

    score_a = response_a.overall_score()
    score_b = response_b.overall_score()

    print(response_a.report("Response A"))
    print(response_b.report("Response B"))

    print("SIDE-BY-SIDE RESULT")
    print("-------------------")
    print(f"Response A Overall Score: {score_a}/5")
    print(f"Response B Overall Score: {score_b}/5")

    if score_a > score_b:
        winner = "Response A"
    elif score_b > score_a:
        winner = "Response B"
    else:
        winner = "Tie"

    print(f"\nPreferred Response: {winner}")

    return winner


if __name__ == "__main__":

    response_a = Evaluation(
        grounding=5,
        relevance=5,
        helpfulness=5,
        naturalness=4,
        instruction_adherence=5,
        rationale=(
            "Response A directly addresses the user's request, "
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
            "Response B is generally relevant but introduces an "
            "unsupported assumption and does not fully satisfy the "
            "user's instruction."
        ),
    )

    compare_responses(response_a, response_b)
