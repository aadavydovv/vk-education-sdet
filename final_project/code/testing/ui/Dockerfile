FROM python:buster

WORKDIR /myapp_testing

COPY testing/misc/requirements_common.txt .
COPY testing/ui/misc/requirements.txt .
RUN pip3 install -r requirements_common.txt -r requirements.txt

COPY testing/misc .
COPY testing/ui .
COPY misc/constants.py misc/constants.py
COPY ui ui

CMD [ "bash", "run.sh" ]
