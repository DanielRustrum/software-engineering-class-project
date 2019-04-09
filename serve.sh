#!/bin/bash
docker build -t mypouch .
docker run --name mypouch --network="host" -d -p 8080:8080 mypouch