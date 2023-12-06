FROM mrismanaziz/man-userbot:buster

RUN git clone -b Main https://github.com/lutpanstein/lutpan-ubott /home/man-userbot/ \
    && chmod 777 /home/lutpan-ubott \
    && mkdir /home/lutpan-ubott/bin/

WORKDIR /home/lutpan-ubott/

CMD [ "bash", "start" ]
