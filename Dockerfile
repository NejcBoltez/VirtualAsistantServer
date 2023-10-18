FROM scratch
RUN apt-get update && apt-get upgrade
COPY . .

CMD [ "python3 server.py" ]

EXPOSE 1234
