from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models import db, Semester, Subject

main = Blueprint('main', __name__)

# simple grade calculator
def get_grade(marks):
    if marks >= 85:
        return 'A', 4.0
    elif marks >= 70:
        return 'B', 3.0
    elif marks >= 55:
        return 'C', 2.0
    elif marks >= 40:
        return 'D', 1.0
    else:
        return 'F', 0.0

@main.route('/')
@login_required
def dashboard():
    semesters = Semester.query.filter_by(user_id=current_user.id).all()

    # calculate cgpa
    total_points = 0
    total_credits = 0
    for sem in semesters:
        for sub in sem.subjects:
            total_points += sub.grade_points * sub.credit_hours
            total_credits += sub.credit_hours

    cgpa = round(total_points / total_credits, 2) if total_credits > 0 else 0.0

    return render_template('dashboard.html', semesters=semesters, cgpa=cgpa)


@main.route('/add_semester', methods=['POST'])
@login_required
def add_semester():
    name = request.form['semester_name']
    semester = Semester(name=name, user_id=current_user.id)
    db.session.add(semester)
    db.session.commit()
    flash('Semester added!', 'success')
    return redirect(url_for('main.dashboard'))


@main.route('/add_subject/<int:sem_id>', methods=['POST'])
@login_required
def add_subject(sem_id):
    name = request.form['subject_name']
    credit_hours = float(request.form['credit_hours'])
    marks = float(request.form['marks'])
    grade, grade_points = get_grade(marks)

    subject = Subject(
        name=name,
        credit_hours=credit_hours,
        marks=marks,
        grade=grade,
        grade_points=grade_points,
        semester_id=sem_id
    )
    db.session.add(subject)
    db.session.commit()
    flash('Subject added!', 'success')
    return redirect(url_for('main.dashboard'))


@main.route('/delete_subject/<int:sub_id>')
@login_required
def delete_subject(sub_id):
    subject = Subject.query.get_or_404(sub_id)
    db.session.delete(subject)
    db.session.commit()
    flash('Subject deleted!', 'success')
    return redirect(url_for('main.dashboard'))


@main.route('/subjects')
@login_required
def subjects():
    semesters = Semester.query.filter_by(user_id=current_user.id).all()
    return render_template('subjects.html', semesters=semesters)


@main.route('/results')
@login_required
def results():
    semesters = Semester.query.filter_by(user_id=current_user.id).all()

    total_points = 0
    total_credits = 0
    for sem in semesters:
        for sub in sem.subjects:
            total_points += sub.grade_points * sub.credit_hours
            total_credits += sub.credit_hours

    cgpa = round(total_points / total_credits, 2) if total_credits > 0 else 0.0

    return render_template('results.html', semesters=semesters, cgpa=cgpa)