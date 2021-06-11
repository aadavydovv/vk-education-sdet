FROM python:buster

WORKDIR /myapp_testing

COPY testing/misc/requirements_common.txt .
COPY testing/api/misc/requirements.txt .
RUN pip3 install -r requirements_common.txt -r requirements.txt

COPY testing/misc .
COPY testing/api .
COPY misc/constants.py misc/constants.py
COPY myapp_api myapp_api
COPY mysql mysql

CMD [ "bash", "run.sh" ]
