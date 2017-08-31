echo Scaling ping Pod
kubectl scale -f ping_pong/deploy/ping.yaml --replicas=2