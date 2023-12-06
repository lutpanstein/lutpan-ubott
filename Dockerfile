FROM lutpanstein/lutpan-ubott:buster

RUN git clone -b lutpan-ubott https://github.com/lutpanstein/lutpan-ubott /home/lutpan-ubott/ \
    && chmod 777 /home/lutpan-ubott \
    && mkdir /home/lutpan-ubott/bin/

WORKDIR /home/lutpan-ubott/

CMD [ "bash", "start" ]
