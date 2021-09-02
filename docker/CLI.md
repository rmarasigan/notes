# [Command Line Reference](https://docs.docker.com/engine/reference/run/)

## `docker run`
Run a command in a new container. The `docker run` command first creates a writeable container layer over the specified image, and then starts it using the specified command.
```
dev@dev-PC:~$ docker run [OPTIONS] IMAGE[:TAG|@DIGEST] [COMMAND] [ARG...]
```

**Example**
```
dev@dev-PC:~$ docker run hello-world
Unable to find image ‘hello-world:latest’ locally
latest: Pulling from library/hello-world
b8dfe127a29: Pull complete
Digest: sha256:9f6ad537c5132bcce57f7a0a20e317228d382c3cd61edae14650eec68b2b345c
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.
```

### `docker run` = `docker create` + `docker start`
The `docker create` command is used to create a container out of an image. `docker start` is used to actually start an image.

```
dev@dev-PC:~$ docker create hello-world
71830b72c406c28acc2908549d42fe10b8c558ce08b28a2ba642129249383481
dev@dev-PC:~$ docker start -a 71830b72c406c28acc2908549d42fe10b8c558ce08b28a2ba642129249383481
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
...........
```

The `-a` specifically means, watch for output coming from it and print it out. `docker run` is going to show you all the information coming out of the container by default. `docker start` is not going to show you information coming out of the terminal.

