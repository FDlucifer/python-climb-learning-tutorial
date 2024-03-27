from blueprintapp.app import db


class Person(db.Model):
    __tablename__ = 'people'

    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, primary_key=False)
    age = db.Column(db.Integer)
    job = db.Column(db.String)

    def __repr__(self):
        return f"<pid {self.pid}, PERSON {self.name}, AGE: {self.age}>, job: {self.job}>"

    def get_id(self):
        return self.tid
