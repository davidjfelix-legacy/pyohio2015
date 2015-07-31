FROM davidjfelix/pyohio2015

WORKDIR /opt
ENTRYPOINT ["python"]
CMD ["-m", "cProfile", "-s", "tottime", "main.py"]

COPY ./main.py /opt/main.py
