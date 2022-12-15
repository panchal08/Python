class Student:

    def __init__(self, enroll, name, course):
        self.enroll = enroll
        self.name = name
        self.course = course

    def display(self):
        print(self.enroll, '\t', self.name, '\t', self.course)


if __name__ == '__main__':
    Student(1101, 'Mark', 'Java').display()


