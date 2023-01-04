FROM python:3.10-slim
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes gcc g++ libpython3-dev libpq-dev && \
    python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r requirements.txt
COPY . /code/

ENV VIRTUAL_ENV /venv
ENV PATH /venv/bin:$PATH

EXPOSE 8000

#ENTRYPOINT ["gunicorn"]
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "BE_CS300.wsgi:application"]
