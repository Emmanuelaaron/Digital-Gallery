import jwt
import uuid
import os
import datetime
from app import db, app

class UserAccount(db.Model):
	__tablename__ = 'ticket_account'
	id = db.Column(db.Integer, primary_key=True)
	ticket_number = db.Column(db.String(10), nullable=False, unique=True)
	payment_status = db.Column(db.String(10), default='Pending')
	firstname = db.Column(db.String(50), nullable=False)
	lastname = db.Column(db.String(50), nullable=False)
	email = db.Column(db.String(60), nullable=False)
	amount = db.Column(db.Float, default=0)
	created_on = db.Column(db.DateTime, default=datetime.datetime.now)


	def __init__(self, *args, **kwargs):
		super(UserAccount, self).__init__(*args, **kwargs)

	def save(self):
		random_string = uuid.uuid4().hex # get a random string in a UUID fromat
		ticket_number  = random_string.upper()[0:9] # convert it in a uppercase letter and trim to 9 digits.
		self.ticket_number = ticket_number
		db.session.add(self)
		db.session.commit()
		return self

	def update(self):
		db.session.commit()

	def get_by_email(self, email):
		return UserAccount.query.get(email)
		
	def get_by_ticket_number(self, ticket_number):
		return UserAccount.query.filter(UserAccount.ticket_number == ticket_number).first()

	def all_users(self):
		''' Return all users in the database. '''
		for user in UserAccount.query.all():
			yield user.json()

	def by_same_email(self, email):
		# users_list = UserAccount.query.filter_by(email=email).all()
		# return users_list
		email = email.lower()
		for acc in UserAccount.query.all():
			if email in acc.email.lower():
				yield acc.json()

	# def email_exists(self, email):
	# 	''' Check whether b account with this email exists. '''
	# 	return bool(UserAccount.query.filter(UserAccount.email == email).first())

	def json(self):
		return {
			'id': self.id,
			'ticket_number': self.ticket_number,
			'firstname': self.firstname,
            'lastname': self.lastname,
			'email': self.email,
			'Payment Status': self.payment_status,
			'amount': self.amount,
			'created_on': self.created_on,
		}

