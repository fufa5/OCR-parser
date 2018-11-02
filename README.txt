
Invocation (Docker):
1) $ docker pull python:3.7
2) Navigate to OCR directory
3) docker build -t ocr-app .
4) $  docker run -it --rm --name ocr-app-container -v "$PWD":/usr/src/app -w /usr/src/app python:3.7 python business_card_parser.py

Invocation (Command line, assuming Python 3.7 is installed):
1) Navigate to OCR/venv/bin directory
2) $ source ./venv/bin/activate
3) $ python business_card_parser.py

Run unit tests (Docker):
1) Navigate to OCR directory
2)  docker run -it --rm --name ocr-app-container -v "$PWD":/usr/src/app -w /usr/src/app python:3.7 python -m unittest -v test.parser_tests

Run unit tests (command line):
1) Navigate to OCR directory
2) $ python -m unittest -v test.parser_tests
3) $ python -m unittest -v test.contact_info_tests
