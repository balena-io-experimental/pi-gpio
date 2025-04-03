FROM debian:bookworm-20250317

WORKDIR /usr/src/app

RUN apt update && apt install -y gpiod


COPY . .

RUN chmod +x example.sh

CMD [ "sleep", "infinity" ]
