FROM debian:bookworm-20250317

WORKDIR /usr/src/app

RUN apt update && apt install -y python3 python3-pip

RUN pip3 install lgpio rpi-lgpio --break-system-packages

COPY . .

CMD [ "sleep", "infinity" ]
