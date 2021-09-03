# [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)

**Dockerfile**
```Dockerfile
FROM golang:1.17

RUN apt update
RUN apt install -y rsyslog

WORKDIR /go/src/application
COPY . .

RUN go get -d -v ./...
RUN go install -v ./...
RUN go build

RUN service rsyslog start

CMD ["application"]
```

<br />

## Build Image

```Bash
dev@dev:~$ docker build .
Sending build context to Docker daemon 2.04kB
```

The build is run by the Docker daemon, not by the CLI. The first thing a build process does is send the entire context (recursively) to the daemon. Traditionally, the **Dockerfile** is called **Dockerfile** and located in the root of the context. You use the `-f` flag with `docker build` to point to a **Dockerfile** anywhere in your file system.

```Bash
dev@dev:~$ docker build -f /path/to/a/Dockerfile .
```

<br />

## Tagging an Image

```Bash
dev@dev:~$ docker build -t docker_id/image_name:latest .
```

<br />

## `FROM`

The `FROM` instruction initializes a new build stage and sets the Base Image for subsequent instructions.

```Dockerfile
FROM <image>:<tag>
FROM golang:1.17

FROM [--platform=<platform>] <image> [AS <name>]
FROM --platform=$BUILDPLATFORM alpine AS build

FROM [--platform=<platform>] <image>[:<tag>] [AS <name>]
FROM --platform=$BUILDPLATFORM golang:alpine AS build

FROM [--platform=<platform>] <image>[@<digest>] [AS <name>]
FROM --platform=$BUILDPLATFORM ubuntu@sha256:82becede498899ec668628e7cb0ad87b6e1c371cb8a1e597d83a47fac21d6af3 AS build
```

The `tag` or `digest` values are optional. If you omit either of them, the builder assumes a latest tag by default. The builder returns an error if it cannot find the tag value. The optional `--platform` flag can be used to specify the platform of the image in case `FROM` references a multi-platform image. For example, linux/amd64, linux/arm64, or windows/amd64. By default, the target platform of the build request is used.

<br />

## `RUN`

The `RUN` instruction will execute any commands in a new layer on top of the current image and commit the results. The resulting committed image will be used for the next step in the **Dockerfile**.

```Dockerfile
# shell form, the command is run in a shell,
# which by default is /bin/sh -c on Linux
# or cmd /S /C on Windows
RUN <command>

# exec form
RUN ["executable", "param1", "param2"]
```

The *exec* form makes it possible to avoid shell string munging, and to `RUN` commands using a base image that does not contain the specified shell executable. The default shell for the *shell* form can be changed using the `SHELL` command.

**Example**

```Dockerfile
# shell form
RUN /bin/bash -c 'source $HOME/.bashrc; echo $HOME'

# exec form
RUN ["/bin/bash", "-c", "echo hello"]
```

<br />

## `CMD`

There can only be one `CMD` instruction in a **Dockerfile**. If you list more than one `CMD` then only the last `CMD` will take effect. The **main purpose of a CMD** is to provide defaults for an executing container. These defaults can include an executable, or they can omit the executable, in which case you must specify an `ENTRYPOINT` instruction as well.

```Dockerfile
# exec form, this is the preferred form
CMD ["executable","param1","param2"]

# as default parameters to ENTRYPOINT
CMD ["param1","param2"]

# shell form
CMD command param1 param2
```

If you use the *shell form* of the `CMD`, then the `<command>` will execute in `/bin/sh -c`:

```Dockerfile
FROM ubuntu
CMD echo "This is a test." | wc -
```

If you want to run your `<command>` without a shell then you must express the command as a JSON array and give the full path to the executable. This array form is the preferred format of `CMD`. Any additional parameters must be individually expressed as strings in the array:

```Dockerfile
FROM ubuntu
CMD ["/usr/bin/wc", "--help"]
```

If you would like your container to run the same executable every time, then you should consider using ENTRYPOINT in combination with `CMD`.

<br />

## `EXPOSE`

The `EXPOSE` instruction informs Docker that the container listens on the specified network ports at runtime. You can specify whether the port listens on TCP or UDP, and the default is TCP if the protocol is not specified. The `EXPOSE` instruction does not actually publish the port. It functions as a type of documentation between the person who builds the image and the person who runs the container, about which ports are intended to be published. To actually publish the port when running the container, use the `-p` flag on `docker run` to publish and map one or more ports, or the `-P` flag to publish all exposed ports and map them to high-order ports.

```Dockerfile
EXPOSE <port> [<port>/<protocol>...]

# By default, EXPOSE assumes TCP.
# You can also specify UDP
EXPOSE 80/udp

# To expose on both TCP and UDP
EXPOSE 80/tcp
EXPOSE 80/udp
```

Regardless of the `EXPOSE` settings, you can override them at runtime by using the `-p` flag.
```Bash
dev@dev:~$ docker run -p 80:80/tcp -p 80:80/udp ...
```

<br />

## `ENV`

```Dockerfile
ENV <key>=<value> ...

ENV GO111MODULE=on
ENV GOOS="linux"
```

The `ENV` instruction sets the environment variable `<key>` to the value `<value>`. This value will be in the environment for all subsequent instructions in the build stage and can be replaced inline in many as well. The environment variables set using `ENV` will persist when a container is run from the resulting image. You can view the values using `docker inspect`, and change them using `docker run --env <key>=<value>`.

<br />

## `COPY`

The `COPY` instruction copies new files or directories from `<src>` and adds them to the filesystem of the container at the path `<dest>`. Multiple` <src>` resources may be specified but the paths of files and directories will be interpreted as relative to the source of the context of the build. The `--chown` feature is only supported on Dockerfiles used to build Linux containers, and will not work on Windows containers. The `<dest>` is an absolute path, or a path relative to `WORKDIR`, into which the source will be copied inside the destination container.

Optionally `COPY` accepts a flag `--from=<name>` that can be used to set the source location to a previous build stage (created with `FROM .. AS <name>`) that will be used instead of a build context sent by the user. In case a build stage with a specified name can’t be found an image with the same name is attempted to be used instead.

```Dockerfile
COPY [--chown=<user>:<group>] <src>... <dest>
COPY --chown=username:groupname files* /somedir/

COPY [--chown=<user>:<group>] ["<src>",... "<dest>"]

# uses a relative path, and adds file.txt”
# to <WORKDIR>/relativeDir/
COPY file.txt relativeDir/

# uses an absolute path, and adds file.txt”
# to /absoluteDir/
COPY file.txt /absoluteDir/
```

<br />

## `VOLUME`

The `VOLUME` instruction creates a mount point with the specified name and marks it as holding externally mounted volumes from native host or other containers. The value can be a JSON array,` VOLUME ["/var/log/"]`, or a plain string with multiple arguments, such as `VOLUME /var/log or VOLUME /var/log /var/db`.


```Dockerfile
VOLUME ["/data"]
```

<br />

## `WORKDIR`

The `WORKDIR` instruction sets the working directory for any `RUN`, `CMD`, `ENTRYPOINT`, `COPY` and `ADD` instructions that follow it in the **Dockerfile**. If the `WORKDIR` doesn’t exist, it will be created even if it’s not used in any subsequent **Dockerfile** instruction. The `WORKDIR` instruction can be used multiple times in a **Dockerfile**.

```Dockerfile
WORKDIR /path/to/workdir

# The WORKDIR instruction can resolve environment
# variables previously set using ENV
ENV DIRPATH=/path
WORKDIR $DIRPATH
```
