FROM python:3.6-stretch AS build-env
COPY requirements.txt /
RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements.txt

FROM gcr.io/distroless/python3
LABEL version="1.2"
LABEL description="Distroless Introduction"
LABEL maintainer="Andrew Latham lathama@lathama.com"
EXPOSE 8080/TCP
COPY . /srv/app
COPY --from=build-env /usr/local/lib/python3.6/site-packages /site-packages
ENV PYTHONPATH=/site-packages
WORKDIR /srv/app
CMD ["distroless.py"]
HEALTHCHECK CMD ["/usr/bin/python3.5", "-V"]

