class Account:
	def __init__(self, amount):
		self.amount = amount

	def getAmount(self):
		return self.amount

	def deposit(self, amount):
		self.amount = self.amount + amount

	def withDraw(self, amount):
		self.amount = self.amount - amount


account = Account(200)
print(account.getAmount())
