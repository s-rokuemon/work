FROM apache/airflow:2.10.0

USER root
RUN echo 'airflow ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
RUN apt update -y && apt upgrade -y
RUN apt-get install git -y
RUN apt-get install vim -y
RUN apt-get install --no-install-recommends -y -q \
    git libpq-dev python3-dev build-essential && \ 
    apt-get clean

USER airflow


RUN pip install --upgrade pip && \
    pip install dbt-core==1.7.3 && \
    pip install airflow-dbt && \
    pip install dbt-snowflake==1.7.3 && \
    pip install python-certifi-win32

ENV PYTHONIOENCODING=utf-8
ENV LANG C.UTF-8