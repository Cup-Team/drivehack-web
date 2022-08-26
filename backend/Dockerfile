FROM python:3.10

WORKDIR /code

COPY requirements.txt .

RUN pip install -U pip wheel setuptools && pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

RUN ["python", "-m", "spacy", "download", "en_core_web_sm"]

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
