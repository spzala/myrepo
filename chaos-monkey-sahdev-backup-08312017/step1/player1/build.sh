export IMAGE=ping_pong_throw_ball:latest
export IMAGE_PATH=spzala/$IMAGE

docker build -t $IMAGE_PATH .
docker login 
docker push $IMAGE_PATH
