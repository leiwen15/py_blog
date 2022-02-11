from app import db
from app.models import User, Post

u = User(username='john', email='john@example.com')
# db.session.add(u)
# db.session.commit()
users = User.query.all()

# print(users)
for u in users:
    db.session.delete(u)
db.session.commit()
