"""Fills an empty database with starter courses, quizzes and scholarship links."""
from datetime import date  # noqa: F401  (handy if you want to add last_verified dates)

from data.seed_data import COURSES, SCHOLARSHIPS
from extensions import db
from models import Course, Lesson, Question, Scholarship


def seed_content():
    if Course.query.count() == 0:
        for c in COURSES:
            course = Course(slug=c["slug"], title=c["title"], category=c["category"],
                            level=c["level"], description=c["description"])
            for pos, (title, content, minutes) in enumerate(c["lessons"], start=1):
                course.lessons.append(Lesson(position=pos, title=title, content=content, minutes=minutes))
            for q in c["questions"]:
                text, a, b, cc, d, correct, why, diff = q
                course.questions.append(Question(text=text, option_a=a, option_b=b, option_c=cc,
                                                 option_d=d, correct=correct, explanation=why,
                                                 difficulty=diff))
            db.session.add(course)
    if Scholarship.query.count() == 0:
        for s in SCHOLARSHIPS:
            db.session.add(Scholarship(**s))  # last_verified stays empty until an admin verifies it
    db.session.commit()
