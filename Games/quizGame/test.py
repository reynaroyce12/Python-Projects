class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def enterMarks(self):
        for i in range(3):
            m = int(input(f"Enter the marks of {self.name} in subject {i + 1}: "))
            self.marks.append(m)

    def display(self):
        print(f"{self.name} got {self.marks}")


n = int(input("How many students you need to enter: "))
for i in range(n):
    user_input = input("Enter the name of the student: ")
    # creating object
    student_name = Student(user_input)
    student_name.enterMarks()
    student_name.display()
    print("\n")
