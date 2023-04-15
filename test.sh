#!/bin/bash


export DNS=$(aws elbv2 describe-load-balancers  --query LoadBalancers[*].DNSName --output text) 

echo ${DNS}

URL="http://${DNS}"

echo ${URL} 