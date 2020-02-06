from flask import render_template, Blueprint, request, flash, redirect, url_for
from sqlalchemy.exc import IntegrityError

from app import db
from app.main.forms import SignupForm
from app.models import Course, Student

bp_main = Blueprint('main', __name__)


@bp_main.route('/')
def index():
    return render_template('index.html')


@bp_main.route('/signup/', methods=['POST', 'GET'])
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate():
        user = Student(name=form.name.data, email=form.email.data, student_ref=form.student_ref.data)
        user.set_password(form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash('You are now a registered user!')
            return redirect(url_for('main.index'))
        except IntegrityError:
            db.session.rollback()
            flash('ERROR! Unable to register {}. Please check your details are correct and resubmit'.format(form.email.data), 'error')
    return render_template('signup.html', form=form)


@bp_main.route('/courses', methods=['GET'])
def courses():
    courses = Course.query.all()
    # courses = Course.query.join(Teacher).with_entities(Course.course_code, Course.name, Teacher.name.label('teacher_name')).all()
    return render_template("courses.html", courses=courses)


@bp_main.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        term = request.form['search_term']
        if term == "":
            flash("Enter a name to search for")
            return redirect('/')
        results = Student.query.filter(Student.email.contains(term)).all()
        if not results:
            flash("No students found with that name.")
            return redirect('/')
        return render_template('search_results.html', results=results)
    else:
        return redirect(url_for('main.index'))


@bp_main.route('/student/<name>')
def show_student(name):
    user = Student.query.filter_by(name=name).first_or_404(description='There is no user {}'.format(name))
    # user = Student.query.filter_by(name=name).first_or_404()
    return render_template('show_student.html', user=user)
