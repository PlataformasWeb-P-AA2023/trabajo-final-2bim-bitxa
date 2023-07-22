## Guía para Desplegar un Proyecto Django con Nginx y Gunicorn en Ubuntu

### Requisitos Previos

- Una máquina virtual con una versión de Ubuntu LTS.
- Conexión a Internet para instalar los paquetes y herramientas necesarias.

### Paso 1: Instalar y Configurar el Entorno de Django

1. Actualizar los paquetes del sistema:

   ```bash
   sudo apt update
   ```

2. Instalar Python y pip:

   ```bash
   sudo apt install python3 python3-pip
   ```

3. Crear un entorno virtual para el proyecto:

   ```bash
   python3 -m venv myenv
   ```

4. Activar el entorno virtual:

   ```bash
   source myenv/bin/activate
   ```

5. Instalar Django y Gunicorn:

   ```bash
   pip install django gunicorn
   ```

6. Configurar y migrar la base de datos de Django:
   ```bash
   cd /ruta/proyecto/django
   python manage.py makemigrations
   python manage.py migrate
   ```

### Paso 2: Probar el Servidor de Desarrollo de Django

1. Iniciar el servidor de desarrollo de Django:
   ```bash
   python manage.py runserver
   ```

### Paso 3: Configurar Nginx como Servidor Web

1. Instalar Nginx:

   ```bash
   sudo apt install nginx
   ```

2. Crear un archivo de configuración para el proyecto:

   ```nginx
   sudo nano /etc/nginx/sites-available/proyecto_django
   ```

3. Copiar y pegar la siguiente configuración en el archivo, ajustando las rutas y dominios según sea necesario:

   ```nginx
   #user  nobody;
   worker_processes  1;

   #error_log logs/error.log;
   #error_log logs/error.log notice;
   #error_log logs/error.log info;

   #pid logs/nginx.pid;

   events {
   worker_connections 1024;
   }

   http {
   include mime.types;
   default_type application/octet-stream;

       sendfile        on;
       keepalive_timeout  65;

       server {
           listen       80;
           server_name  localhost;

           location / {
               proxy_pass http://localhost:8000;
               proxy_set_header Host $host;
               proxy_set_header X-Real-IP $remote_addr;
               proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           }

           location /static/ {
               alias ~/Developer/DesarolloWeb/bimestre2/trabajo-final-2bim-bitxa/proyecto-django/project/app/static/;
           }

           error_page   500 502 503 504  /50x.html;
           location = /50x.html {
               root   html;
           }
       }

       include servers/*;
   }

   ```

4. Crear un enlace simbólico para habilitar el sitio:
   ```bash
   sudo ln -s /etc/nginx/sites-available/proyecto_django /etc/nginx/sites-enabled/
   ```

5. Verificar la configuración de Nginx:

   ```bash
   sudo nginx -t
   ```

6. Reiniciar Nginx para aplicar los cambios:
   ```bash
   sudo service nginx restart
   ```

### Paso 4: Configurar Gunicorn

1. Crear un archivo de servicio para Gunicorn:

   ```bash
   sudo nano /etc/systemd/system/gunicorn.service
   ```

2. Agregar el siguiente contenido al archivo, ajustando las rutas según sea necesario:

   ```plaintext
   [Unit]
   Description=Daemon Gunicorn
   After=network.target

   [Service]
   User=tu_usuario
   Group=www-data
   WorkingDirectory=/ruta/proyecto/django
   ExecStart=/ruta/a/entorno_virtual/bin/gunicorn tu_proyecto_django.wsgi:application --bind 127.0.0.1:8000

   [Install]
   WantedBy=multi-user.target
   ```

3. Iniciar el servicio de Gunicorn:

   ```bash
   sudo systemctl start gunicorn
   ```

4. Habilitar el servicio para que se inicie en el arranque:
   ```bash
   sudo systemctl enable gunicorn
   ```

### Paso 5: Acceder al Proyecto Django a Través de Nginx

1. Accediendo a la dirección IP: `http://localhost:80`.
   Se debería ver proyecto Django cargado correctamente a través de Nginx.

