docker pull danielrustrum/mypouch:latest
docker run --name mypouch --network="host" -d -p 8080:8080 danielrustrum/mypouch:latest