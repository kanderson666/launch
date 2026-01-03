def validate(ticket):
    if ticket.get("urgency") in range(6):
        return True
    else:
        return "Missing"
ticket1 = {
	'desc' : 'hi',
	'urgency' : 0,
}

print(validate(ticket1))