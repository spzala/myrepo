echo Deleting commentator Replica Set
kubectl delete rs commentator

echo Deploying commentator Replica Set
kubectl create -f commentator/src/commentator_rset.yaml