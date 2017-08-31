CONTEXT=minikube

kubectl create namespace ping-pong
kubectl config set-context $CONTEXT --user=minikube --namespace=ping-pong
