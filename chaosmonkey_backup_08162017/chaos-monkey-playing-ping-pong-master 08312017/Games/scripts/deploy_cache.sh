CHART_NAME=redis
APP_NAME=cache

echo Deleting $CHART_NAME chart
helm delete --purge $APP_NAME

echo Deploying $CHART_NAME chart
helm install --name $APP_NAME --set redisPassword=ping_pong stable/$CHART_NAME
