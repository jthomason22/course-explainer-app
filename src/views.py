from flask import render_template
from models import courses

def index():
    return render_template('index.html', courses=courses)

def course(course_id):
    course = courses[int(course_id) - 1]
    return render_template('course.html', course=course)