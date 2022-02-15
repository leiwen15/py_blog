from flask_mail import Message
from app import mail, app
# import app

print(app.config['ADMINS'][0])
msg = Message('test subject', sender=app.config['ADMINS'][0], recipients=['1141677899@qq.com'])
msg.body = 'text body'
msg.html = '<h1>HTML body</h1>'
mail.send(msg)
