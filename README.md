# Flask Microservices on Kubernetes

This project demonstrates a microservices architecture using Flask and PostgreSQL, deployed on Kubernetes. It consists of two microservices and a shared PostgreSQL database.

## Architecture

- **user**: Handles users.
- **data**: fetches user data.
- **PostgreSQL Database**: Central database used by both microservices.

## Prerequisites

- Docker
- Kubernetes (minikube, k3s or k8s)
- kubectl

## Setup and Installation

minikube start

Note: Before deploying, create Docker images for the user and data microservices, tag them appropriately, and push them to your registry. Update the image tags in user-deployment.yaml and data-deployment.yaml accordingly.

docker build -t yourregistry/user-service:v1 ./path/to/user/Dockerfile
docker build -t yourregistry/data-service:v1 ./path/to/data/Dockerfile

docker push yourregistry/user-service:v1
docker push yourregistry/data-service:v1

Deploy PostgreSQL using the provided Kubernetes manifests. Note that the PostgreSQL image will be pulled from the public Docker registry by Kubernetes:

kubectl apply -f postgres-configmap.yaml
kubectl apply -f postgres-deployment.yaml
kubectl apply -f postgres-service.yaml

Note: Currently, environment variables like database credentials are set using ConfigMaps. For better security in production environments, it's advisable to use Kubernetes Secrets to handle sensitive data.

kubectl create secret generic db-credentials --from-literal=username=dbuser --from-literal=password=dbpass

Update your deployment configurations to use values from secrets instead of ConfigMaps.

# REQUIRED ENV variables on runtime (already set in configmap)
#DB_USER
#DB_PASS
#DB_HOST
#DB_PORT
#DB_NAME

kubectl apply -f user-service-configmap.yaml
kubectl apply -f user-deployment.yaml
kubectl apply -f user-svc.yaml

kubectl apply -f data-service-configmap.yaml
kubectl apply -f data-deployment.yaml
kubectl apply -f data-svc.yaml

kubectl get all -A

### use < minikube ip > : port to access the services. if minikube ip not working use kubectl port-forward svc/svc_name port:port

access both the services ( user and data ) on Node's ipaddress with ports 8082 and 8081 respectively.

apis are listed on homepage

note 3: using binary of pycopg2 as its for development pursposes not production. psycopg2-binary