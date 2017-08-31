kubectl delete rs pong

echo Deleting pong Pod
kubectl delete pod pong

echo Waiting for pong to die
while [ ! -z "`kubectl get po | grep pong`" ]
do
	sleep 1
done

echo Deploying pong Pod
kubectl create -f ping_pong/src/pong.yaml