#!/bin/bash
docker build -t mypouch .
docker tag mypouch danielrustrum/mypouch
docker login
docker push danielrustrum/mypouch