FROM python:3.8.4-slim as base

RUN pip install pytz

WORKDIR /src

COPY . ./

FROM base as debugger

RUN pip install debugpy

ENTRYPOINT ["python","-m","debugpy","--listen","0.0.0.0:5678","--wait-for-client","-m"]

FROM base as primary 

ENTRYPOINT ["python","-m"]


