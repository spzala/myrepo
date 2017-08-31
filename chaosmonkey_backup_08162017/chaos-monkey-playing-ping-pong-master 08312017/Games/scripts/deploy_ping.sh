kubectl delete rs ping

destroy_ping.sh

echo Waiting for ping to die
while [ ! -z "`kubectl get po | grep ping`" ]
do
	sleep 1
done

echo Deploying ping Pod
kubectl create -f ping_pong/src/ping.yaml