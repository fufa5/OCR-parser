Clone the github image
----------------------

git clone https://github.com/fufa5/OCR-parser.git

Using Docker
------------

Invocation:
1) $ docker pull python:3.7
2) Navigate to OCR-parser directory
3) docker build -t ocr-app .
4) $  docker run -it --rm --name ocr-app-container -v "$PWD":/usr/src/app -w /usr/src/app python:3.7 python business_card_parser.py

Run unit tests:
1) Navigate to OCR-parser directory
2) docker run -it --rm --name ocr-app-container -v "$PWD":/usr/src/app -w /usr/src/app python:3.7 python -m unittest -v test.parser_tests
3) docker run -it --rm --name ocr-app-container -v "$PWD":/usr/src/app -w /usr/src/app python:3.7 python -m unittest -v test.contact_info_tests


Command Line
------------

Invocation (assuming Python 3.7 is installed):
1) Navigate to OCR-parser directory
2) $ python business_card_parser.py

Run unit tests:
1) Navigate to OCR-parser directory
2) $ python -m unittest -v test.parser_tests
3) $ python -m unittest -v test.contact_info_tests
