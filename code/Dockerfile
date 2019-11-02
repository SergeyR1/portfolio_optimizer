FROM python:3.7

EXPOSE 8000
RUN apt-get update && apt-get -yqq install unzip libaio-dev

ENV LD_LIBRARY_PATH=/opt/oracle/instantclient
ENV ORACLE_HOME=/opt/oracle/instantclient
ENV OCI_LIB=/opt/oracle/instantclient
ENV OCI_LIB_DIR=/opt/oracle/instantclient
ENV OCI_INCLUDE_DIR=/opt/oracle/instantclient/sdk/include

RUN pip install -U pip
RUN pip install sanic motor cx_Oracle requests

ADD oracle-instantclient /opt
ADD install_oracle.sh /opt
RUN sh /opt/install_oracle.sh

RUN mkdir code
COPY utils /code/utils
ADD app.py /code
ADD blueprints.py /code
ADD service_v2.py /code
WORKDIR /code

CMD python app.py
