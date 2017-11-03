virtualenv:
	virtualenv -p /usr/bin/python3 .

activateenv:
	source bin/activate

deletevirtualenv:
	rm -rf share/ lib/ include/ bin/

pipinstall:
	pip install -r requirements.txt