**Additional detailed information**
* [Docker run reference](https://docs.docker.com/engine/reference/run/)

<br />

## `docker ps`
List containers.
```
dev@dev-PC:~$ docker ps [OPTIONS]
```

**Options**

Shorthand   |       |       | Description                                            |
----------- | ----- | ----- | ------------------------------------------------------ |
`--all`     | `-a`  |       | Show all containers                                    |
`--filter`  | `-f`  |       | Filter output based on conditions provided             |
`--last`    | `-n`  | `-1`  | Show n last created containers (includes all states)   |
`--latest`  | `-l`  |       | Show the latest created container (includes all states)|
`--quiet`   | `-q`  |       | Only display container IDs                             |
`--size`    | `-s`  |       | Display total file sizes                               |

<br />

## `docker start`
Start one or more stopped containers
```
dev@dev-PC:~$ docker start [OPTIONS] CONTAINER [CONTAINER...]

dev@dev-PC:~$ docker start my_container
```

**Options**

Shorthand           |       | Description                                         |
------------------- | ----- | --------------------------------------------------- |
`--attach`          | `-a`  | Attach STDOUT/STDERR and forward signals            |
`--detach-keys`     |       | Override the key sequence for detaching a container |
`--interactive`     | `-i`  | Attach container's STDIN                            |

<br />

## `docker system prune`
Remove unused data. Removed all unused containers, networks, images (both dangling and unreferenced) and optionally volumes. This is not only going to delete stopped containers, it's going to delete a couple of either items as well. Most notable, your `build cache`. The `build cache` is any image that you have fetch from **Docker Hub**. So after running the `docker system prune`, you'll have to re-download images from Docker.
```
dev@dev-PC:~$ docker system prune [OPTIONS]

dev@dev-PC:~$ docker system prune
WARNING! This will remove:
	- all stopped containers
	- all networks not used by at least one container
	- all dangling images
	- all build cache
Are you sure you want to continue? [y/N] y
Deleted Containers:
37a8c45a23e150b0818847ddea988c2de7769f2f8ef262082a69b3cd5c0e799c
88a49c62dd857d8d7b1854c03e0bb60c196921d4111d038389257ad3972a6c72
```

**Options**

Shorthand   |       | Description                                            |
----------- | ----- | ------------------------------------------------------ |
`--all`     | `-a`  | Remove all unused images not just dangling ones        |
`--filter`  |       | Provide filter values (e.g. `label=<key>=<value>`)     |
`--force`   | `-f`  | Do not prompt for confirmation                         |
`--volumes` |       | Prune volumes                                          |

<br />

## `docker logs`
Fetch the logs of a container. The `docker logs` command batch-retrieves logs present at the time of execution.
```
dev@dev-PC:~$ docker logs [OPTIONS] CONTAINER

dev@dev-PC:~$ docker logs my_container
```

**Options**

Shorthand      |       |       | Description                                                                                 |
-------------- | ----- | ----- | ------------------------------------------------------------------------------------------- |
`--details`    |       |       | Show extra details provided to logs                                                         |
`--follow`     | `-f`  |       | Follow log output                                                                           |
`--since`      |       |       | Show logs since timestamp (e.g. 2013-01-02T13:23:37Z) or relative (e.g. 42m for 42 minutes) |
`--tail`       | `-n`  | `all` | Number of lines to show from the end of the logs                                            |
`--timestamps` | `-t`  |       | Show timestamps                                                                             |

<br />

## `docker stop`
Stop one or more running containers. The main process inside the container will receive `SIGTERM`, and after a grace period, `SIGKILL`. The first signal can be changed with the `STOPSIGNAL` instruction in the container’s Dockerfile, or the `--stop-signal` option to `docker run`.

When you issue `docker stop` commands, a hardware signal is sent to the process, the primary process inside that container. In the case of `docker stop`, we send a `SIGTERM` message which is short for `terminate signal`. It's the message that's going to be received by the process, telling it essentially to shutdown on its own time.

`SIGTERM` is used any time that you want to stop a process inside of your container and shut the container down and you want to give that process inside there a little bit of time to shut itself down and do a little cleanup. And as soon as you get that signal, you could attempt to do a little bit of cleanup or maybe save some file or emit some message or something like that. When you issued `docker stop` to a container, if the container does not automatically stop in 10 seconds, then docker is going to automatically fall back to issuing the `docker kill` command.
```
dev@dev-PC:~$ docker stop [OPTIONS] CONTAINER [CONTAINER...]

dev@dev-PC:~$ docker stop my_container
```

**Options**

Shorthand    |       | Description                                                 |
------------ | ----- | ----------------------------------------------------------- |
`--time`     | `-t`  | Seconds to wait for stop before killing it. Default is `10` |

<br />

## `docker kill`
Kill one or more running containers. The `docker kill` subcommand kills one or more containers. The main process inside the container is sent `SIGKILL` signal (default), or the signal that is specified with the `--signal` option. You can kill a container using the container’s ID, ID-prefix, or name.

The `docker kill` command issues a `SIGKILL` or a `kill signal` to the primary running process inside the container. `SIGKILL` essentially means you have to shut down right now and you do not get to do any additional work. So ideally, we always stop a container with the `docker stop` command in order to give the running process inside of it a little bit more time to shut itself down. Otherwise, if it feels like the container has locked up and it's not responding to the `docker stop`, then we could issue `docker kill` instead.
```
dev@dev-PC:~$ docker kill [OPTIONS] CONTAINER [CONTAINER...]

dev@dev-PC:~$ docker kill my_container
```

**Options**

Shorthand      |       | Description                                         |
-------------- | ----- | --------------------------------------------------- |
`--signal`     | `-s`  | Signal to send to the container. Default is `KILL`  |

<br />

## `docker exec`
Run a command in a running container. The `docker exec` command runs a new command in a running container. The command started using `docker exec` only runs while the container's primary process (`PID 1`) is running and it is not restarted if the container is restarted.
```
dev@dev-PC:~$ docker exec [OPTIONS] CONTAINER COMMAND [ARG...]

dev@dev-PC:~$ docker exec -it my_container <command>
```
`-it` allows us to type input directly into the container. We provide the `my_container` and `command` that we want to execute inside of the container.

**Options**

Shorthand        |       | Description                                                  |
---------------- | ----- | ------------------------------------------------------------ |
`--detach `      | `-d`  | Detached mode: run command in the background                 |
`--detach-keys`  |       | Override the key sequence for detaching a container          |
`--env`          | `-e`  | Set environment variables                                    |
`--env-file`     |       | Read in a file of environment variables                      |
`--interactive`  | `-i`  | Keep STDIN open even if not attached                         |
`--privileged`   |       | Give extended privileges to the command                      |
`--tty`          | `-t`  | Allocate a pseudo-TTY                                        |
`--user`         | `-u`  | Username or UID (format: `<name|uid>[:<group|gid>]`)         |
`--workdir`      | `-w`  | Working directory inside the container                       |

**The Purpose of IT Flag**

When you are running docker on your machine, every single container that you are running is running inside of a virtual machine running Linux. So these processes are really being executed inside of a Linux world even if you're on Mac or Windows. The `-it` is actually two separate flags but by convention we usually just kind of shorten it down to be simply `-it` which is 100% equivalent to the two separate flags. The `-i` on here means when we execute this new command inside the container, we want to attach our terminal to the standard input channel of that new running process. The `-t` flag is to make sure that all the text that you are entering in and that is coming out shows up in a nicely formatted manner on your screen.

<br />

## `docker images`
List images. The default `docker images` will show all top level images, their repository and tags, and their size. Docker images have intermediate layers that increase reusability, decrease disk usage, and speed up `docker build` by allowing each step to be cached. These intermediate layers are not shown by default. The `SIZE` is the cumulative space taken up by the image and all its parent images. This is also the disk space used by the contents of the Tar file created when you docker save an image.
```
dev@dev-PC:~$ docker images [OPTIONS] [REPOSITORY[:TAG]]

dev@dev-PC:~$ docker images
```

**Options**

Shorthand        |       | Description                                              |
---------------- | ----- | -------------------------------------------------------- |
`--all `         | `-a`  | Show all images (default hides intermediate images)      |
`--digests`      |       | Show digests                                             |
`--filter`       | `-f`  | Filter output based on conditions provided               |
`--format`       |       | Pretty-print images using a Go template                  |
`--no-trunc`     |       | Don't truncate output                                    |
`--quiet`        | `-q`  | Only show image IDs                                      |


<br />

## `docker rmi`
Remove one or more images. Removes (and un-tags) one or more images from the host node. If an image has multiple tags, using this command with the tag as a parameter only removes the tag. If the tag is the only one for the image, both the image and the tag are removed.
```
dev@dev-PC:~$ docker rmi [OPTIONS] IMAGE [IMAGE...]

dev@dev-PC:~$ docker rmi --force $(docker images -a -q)
```

**Options**

Shorthand        |       | Description                                |
---------------- | ----- | ------------------------------------------ |
`--force `       | `-f`  | Force removal of the image                 |
`--no-prune`     |       | Do not delete untagged parents             |

<br />

## `docker volume ls`
List volumes. List all the volumes known to Docker. You can filter using the `-f` or `--filter` flag.
```
dev@dev-PC:~$ docker volume ls [OPTIONS]

dev@dev-PC:~$ docker volume ls
```

**Options**

Shorthand        |       | Description                                   |
---------------- | ----- | --------------------------------------------- |
`--filter `      | `-f`  | Provide filter values (e.g. `dangling=true`)  |
`--format`       |       | Pretty-print volumes using a Go template      |
`--quiet`        | `-q`  | Only display volume names                     |


<br />

## `docker volume prune`
Remove all unused local volumes. Unused local volumes are those which are not referenced by any containers.
```
dev@dev-PC:~$ docker volume prune [OPTIONS]

dev@dev-PC:~$ docker volume prune
```

**Options**

Shorthand        |       | Description                                  |
---------------- | ----- | -------------------------------------------- |
`--force `       | `-f`  | Do not prompt for confirmation               |
`--filter`       |       | Provide filter values (e.g. `label=<label>`) |