wrk -c 5 -t 5 -d 300s -H "Connection: Close" http://stress-test-service:8000/stress
wrk -c 100 -t 100 -d 300s -H "Connection: Close" http://stress-test-service:8000/get
# install metrics server
wget -O metrics-server.yaml https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml