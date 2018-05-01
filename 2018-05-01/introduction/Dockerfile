FROM gcr.io/distroless/python3
LABEL version="1.0"
LABEL description="Distroless Introduction"
LABEL maintainer="Andrew Latham lathama@lathama.com"
EXPOSE 8080/TCP
COPY . /srv/app
WORKDIR /srv/app
CMD ["distroless.py"]
HEALTHCHECK CMD ["/usr/bin/python3.5", "-V"]

