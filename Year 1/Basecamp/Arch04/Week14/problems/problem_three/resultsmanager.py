import os
import sys
import sqlite3

from result import Result
from student import Student
from course import Course


# noinspection SpellCheckingInspection
class ResultsManager:
    def __init__(self):
        self.conn = sqlite3.connect(os.path.join(
            sys.path[0], 'studentresults.db'))
        self.dbc = self.conn.cursor()

    def create_tables(self):
        self.dbc.execute('''CREATE TABLE IF NOT EXISTS courses
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          name TEXT NOT NULL,
                          points INTEGER NOT NULL);''')

        self.dbc.execute('''CREATE TABLE IF NOT EXISTS students
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          first_name TEXT NOT NULL,
                          last_name TEXT NOT NULL,
                          date_of_birth DATE NOT NULL,
                          class_code TEXT NULL);''')

        self.dbc.execute('''CREATE TABLE IF NOT EXISTS results
                         (student_id INTEGER NOT NULL,
                          course_id INTEGER NOT NULL,
                          mark INTEGER NOT NULL,
                          achieved DATE NOT NULL,
                          PRIMARY KEY(student_id, course_id, mark));''')

        self.conn.commit()

    def get_course(self, course_id):
        self.conn = sqlite3.connect(os.path.join(sys.path[0], 'studentresults.db'))
        self.dbc = self.conn.cursor()
        course = self.dbc.execute("SELECT * FROM courses WHERE id=?", [course_id]).fetchone()
        if course is None:
            self.conn.commit()
            self.conn.close()
            return None
        else:
            self.conn.commit()
            self.conn.close()
            return Course(course[1], course[2], course[0])

    def add_course(self, course: Course):
        self.conn = sqlite3.connect(os.path.join(sys.path[0], 'studentresults.db'))
        self.dbc = self.conn.cursor()
        self.dbc.execute("INSERT INTO courses (name, points) VALUES (?,?)", [course.name, course.points])
        self.conn.commit()

        get_updated_course = self.dbc.execute("SELECT * FROM courses WHERE name=?", [course.name])
        course_class = Course(course.name, course.points, get_updated_course.lastrowid)

        self.conn.close()
        return course_class

    def get_student(self, student_id):
        self.conn = sqlite3.connect(os.path.join(sys.path[0], 'studentresults.db'))
        self.dbc = self.conn.cursor()
        student = self.dbc.execute("SELECT * FROM students WHERE id=?", [student_id]).fetchone()
        if student is None:
            self.conn.commit()
            self.conn.close()
            return None
        else:
            self.conn.commit()
            self.conn.close()
            return Student(student[1], student[2], student[3], student[4], student[0])

    def add_student(self, student: Student) -> Student:
        self.conn = sqlite3.connect(os.path.join(sys.path[0], 'studentresults.db'))
        self.dbc = self.conn.cursor()
        self.dbc.execute("""INSERT INTO students (first_name, last_name, date_of_birth, class_code)
                         VALUES (?,?,?,?)""",
                         [student.first_name, student.last_name,
                          student.date_of_birth, student.class_code])

        self.conn.commit()

        get_updated_student = self.dbc.execute("SELECT * FROM students WHERE first_name=?", [student.first_name])
        student_class = Student(student.first_name, student.last_name,
                                student.date_of_birth, student.class_code, get_updated_student.lastrowid)

        self.conn.close()
        return student_class

    def add_result(self, result: Result) -> bool:
        self.conn = sqlite3.connect(os.path.join(sys.path[0], 'studentresults.db'))
        self.dbc = self.conn.cursor()

        get_previous_result = self.dbc.execute("""SELECT * FROM results 
        WHERE student_id=? AND course_id=?
        
        """,[result.student_id, result.course_id]).fetchall()

        insert_new_result = """INSERT INTO results (student_id, course_id, mark, achieved)
        VALUES (?,?,?,?)"""

        if len(get_previous_result) == 0 or get_previous_result[0][2] < result.mark:
            self.dbc.execute(insert_new_result, [result.student_id, result.course_id,
                                                 result.mark, result.achieved])
            self.conn.commit()
            self.conn.close()
            return True
        elif get_previous_result[0][2] >= result.mark or get_previous_result[0][2] == result.mark:
            return False

    def get_results_by_student(self, student_id, only_last=True):
        self.conn = sqlite3.connect(os.path.join(sys.path[0], 'studentresults.db'))
        self.dbc = self.conn.cursor()
        get_all_results = self.dbc.execute("SELECT * FROM results WHERE student_id=?", [student_id])
        if only_last:
            try:
                get_all_results = get_all_results.fetchall()[-1]
                self.conn.commit()
                self.conn.close()
                return [get_all_results]
            except IndexError:
                self.conn.commit()
                self.conn.close()
                return []
        else:
            get_all_results = get_all_results.fetchall()
            self.conn.commit()
            self.conn.close()
            return [get_all_results]

    def get_results_by_course(self, course_id, only_last=True):
        self.conn = sqlite3.connect(os.path.join(sys.path[0], 'studentresults.db'))
        self.dbc = self.conn.cursor()
        get_all_results = self.dbc.execute("SELECT * FROM results WHERE course_id=?", [course_id])
        if only_last:
            try:
                get_all_results = get_all_results.fetchall()[-1]
                self.conn.commit()
                self.conn.close()
                return [get_all_results]
            except IndexError:
                self.conn.commit()
                self.conn.close()
                return []
        else:
            get_all_results = get_all_results.fetchall()
            self.conn.commit()
            self.conn.close()
            return [get_all_results]

    def close(self):
        self.conn.close()
