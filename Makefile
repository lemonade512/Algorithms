.PHONY: test quicktest

test:
	nosetests -v -w tests/Python

quicktest:
	nosetests -w tests/Python
