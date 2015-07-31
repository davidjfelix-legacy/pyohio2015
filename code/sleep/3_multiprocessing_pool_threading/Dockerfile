FROM davidjfelix/pyohio2015

ENTRYPOINT ["python"]
CMD ["-m", "cProfile", "-s", "tottime", "main.py"]
WORKDIR /opt

COPY ./main.py /opt/main.py
