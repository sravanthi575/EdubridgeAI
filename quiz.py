from extensions import db, utcnow


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False, index=True)
    text = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.String(300), nullable=False)
    option_b = db.Column(db.String(300), nullable=False)
    option_c = db.Column(db.String(300), nullable=False)
    option_d = db.Column(db.String(300), nullable=False)
    correct = db.Column(db.String(1), nullable=False)  # "A".."D"
    explanation = db.Column(db.Text, default="")
    difficulty = db.Column(db.String(10), default="easy")  # easy / medium / hard

    @property
    def options(self):
        return [("A", self.option_a), ("B", self.option_b),
                ("C", self.option_c), ("D", self.option_d)]


class QuizAttempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    difficulty = db.Column(db.String(10), default="all")
    created_at = db.Column(db.DateTime, default=utcnow)

    @property
    def percent(self):
        return round(self.score * 100 / self.total) if self.total else 0
