# Linux Command Lines

## Kill specific port
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

## cURL
It is a command line tool that helps transfer the data from the server to the client and vice-versa using many different protocols such as HTTP, HTTPS, FTP, SFTP and more.

Installing cURL
```bash
dev@dev:~$ sudo apt install curl
```

To see the installed version
```bash
dev@dev:~$ curl --version
```

### Download file with cURL command
```bash
# HTTPS
dev@dev:~$ curl https://example.com/file.extension

# FTP
dev@dev:~$ curl ftp://ftp-domain/file.tar.gz
```

#### Download file with output name
```bash
dev@dev:~$ curl https://example.com/file.extension -o file_name.extension
```
The `o` or `--output` options allows you to give the downloaded file a different name.

#### Download multiple files using cURL
The `-O` will save the file with the name of the default website
```bash
dev@dev:~$ curl -O https://example.com/file1.extenstion \
   -O https://example.com/file2.extenstion
```

You can use the bash for loop too:
```bash
## Define bash shell variable
files = "https://example.com/file1.extension https://example.com/file2.extenstion"

for file in $files
do
   curl -O "$u"
done
```

### Getting HTTP headers information
Fetch HTTP headers without downloading the data or actual files.
```bash
dev@dev:~$ curl -I https://example.com/file.extension
```

### HTTP GET and POST Request

#### Get the body of the response
By default, `GET` is used.

```bash
dev@dev:~$ curl https://example.com/
```

#### Sending additional fields with a POST request
* `-d` send data with the POST request
* `-X` specifies a custom request method to use

```bash
dev@dev:~$ curl -d "key1=value1&key2=value2" -X POST https://example.com/login
```

#### Specifying `Content-Type` in POST request
* `-d` sending data as a JSON object
* `-H` is used to send a specific data type or header

```bash
dev@dev:~$ curl -d '{"key1": "value1", "key2": "value2"}' -H 'Content-Type: application/json' https://example.com/login
```