# ProjetoLuizaCode

Esta aplicação consiste no projeto final do Programa de Aceleração da LuizaLabs. É um CRUD feito em Python/Django com as funções de: adicionar uma empresa, adicionar produtos a esta empresa, apagar produtos desta empresa, apagar a empresa adicionada, visualizar as empresas e os produtos adicionados. Nesta aplicação, temos uma imagem Docker (disponível no docker-hub) e o deploy da aplicação em Kubernetes.

# Instalação
## Máquina Virtual
Windows:
```bash
ambiente_virtual\Scripts\activate    
ambiente_virtual\Scripts\activate.bat
```
Unix ou MacOS
```bash
source tutorial-env/bin/activate
````

## Instalação do Django

```bash
pip install django
```

## Docker
Para rodar a imagem desta aplicação com docker:
1) Inicie o docker
```bash
docker start
```
2) Rode a imagem
```bash
docker run -it -d -p 5000:8000 luizacodeimages:v1.0
```

## Kubernetes
Para rodar a aplicação com o Minikube:

1) Abra um terminal e certifique-se que está executando como administrador
```bash
minikube start
```
2) Execute o comando no terminal da sua IDE
```bash
kubectl apply -f deployment.yaml
```
3) Para analisar os pods (execute de um terminal como administrador):
````bash
minikube dashboard
````
4) Para rodar a aplicação localmente através do minikube, devemos achar o endereço de um pod:

```bash
kubectl expose deployment luiza-labs-g5 --type=NodePort
```
```bash
kubectl get svc
```
```bash
minikube service luiza-labs-g5 --url
```

## Link da imagem no Docker Hub
[Docker Hub](https://hub.docker.com/r/anastrojake/luizacodeg5)

# Contato
[Ana Strojake](https://www.linkedin.com/in/anastrojake/)

[Jane Rodrigues](https://www.linkedin.com/in/jane-rodrigues-25086a214/)

[Bruna Molina](https://www.linkedin.com/in/bruna-molina-909345144/)

[Jullie Belmonte](https://www.linkedin.com/in/julliebelmonte/)