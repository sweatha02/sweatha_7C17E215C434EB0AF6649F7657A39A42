class student:
  def __init__(self,name,roll_number,cpga):
    self.name=name
    self.roll_number=roll_number
    self.cpga=cpga

def sort_students(student_list):
  sorted_students=sorted(student_list,key= lambda student: student.cpga, reverse=True)
  return sorted_students

students=[student("hari","A123",7.5),student("srikanth","A124",8.5),student("sowsiya","A125",6.9),student("mahi","A126",9.1)]

sorted_students=sort_students(students)

for student in sorted_students:
  print("name:{},roll number:{},cpga:{}".format(student.name,student.roll_number,student.cpga))