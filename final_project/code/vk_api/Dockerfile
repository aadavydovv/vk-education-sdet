FROM python:buster

WORKDIR /app

COPY vk_api/requirements.txt .
RUN pip3 install -r requirements.txt

COPY vk_api .
COPY misc/constants.py misc/constants.py
COPY mysql mysql

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=1337"]
