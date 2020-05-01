#!/bin/sh
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
#heroku plugins:install heroku-container-registry
docker login --username=$DOCKER_USER --password=$(heroku auth:token) registry.heroku.com
heroku container:push web --app $HEROKU_APP_NAME
heroku container:release web --app $HEROKU_APP_NAME
