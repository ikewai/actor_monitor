FROM debian:stable

WORKDIR /usr/src/app

## Get OS-side dependencies ##
RUN apt update
RUN apt install python3 python3-pip -y

## Get python-side dependencies ##
# Update pip to prevent issue with installing tapipy
RUN pip3 install --upgrade pip
RUN pip3 install tapipy

COPY ./scripts/monitor.py scripts/.

CMD [ "/bin/python3", "/usr/src/app/scripts/monitor.py"]