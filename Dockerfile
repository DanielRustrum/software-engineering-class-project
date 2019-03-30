From ubuntu:latest

#* Dependencies
    # Python 3 / Pip
    RUN apt-get update \
    && apt-get install -y python3-pip python3-dev \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python \
    && pip3 install --upgrade pip

    # Cherrypy
    RUN pip3 install cherrypy

#* Run Executable
    RUN ./run.sh