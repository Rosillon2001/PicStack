from app import db
from user import User

def create_user(request):
    user = User( request.form['username'],
                 request.form['password'])
    db.session.add(user)
    db.session.commit()
    return {'message': 'user created'}