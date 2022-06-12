# Docker CLI CheatSheet

### Container Management Commands

Command                                | Description                                   |
-------------------------------------- | --------------------------------------------- |
`docker create image [command]`        | Create container                              |
`docker run image [command]`           | = `create` + `start`                          |
`docker start [container]`             | Start the container                           |
`docker stop [container`               | Graceful stop                                 |
`docker kill [container]`              | Kill (`SIGKILL`) the container                |
`docker restart [container]`           | = `stop` + `start`                            |
`docker pause [container]`             | Suspend the container                         |
`docker unpause [container]`           | Resume the container                          |
`docker rm [-f] [container]`           | Destroy the container                         |

**NOTE:**

**`-f`** allows removing running containers (`docker kill` + `docker rm`)

### Inspecting the Container

Command                                | Description                                           |
-------------------------------------- | ----------------------------------------------------- |
`docker ps`                            | List running containers                               |
`docker ps -a`                         | List all containers                                   |
`docker logs [-f] [container]`         | Show the container output (`stdout` + `stderr`)       |
`docker top [container`                | List the process running inside the containers        |
`docker diff [container]`              | Show the differences with the image (modified files)  |
`docker inspect [container]`           | Show low-level infos (in json format)                 |

### Interacting with the Container

Command                                  | Description                                                    |
---------------------------------------- | -------------------------------------------------------------- |
`docker attach container`                | Attach to a running container (`stdin` / `stdout` / `stderr`)  |
`docker cp container:path hostpath`      | Copy files from the container                                  |
`docker cp hostpath container:path`      | Copy files into container                                      |
`docker export container`                | Export the content of the container (tar archive)              |
`docker exec container args...`          | Run a command in an existing container (useful for debugging)  |
`docker wait container`                  | Wait until the container terminates and return the exit code   |
`docker commit container image`          | Commit a new docker image (snapshot of the container)          |

### Image Management Commands

Command                                  | Description                                                    |
---------------------------------------- | -------------------------------------------------------------- |
`docker images`                          | List all local images                                          |
`docker history image`                   | Show the image history                                         |
`docker inspect image`                   | Show low-level infos (json format)                             |
`docker tag image tag`                   | Tag an image                                                   |
`docker commit container image`          | Create an image (from a container)                             |
`docker rmi image`                       | Delete images                                                  |

### Build & Run

**Create an image from a Dockerfile**

```bash
dev@dev:~$ docker build -t "app/container_name" .
```

**Run a command in an image**

```bash
dev@dev:~$ docker run "app/container_name" .
```

### Lifecycle Commands

**Create a container (without starting it)**

```bash
docker create [options] IMAGE
  -a, --attach               # attach stdout/err
  -i, --interactive          # attach stdin (interactive)
  -t, --tty                  # pseudo-tty
      --name NAME            # name your image
  -p, --publish 5000:5000    # port map
      --expose 5432          # expose a port to linked containers
  -P, --publish-all          # publish all ports
      --link container:alias # linking
  -v, --volume `pwd`:/app    # mount (absolute paths needed)
  -e, --env NAME=hello       # env vars

dev@dev:~$ docker create --name app_redis_1 \
          --expose 6379 \
          redis:3.0.2
```

**Rename an existing container**

```bash
dev@dev:~$ docker rename [CONTAINER_NAME] [NEW_CONTAINER_NAME]
```

**Run a command in a new container**

```bash
dev@dev:~$ docker run [IMAGE] [COMMAND]
```

**Remove container after it exits**

```bash
dev@dev:~$ docker run --rm [IMAGE]
```

**Start a container and keep it running**

```bash
dev@dev:~$ docker run -td [IMAGE]
```

**Start a container and creates an interactive bash shell in the container**

```bash
dev@dev:~$ docker run -it [IMAGE]
```

**Create, Start, and run a command inside the container and remove the container after executing command.**

```bash
dev@dev:~$ docker run -it-rm [IMAGE]
```

**Execute command inside already running container.**

```bash
docker exec [options] CONTAINER COMMAND
  -d, --detach        # run in background
  -i, --interactive   # stdin
  -t, --tty           # interactive

dev@dev:~$ docker exec -it [CONTAINER]
dev@dev:~$ docker exec [CONTAINER] tail logs/development.log
```

**Delete a container (if it is not running)**

```bash
dev@dev:~$ docker rm [CONTAINER]
```

**Update the configuration of the container**

```bash
dev@dev:~$ docker update [CONTAINER]
```

### Starting and Stopping Containers

**Start Container**

```bash
docker start [options] CONTAINER
  -a, --attach        # attach stdout/err
  -i, --interactive   # attach stdin

dev@dev:~$ docker start [CONTAINER]
```

