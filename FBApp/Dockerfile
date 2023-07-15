FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /code

#COPY /my_app/prices_store.json .
COPY /prices_store.json .

#сopying NN data
COPY /my_model_text .

#copying learning data for RNN
COPY /ALL_TEXT_VARIANTS .

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3", "manage.py", "runserver"]