from main import *

account = Account(200)

def test_getAmount():
	assert account.getAmount() == 200


def test_deposit():
	account.deposit(300)
	assert account.getAmount() == 500

def test_withdraw():
	account.withDraw(100)
	assert account.getAmount() == 400