**Stop running Container**

```bash
dev@dev:~$ docker stop [options] CONTAINER
```

**Stop running Container and start it again**

```bash
dev@dev:~$ docker restart [CONTAINER]
```

**Pause processes in a running container**

```bash
dev@dev:~$ docker pause [CONTAINER]
```

**Unpause processes in a running container**

```bash
dev@dev:~$ docker unpause [CONTAINER]
```

**Block a container until others stop**

```bash
dev@dev:~$ docker wait [CONTAINER]
```

**Kill a container by sending a SIGKILL to a running container**

```bash
dev@dev:~$ docker kill [CONTAINER]
```

**Attach local standard input, output, and error streams to a running container**

```bash
dev@dev:~$ docker attach [CONTAINER]
```

### Docker Image Commands

**Create an image from a Dockerfile**

```bash
dev@dev:~$ docker build [URL/FILE]
```

**Create an image from a Dockerfile with Tags**

```bash
dev@dev:~$ docker build -t <tag> [URL/FILE]
```

**Pull an image from a registry**

```bash
dev@dev:~$ docker pull [IMAGE]
```

**Push an image to a registry**

```bash
dev@dev:~$ docker push [IMAGE]
```

**Create an image from a tarball**

```bash
dev@dev:~$ docker import [URL/FILE]
```

**Create an image from a container**

```bash
dev@dev:~$ docker commit [CONTAINER] [NEW_IMAGE_NAME]
```

**Remove an image**

```bash
dev@dev:~$ docker rmi [IMAGE]
```

**Save an image to a tar archive**

```bash
dev@dev:~$ docker load [TAR_FILE/STDIN_FILE]
```

**Load an image from a tar archive or stdin**

```bash
dev@dev:~$ docker save [IMAGE] > [TAR_FILE]
```

### Docker Container And Image Information

**List running containers**

```bash
dev@dev:~$ docker ps
```

**Lists both running containers and ones that have stopped**

```bash
dev@dev:~$ docker ps -a
```

**List the logs from a running container**

```bash
dev@dev:~$ docker logs [CONTAINER]
```

**List low-level information on Docker objects**

```bash
dev@dev:~$ docker inspect [OBJECT_NAME/ID]
```

**List real-time events from a container**

```bash
dev@dev:~$ docker events [CONTAINER]
```

**Show port mapping for a container**

```bash
dev@dev:~$ docker port [CONTAINER]
```

**Show running processes in a container**

```bash
dev@dev:~$ docker top [CONTAINER]
```

**Show live resource usage statistics of container**

```bash
dev@dev:~$ docker stats [CONTAINER]
```

**Show changes to files (or directories) on a filesystem**

```bash
dev@dev:~$ docker diff [CONTAINER]
```

**List all images that are locally stored with the docker engine**

```bash
dev@dev:~$ docker [image] ls
dev@dev:~$ docker images -a           # also show intermediate
```

**Show the history of an image**

```bash
dev@dev:~$ docker history [IMAGE]
```

### Network Commands

**List networks**

```bash
dev@dev:~$ docker network ls
```

**Remove one or more networks**

```bash
dev@dev:~$ docker network rm [NETWORK]
```

**Show information on one or more networks**

```bash
dev@dev:~$ docker network inspect [NETWORK]
```

**Connects a container to a network**

```bash
dev@dev:~$ docker network connect [NETWORK] [CONTAINER]
```

**Disconnect a container from a network**

```bash
dev@dev:~$ docker network disconnect [NETWORK] [CONTAINER]
```

### Services

```bash
dev@dev:~$ docker service ls                                      # view list of all the services runnning in swarm
dev@dev:~$ docker stack services stack_name                       # see all running services
dev@dev:~$ docker service logs stack_name service_name            # see all services logs
dev@dev:~$ docker service scale stack_name_service_name=replicas  # scale services quickly across qualified node
```

### Clean up

```bash
dev@dev:~$ docker image prune              # clean or prune unused (dangling) images
dev@dev:~$ docker image prune -a           # remove all images which are not in use containers , add - a
dev@dev:~$ docker system prune             # prune your entire system
dev@dev:~$ docker swarm leave              # leave swarm
dev@dev:~$ docker stack rm stack_name      # remove swarm ( deletes all volume data and database info)
dev@dev:~$ docker kill $(docker ps -q)     # kill all running containers
```

## **Reference**

* [Docker Cheatsheet](https://dockerlabs.collabnix.com/docker/cheatsheet/)
* [wsargent/docker-cheat-sheet](https://github.com/wsargent/docker-cheat-sheet)
* [Docker commands that you should know](https://vishnuch.tech/docker-cheatsheet)