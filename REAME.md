

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
