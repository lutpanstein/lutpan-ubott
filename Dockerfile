FROM mrismanaziz/man-userbot:buster

RUN git clone -b Main https://github.com/lutpanstein/lutpan-ubott /home/Main/ \
    && chmod 777 /home/Main\
    && mkdir /home/Main/bin/

WORKDIR /home/Main/

CMD [ "bash", "start" ]
