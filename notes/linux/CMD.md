# Linux Command Lines


### Kill specific port
List any process listening to the port 8080:
```bash
dev@dev:~$ lsof -i:8080
```

Kill any process listening to the port 8080:
```bash
dev@dev:~$ kill $(lsof -t -i:8080)
```

Kill more violently any process listening to the port 8080:
```bash
dev@dev:~$ kill -9 $(lsof -t -i:8080)
```

`-9` implies the process will be killed forcefully.

