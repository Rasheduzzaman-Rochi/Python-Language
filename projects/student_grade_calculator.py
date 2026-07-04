class Student():
    def __init__(self, name, marks, attendence):
        self.name = name
        self.marks = marks
        self.attendence = attendence

    def calculate_avg(self):
        avg = sum(self.marks) / len(self.marks)
        return avg

    def display_student(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

    def check_grade(self):
        avg_mark = self.calculate_avg()
        if avg_mark > 80:
            grade = "A"
        elif avg_mark > 60 and avg_mark < 80:
            grade = "B"
        else:
            grade = "C"
        return grade

    def predict_future_grade(self):
        import random
        return random.choice(["A", "B", "C"])
    

s1 = Student("Sadia", [10, 20], 90)

print(s1.marks)
print(s1.name)
print(s1.attendence)