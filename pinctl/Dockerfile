FROM debian:bookworm-20250317

WORKDIR /usr/src/app

RUN apt update && apt install -y cmake device-tree-compiler libfdt-dev wget unzip

RUN apt-get update && apt-get install -y build-essential

RUN wget https://github.com/raspberrypi/utils/archive/refs/heads/master.zip && \
    unzip master.zip && \
    cd utils-master/pinctrl && \
    cmake . && \
    make && \
    make install && \
    cd .. && cd ..

COPY . .
RUN chmod +x example.sh

CMD [ "sleep", "infinity" ]
