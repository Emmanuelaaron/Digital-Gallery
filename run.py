
from flask import Blueprint, jsonify, request, make_response
from flask_cors import cross_origin
from datetime import datetime
from model import UserAccount
''' Main entry to the application. '''
from app import app


@app.route('/')
def index():
	return jsonify({ 'default': 'Welcome to Chena Art Gallery Home page' })

@app.route('/ticket', methods=['GET', 'POST'])
def get_ticket():
	contents = request.json
	firstname, lastname, email = contents['firstname'], contents['lastname'], contents['email']
	kids_tickets, phone = int(contents['kids_tickets']), int(contents['phone'])
	adult_tickets = int(contents['adult_tickets'])
	event_date = datetime(year = 2020, month = 7, day = 4)
		
	if datetime.now() < event_date:

		if kids_tickets != 0:
			kidsTicketTotal = kids_tickets * 30
		else:
			kidsTicketTotal = 0

		if adult_tickets != 0:
			adultTicketTotal = adult_tickets * 80
		else:
			adultTicketTotal = 0

	else:

		if kids_tickets != 0:
			kidsTicketTotal = kids_tickets * 50
		else:
			kidsTicketTotal = 0

		if adult_tickets != 0:
			adultTicketTotal = adult_tickets * 100
		else:
			adultTicketTotal = 0

	total_tickets = kids_tickets + adult_tickets

	amount = kidsTicketTotal + adultTicketTotal
	# print("Derek ", event_date)
	# print(datetime.now())
	# if UserAccount().phone_exists(phone):
	# 	return jsonify({ 'phone_inuse': True })
	user_details = UserAccount(
		firstname=firstname,
		lastname=lastname,
		email=email,
		phone=phone,
		kids_tickets=kids_tickets,
		kidsTicketTotal=kidsTicketTotal,
		adult_tickets=adult_tickets,
		adultTicketTotal=adultTicketTotal, 
		total_tickets=total_tickets,
		amount=amount).save()
	
	return jsonify({ 
		'success': True,
		'user_details': user_details.json() })

@app.route('/confirm', methods=['POST'])
def confirm_payment():
	# try:
	contents = request.json
	basket_reference = contents['basket_reference']
	main_user = UserAccount().get_by_basket_reference(basket_reference)
	if main_user:
		main_user.payment_status = "Paid"
		main_user.update()
		return jsonify({"success":main_user.json()})
	return jsonify({"Error":"Ticket Basket reference doesnt exist"})

@app.route('/check_reference', methods=['POST'])
def confirm_reference():
	# try:
	contents = request.json
	basket_reference = contents['basket_reference']
	main_user = UserAccount().get_by_basket_reference(basket_reference)
	if main_user:
		return jsonify({"success":main_user.json()})
	return jsonify({"Error":"Ticket Basket reference doesnt exist"})

@app.route('/check_email', methods=['POST'])
def check_email():
	# try:
	contents = request.json
	email = contents['email']
	main_user = UserAccount().get_by_email(email)
	if main_user:
		return jsonify({"success":main_user.json()})
	return jsonify({"Error":"Email doesnt exist"})


@app.errorhandler(404)
def page_not_found(e):
	""" Error handler route bad requests."""
	return jsonify({
		'status': 404,
		'data': [
			{
				'Issue': "You have entered an unknown URL.",
				'message': 'Please contact kidricederek@gmail.com for more details on this.'
			}]
	}), 404

@app.errorhandler(405)
def method_not_allowed(e):
	""" This is a route handler for wrong methods."""

	return jsonify({
		"status": 405,
		"error": "The used method is not allowed for this endpoint. Change method or contact kidricederek@gmail.com."
	}), 405

@app.route('/users')
def users():
	users = list(UserAccount().all_users())
	return jsonify({ 'users': users })


@app.route('/search_email', methods=['GET', 'POST'])
def search_account():
	key = request.json['key']
	if not key:
		return jsonify({ 'results': [] })
	results = list(UserAccount().filter_by_email(key))
	return jsonify({ 'results': results })


if __name__ == '__main__':
	app.run(host='0.0.0.0')
