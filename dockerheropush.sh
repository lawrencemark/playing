#!/bin/bash
docker build -f Dockerfile.web . -t $TAG 
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
heroku plugins:install @heroku-cli/plugin-container-registry
docker login --username $DOCKERUSER --password $DOCKERPASSWORD
docker login --username _ --password=$HEROKU_API_KEY registry.heroku.com
docker tag $TAG registry.heroku.com/$HEROKU_APP_NAME/web
heroku container:push web --app $HEROKU_APP_NAME
heroku container:release web --app $HEROKU_APP_NAME