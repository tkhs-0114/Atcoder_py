FROM python:3.10

RUN echo 'export PS1="\[\e[1;31m\]\u@\h\[\e[m\]:\[\e[1;34m\]/\W\[\e[m\]$ "' >> /etc/bash.bashrc

COPY ./../lib/run /usr/bin/run
COPY ./../lib/start /usr/bin/start

RUN chmod 777 /usr/bin/run && \
    chmod 777 /usr/bin/start

ARG ID=1000
ARG NAME=CODER

RUN groupadd -g $ID $ID && \
    useradd -m -u $ID -g $ID $NAME
USER $NAME

WORKDIR /usr/src/code

RUN echo 'PS1="\[\e[1;31m\]\u@\h\[\e[m\]:\[\e[1;34m\]/\W\[\e[m\]$ "' >> /home/CODER/.bashrc