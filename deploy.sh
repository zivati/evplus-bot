
#!/bin/bash

# Substitua pelo seu usuário no Docker Hub
DOCKER_USER=harthurfraga
REPO_NAME=ev-bot

echo "🔧 Buildando imagem..."
docker build -t $DOCKER_USER/$REPO_NAME:latest .

echo "🔐 Logando no Docker Hub..."
docker login

echo "📤 Publicando imagem..."
docker push $DOCKER_USER/$REPO_NAME:latest

echo "✅ Deploy concluído!"
