#!/bin/bash#
alias k=kubectl
k apply -f deployment.yml
k apply -f service.yml
k apply -f nginx-exporter.yml
k apply -f rbac.yml
k apply -f servicemonitor.yml
k apply -f prometheus.yml