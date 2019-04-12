FROM ubuntu:latest

#* Dependencies
    # Python 3 / Pip
    RUN apt-get update \
    && apt-get install -y python3-pip python3-dev \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python \
    && pip3 install --upgrade pip

    # Cherrypy
    RUN pip3 install cherrypy
    RUN pip3 install pyrebase

#* Copy Current Directory
    COPY . .

#* Expose Port
    EXPOSE 8080

#* Run Executable
    CMD ["./run.sh"]

