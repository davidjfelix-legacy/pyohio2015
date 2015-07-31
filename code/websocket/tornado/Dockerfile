FROM davidjfelix/pyohio2015

WORKDIR /opt
ENTRYPOINT ["python"]
CMD ["-m", "cProfile", "-s", "tottime", "main.py"]
COPY ./requirements.txt /opt/requirements.txt
RUN ["pip3", "install", "-r", "requirements.txt"]

COPY ./main.py /opt/main.py
