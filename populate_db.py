from app import db
from app.models import Student, Teacher, Course, Grade


def populate_db():
    """Populates the cscourses.db database if it is empty. The Flask app needs to be running before you execute this code.

    :return: None
    """

    if not Student.query.first():
        s1 = Student(student_ref="CS1234567", name="Ahmet Roth", email='cs1234567@ucl.co.uk', password='test1pass')
        s2 = Student(student_ref="CS1234568", name="Elsie-Rose Kent", email="cs1234568@ucl.co.uk", password="test2pass")
        s3 = Student(student_ref="CS1234569", name="Willem Bull", email="cs1234569@ucl.co.uk", password="test3pass")
        s4 = Student(student_ref="CS1234570", name="Jago Curtis", email="cs1234570@ucl.co.uk", password="test4pass")
        s5 = Student(student_ref="CS1234571", name="Mateusz Bauer", email="cs1234571@ucl.co.uk", password="test5pass")
        s6 = Student(student_ref="CS1234572", name="Morwenna Shepherd", email="cs1234572@ucl.co.uk", password="test6pass")

        t1 = Teacher(teacher_ref="uclcs0002", title="Dr", name="Lewis Baird")
        t2 = Teacher(teacher_ref="uclcs0006", title="Prof", name="Elif Munro")
        t3 = Teacher(teacher_ref="uclcs0010", title="Ms", name="Aleyna Bonilla")
        t4 = Teacher(teacher_ref="uclcs0072", title="Dr", name="Maximus Tierney")
        t5 = Teacher(teacher_ref="uclcs0021", title="Dr", name="Marcelina McClure")
        t6 = Teacher(teacher_ref="uclcs0132", title="Dr", name="Fei Hong Zhou")

        c1 = Course(course_code="COMP0015", name="Introduction to Programming")
        c2 = Course(course_code="COMP0034", name="Software Engineering")
        c3 = Course(course_code="COMP0035", name="Web Development")
        c4 = Course(course_code="COMP0070", name="Algorithmics")
        c5 = Course(course_code="COMP0068", name="Architecture and Hardware")
        c6 = Course(course_code="COMP0022", name="Database and Information Management Systems")
        c7 = Course(course_code="COMP0067", name="Design")
        c8 = Course(course_code="COMP0066", name="Introductory Programming")
        c9 = Course(course_code="COMP0039", name="Entrepreneurship: Theory and Practice")
        c10 = Course(course_code="COMP0020", name="Functional Programming")
        c11 = Course(course_code="COMP0021", name="Interaction Design")
        c12 = Course(course_code="COMP0142", name="Machine Learning for Domain Specialists")
        c13 = Course(course_code="COMP0142", name="Software Engineering")

        g1 = Grade(grade="B-")
        g2 = Grade(grade="C")
        g3 = Grade(grade="B+")
        g4 = Grade(grade="A+")
        g5 = Grade(grade="A+")
        g6 = Grade(grade="D+")
        g7 = Grade(grade="B")
        g8 = Grade(grade="D-")

        s1.grades.append(g1)
        s1.grades.append(g5)
        s2.grades.append(g2)
        s2.grades.append(g6)
        s3.grades.append(g3)
        s3.grades.append(g7)
        s4.grades.append(g4)
        s4.grades.append(g8)

        c1.grades.append(g1)
        c1.grades.append(g2)
        c1.grades.append(g3)
        c1.grades.append(g4)
        c2.grades.append(g5)
        c2.grades.append(g6)
        c2.grades.append(g7)
        c2.grades.append(g8)

        t1.courses.append(c1)
        t2.courses.append(c2)
        t3.courses.append(c3)
        t4.courses.append(c4)
        t5.courses.append(c5)
        t6.courses.append(c6)
        t6.courses.append(c7)
        t6.courses.append(c8)
        t1.courses.append(c9)
        t2.courses.append(c10)
        t3.courses.append(c11)
        t5.courses.append(c12)
        t5.courses.append(c13)

        db.session.add_all([s1, s2, s3, s4, s5, s6])
        db.session.add_all([t1, t2, t3, t4, t5, t6])
        db.session.commit()
