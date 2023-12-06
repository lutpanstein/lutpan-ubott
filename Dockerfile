FROM mrismanaziz/man-userbot:buster

RUN git clone -b main https://github.com/lutpanstein/lutpan-ubott /home/main/ \
    && chmod 777 /home/main\
    && mkdir /home/main/bin/

WORKDIR /home/main/

CMD [ "bash", "start" ]
