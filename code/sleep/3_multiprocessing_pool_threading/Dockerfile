FROM davidjfelix/pyohio2015

COPY ./main.py /opt/main.py
WORKDIR /opt

ENTRYPOINT ["python"]
CMD ["-m", "cProfile", "-s", "tottime", "main.py"]
