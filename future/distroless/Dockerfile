FROM gcr.io/distroless/python3
EXPOSE 8080
COPY distroless /srv/app/
COPY distroless.py /srv/app/
COPY libraries /srv/app/
COPY static /srv/app/
WORKDIR /srv/app
CMD ["distroless.py"]

