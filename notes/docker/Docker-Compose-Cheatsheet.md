# docker-compose

**docker-compose.yml**

```yaml
version: '2'

services:
  web:
    build: .
    # build from Dockerfile
    context: ./path
    dockerfile: Dockerfile
    ports:
     - "5000:5000"
    volumes:
     - .:/container_path
  redis:
    image: redis
```

### **Commands**

```bash
dev@dev:~$ docker-compose start
dev@dev:~$ docker-compose stop
dev@dev:~$ docker-compose pause
dev@dev:~$ docker-compose unpause
dev@dev:~$ docker-compose ps
dev@dev:~$ docker-compose up
dev@dev:~$ docker-compose down
```

### **Reference**

**Building**

```yaml
# Build image
web:
  # build from Dockerfile
  build: .
```

```yaml
# build from custom Dockerfile
  build:
    context: ./dir
    dockerfile: Dockerfile.dev
```

```yaml
  # build from image
  image: ubuntu
  image: ubuntu:14.04
```

**Ports**

```yaml
  ports:
    - "3000"
    - "8000:80"  # guest:host
```

```yaml
  # expose ports to linked services (not to host)
  expose: ["3000"]
```

**Commands**

```yaml
  # command to execute
  command: bundle exec thin -p 3000
  command: [bundle, exec, thin, -p, 3000]
```

```yaml
  # override the entrypoint
  entrypoint: /app/start.sh
  entrypoint: [php, -d, vendor/bin/phpunit]
```

**Environment Variables**

```yaml
  # environment variabless
  environment:
    RACK_ENV: development
  environment:
    - RACK_ENV=development
```

```yaml
  # environment vars from file
  env_file: .env
  env_file: [.env, .development.env]
```

**Dependencies**

```yaml
  # makes the `db` service available as the hostname `database`
  # (implies depends_on)
  links:
    - db:database
    - redis
```

```yaml
  # make sure `db` is alive before starting
  depends_on:
    - db
```

**DNS Servers**

```yaml
services:
  web:
    dns: 8.8.8.8
    dns:
      - 8.8.8.8
      - 8.8.4.4
```

**Devices**

```yaml
services:
  web:
    devices:
    - "/dev/ttyUSB0:/dev/ttyUSB0"
```

**Hosts**

```yaml
services:
  web:
    extra_hosts:
      - "somehost:192.168.1.100"
```