# Importaciones necesarias
from Documentos.Nomina import Nomina
from Datos.Datos import Datos
from Api.Empleados import Empleado
from Api import aplicacion
import uvicorn

# Método principal

if __name__ == '__main__':
    #datos = Datos()
    #empleados = datos.all_data('./resources/empleados.csv')
    #nomina = Nomina()
    #nomina.crear_documento(empleados[1])
    uvicorn.run(aplicacion, port=8080, host='localhost')


# git init
# git checkout -b main
# git add .
# git commmit -m "ft Funcion crear documento"
