class Student:

  def __init__(self, name, r_no, cgpa):
    self.name = name
    self.r_no = r_no
    self.cgpa = cgpa


def sort_students(student_list):
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


students = [
    Student("Has", "Emuc105", 8.7),
    Student("Nami", "Emuc101", 8.6),
    Student("Afi", "Emuc103", 7.5),
]
sorted_students = sort_students(students)
for student in sorted_students:
  print("Name: {}, Roll_no: {}, CGPA: {}".format(student.name, student.r_no,
                                                 student.cgpa))
