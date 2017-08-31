echo Deleting queue chart
helm delete --purge queue

echo Deploying queue chart
helm install --name queue --set rabbitmqPassword=ping_pong stable/rabbitmq
