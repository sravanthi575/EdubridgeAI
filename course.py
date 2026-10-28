from extensions import db, utcnow


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(120), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, default="")
    category = db.Column(db.String(60), nullable=False, index=True)
    level = db.Column(db.String(20), default="Beginner")
    created_at = db.Column(db.DateTime, default=utcnow)

    lessons = db.relationship("Lesson", backref="course", order_by="Lesson.position",
                              cascade="all, delete-orphan")
    questions = db.relationship("Question", backref="course", cascade="all, delete-orphan")
    enrollments = db.relationship("Enrollment", backref="course", cascade="all, delete-orphan")
    attempts = db.relationship("QuizAttempt", backref="course", cascade="all, delete-orphan")


class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False, index=True)
    position = db.Column(db.Integer, default=1)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, default="")  # trusted HTML written by admins
    minutes = db.Column(db.Integer, default=20)

    progress_entries = db.relationship("LessonProgress", backref="lesson",
                                       cascade="all, delete-orphan")


class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=utcnow)
    __table_args__ = (db.UniqueConstraint("user_id", "course_id"),)
