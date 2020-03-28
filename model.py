import jwt
import uuid
import os
import datetime
from app import db, app

class UserAccount(db.Model):
	__tablename__ = 'ticket_account'
	id = db.Column(db.Integer, primary_key=True)
	basket_reference = db.Column(db.String(10), nullable=False, unique=True)
	payment_status = db.Column(db.String(10), default='Pending')
	firstname = db.Column(db.String(50), nullable=False)
	lastname = db.Column(db.String(50), nullable=False)
	email = db.Column(db.String(60), nullable=False)
	kids_tickets = db.Column(db.Integer, default=0)
	kidsTicketTotal = db.Column(db.Float, default=0)
	adult_tickets = db.Column(db.Integer, default=0)
	adultTicketTotal = db.Column(db.Float, default=0)
	total_tickets = db.Column(db.Integer, nullable=False)
	amount = db.Column(db.Float, nullable=False)
	created_on = db.Column(db.DateTime, default=datetime.datetime.now)


	def __init__(self, *args, **kwargs):
		super(UserAccount, self).__init__(*args, **kwargs)

	def save(self):
		random_string = uuid.uuid4().hex # get a random string in a UUID fromat
		basket_reference = random_string.upper()[0:9] # convert it in a uppercase letter and trim to 9 digits.
		self.basket_reference = basket_reference
		db.session.add(self)
		db.session.commit()
		return self

	def update(self):
		db.session.commit()

	def get_by_email(self, email):
		return UserAccount.query.get(email)
		
	def get_by_basket_reference(self, basket_reference):
		return UserAccount.query.filter(UserAccount.basket_reference == basket_reference).first()

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
			'basket_reference': self.basket_reference,
			'firstname': self.firstname,
            'lastname': self.lastname,
			'email': self.email,
			'kids_tickets': self.kids_tickets,
			'kidsTicketTotal': self.kidsTicketTotal,
			'adult_tickets':self.adult_tickets,
			'adultTicketTotal':self.adultTicketTotal,
			'total_tickets':self.total_tickets,
			'Payment Status': self.payment_status,
			'amount': self.amount,
			'created_on': self.created_on,
		}

