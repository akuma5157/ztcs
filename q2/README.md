# 2. Create a Dockerfile and docker-compose to run a 3 Tier application with backend api(node, python or any sample backend application), database and a nginx server. Mount volumes for persistent data for database Server.  
  a. Configure nginx to enable https  
  b. Redirect http to https  
  c. Create a self signed certificate - document how to do it.  
  d. Whitelist Ip’s  
  e. Any other important configurations  

## Dockerfile and docker-compose to run a 3 Tier application
see [Dockerfile](https://gitlab.com/akuma5157/rezotrak/-/blob/q2/python-fastapi-server/Dockerfile) and [docker-compose.yml](https://gitlab.com/akuma5157/rezotrak/-/blob/q2/docker-compose.yml) at app repo

## Configure nginx to enable https
see [nginx.conf](https://gitlab.com/akuma5157/rezotrak/-/blob/q2/nginx.conf#L29) at app repo

## Redirect http to https
see [redirection rule](https://gitlab.com/akuma5157/rezotrak/-/blob/q2/nginx.conf#L14) at app repo

## Create a self signed certificate - document how to do it.
```
openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out certificate.pem
```

## Any other important configurations
added [network isolation](https://gitlab.com/akuma5157/rezotrak/-/blob/q2/docker-compose.yml#L27) in 3-tier docker-compose.yml
