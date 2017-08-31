export IMAGE=pingpongdraft1:latest
export IMAGE_PATH=spzala/$IMAGE

docker build -t $IMAGE_PATH .
# docker login 
docker push $IMAGE_PATH
