install:
	pip3 install -r requirements.txt && pip3 install flask


test:
	pytest test.py
