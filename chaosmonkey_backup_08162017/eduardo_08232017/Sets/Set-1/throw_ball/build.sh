export IMAGE=ping_pong_throw_ball:latest
export KUBE_DTR=169.57.182.101:8500
export IMAGE_PATH=$ICP_DTR/ping-pong/$IMAGE

docker build -t $IMAGE_PATH .
docker login $KUBE_DTR
docker push $IMAGE_PATH
