# from typing import List, Tuple
#
# class GradeCalculator:
#     def __init__(self, scores: List[int]):
#         self.scores = scores
#
#     def calculate_grade(self, score: int, best: int) -> str:
#         if score >= best - 10:
#             return 'A'
#         elif score >= best - 20:
#             return 'B'
#         elif score >= best - 30:
#             return 'C'
#         elif score >= best - 40:
#             return 'D'
#         else:
#             return 'F'
#
#     def get_best_score(self) -> int:
#         return max(self.scores)
#
#     def get_average_score(self) -> float:
#         return sum(self.scores) / len(self.scores)
#
#     def get_grades(self, best_score: int) -> List[Tuple[int, str]]:
#         return [(score, self.calculate_grade(score, best_score)) for score in self.scores]
class GradeCalculator:
    def __init__(self, scores):
        self.scores = scores

    def get_best_score(self):
        """Return the highest score."""
        return max(self.scores)

    def get_average_score(self):
        """Return the average score."""
        return sum(self.scores) / len(self.scores)

    def get_grades(self, best_score):
        """Return grades based on the best score."""
        grades = []
        for score in self.scores:
            if score >= best_score - 10:
                grade = 'A'
            elif score >= best_score - 20:
                grade = 'B'
            elif score >= best_score - 30:
                grade = 'C'
            elif score >= best_score - 40:
                grade = 'D'
            else:
                grade = 'F'
            grades.append((score, grade))
        return grades
