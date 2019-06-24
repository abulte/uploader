# Uploader

> Upload and list files with Nginx upload-module and Flask

## Quickstart

```
docker-compose up
```

Upload a file through http://localhost:8080/upload like this:

```
curl --request POST \
  --url http://localhost:8080/upload \
  --header 'content-type: multipart/form-data; boundary=---011000010111000001101001' \
  --form file=@/path/to/file \
  --form user=client \
  --form password=motdepasse \
  --form submit=submit
```

Your uploaded file should be available at http://localhost:8080/files/.
