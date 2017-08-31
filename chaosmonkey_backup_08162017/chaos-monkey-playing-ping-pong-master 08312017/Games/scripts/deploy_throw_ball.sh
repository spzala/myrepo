echo Deleting throw_ball job
kubectl delete job throw-ball

echo Deploying throw_ball
kubectl create -f throw_ball/src/throw_ball_job.yaml