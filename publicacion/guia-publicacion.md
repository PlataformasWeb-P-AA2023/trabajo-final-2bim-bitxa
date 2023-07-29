## Desplegando un proyecto en Django con Nginx y Gunicorn en MacOS

### Requisitos Previos

- Un sistema Mac.
- Homebrew instalado.
- Python3 y pip.

### Paso 1: Configuración del entorno Django

1. Primero instalé Gunicorn usando pip: `pip install gunicorn`.
2. Mi proyecto Django ya estaba creado y configurado.

### Paso 2: Instalación y Configuración de Nginx

1. Luego instalé Nginx utilizando Homebrew: `brew install nginx`.
2. Navegué hasta el directorio principal de Nginx: `cd /opt/homebrew/etc/nginx/`.
3. Abrí el archivo `nginx.conf` usando mi editor de texto preferido: `nano nginx.conf`.
4. Pegué la siguiente configuración en el archivo `nginx.conf`:

```nginx
user  sebastian;
worker_processes  1;

events {
    worker_connections  1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;

    sendfile        on;
    keepalive_timeout  65;

    include /opt/homebrew/etc/nginx/servers/*;

    server {
        listen      80 default_server;
        server_name _;
        return      444;
    }
}
```

5. Navegué hasta el directorio de servidores de Nginx: `cd servers/`.
6. Creé un nuevo archivo de configuración para mi proyecto llamado proyecto-django: `touch proyecto-django`.
7. Abrí `proyecto-django` con el editor de texto: `nano proyecto-django`.
8. Pegué la siguiente configuración en el archivo, ajustando las rutas según sea necesario:

```nginx
server {
    listen 80;
    server_name localhost;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
        alias /Users/sebastian/Developer/DesarolloWeb/bimestre2/trabajo-final-2bim-bitxa/proyecto-django/project/static/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/tmp/gunicorn.sock;
    }
}
```

### Paso 3: Lanzamiento del Proyecto Django con Gunicorn

1. Fui al directorio de mi proyecto Django e inicié Gunicorn: `cd /Users/sebastian/Developer/DesarolloWeb/bimestre2/trabajo-final-2bim-bitxa/proyecto-django/project`
2. Inicié el proyecto de django con gunicorn:

   `gunicorn project.wsgi:application --bind unix:/tmp/gunicorn.sock --workers 3`
