Oauth testing app by instructions from https://medium.com/@ratrosy/building-a-basic-authorization-server-with-implicit-flow-3f474eb2a306

Making public and private keys:
```
openssl genrsa -out private.pem 2048

openssl rsa -in private.pem -pubout -outform PEM -out public.pem
```