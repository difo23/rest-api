

## Problem #1 API REST

- Use Flask Python

- Json file like database

  

## Automatizar

```bash
   python3 -m pip install -r requirements.txt
```
```python

#!/bin/bash

source venv/bin/activate

export FLASK_APP=main.py
export FLASK_DEBUG=1

flask run
```

1. Copia el código en un nuevo archivo dentro de la raíz de tu proyecto
2. Guarda el archivo con extension .sh
3. Ejecuta desde la consola con el comando: source file_name.sh
4. Listo!, Cada vez que quieras levantar el servidor de Flask solo haz el paso 3

## Test 

### Users without payload

![image-20220108174203412](/home/digdata/.config/Typora/typora-user-images/image-20220108174203412.png)

### Userw with paytload

```bash
curl -i -H "Content-Type: application/json" -X GET -d '{"users":["Adam","Bob"]}' http://localhost:5000/users                          
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 440
Server: Werkzeug/2.0.2 Python/3.8.10
Date: Sat, 08 Jan 2022 21:42:49 GMT

{
  "users": [
    {
      "balance": 56.25, 
      "name": "Adam", 
      "owed_by": {
        "Bob": 80.0, 
        "Dan": 2.75
      }, 
      "owes": {
        "Bob": 12.0, 
        "Chuck": 4.0, 
        "Dan": 9.5
      }
    }, 
    {
      "balance": -71.5, 
      "name": "Bob", 
      "owed_by": {
        "Adam": 12.0, 
        "Dan": 2.0
      }, 
      "owes": {
        "Adam": 69.5, 
        "Chuck": 3.0
      }
    }
  ]
}
➜  ~ 


```



### Add User

```bash
curl -i -H "Content-Type: application/json" -X POST -d '{"user":"Juanita"}' http://localhost:5000/add                              
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 74
Server: Werkzeug/2.0.2 Python/3.8.10
Date: Sat, 08 Jan 2022 21:44:49 GMT

{
  "balance": 0, 
  "name": "Juanita", 
  "owed_by": {}, 
  "owes": {}
}

```



### IOU 

```bash

curl -i -H "Content-Type: application/json" -X POST -d '{"lender":"Adam", "borrower":"Bob", "amount": 5.25}' http://localhost:5000/iou
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 440
Server: Werkzeug/2.0.2 Python/3.8.10
Date: Sat, 08 Jan 2022 21:34:05 GMT

{
  "users": [
    {
      "balance": 56.25, 
      "name": "Adam", 
      "owed_by": {
        "Bob": 80.0, 
        "Dan": 2.75
      }, 
      "owes": {
        "Bob": 12.0, 
        "Chuck": 4.0, 
        "Dan": 9.5
      }
    }, 
    {
      "balance": -71.5, 
      "name": "Bob", 
      "owed_by": {
        "Adam": 12.0, 
        "Dan": 2.0
      }, 
      "owes": {
        "Adam": 69.5, 
        "Chuck": 3.0
      }
    }
  ]
}
```

