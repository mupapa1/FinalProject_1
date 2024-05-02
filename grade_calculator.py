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
