class Grade:

    def __init__(self, gradePoint, letterGrade, weight, courseCode) -> None:
        self.gradePoint = gradePoint
        self.letterGrade = letterGrade
        self.weight = weight
        self.courseCode = courseCode
    
    def getGradePoint(self):
        return self.gradePoint
    
    def getLetterGrade(self):
        return self.letterGrade
    
    def getWeight(self):
        return self.weight

    def getCourseCode(self):
        return self.courseCode