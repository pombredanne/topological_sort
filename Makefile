PYTHON=python

run:
	$(PYTHON) tsort.py example.txt

test:
	$(PYTHON) -m unittest discover

build:
	$(PYTHON) setup.py build

install:
	$(PYTHON) setup.py install

clean:
	rm -rf *~ *.py[oc] __pycache__ build dist
