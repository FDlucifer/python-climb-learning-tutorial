from blueprintapp.app import db


class Todo(db.Model):
    __tablename__ = 'todos'

    tid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, primary_key=False)
    description = db.Column(db.String)
    done = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<tid {self.tid}, TODO {self.title}, description {self.description}, Done: {self.done}>"

    def get_id(self):
        return self.tid
