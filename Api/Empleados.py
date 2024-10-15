import tempfile

from starlette.responses import FileResponse

from Api import aplicacion
from Datos.Datos import Datos
from Documentos.Nomina import Nomina


class Empleado:
    @aplicacion.get("/")
    def get_all():
        empleados = Datos().all_data("./resources/empleados.csv")
        return empleados

    @aplicacion.get("/recibo/{id}")
    def get_recibo(id: int):
        empleados = Datos().all_data("./resources/empleados.csv")
        nomina = Nomina()
        recibo = nomina.crear_documento(empleados[id])
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
            temp_path = tmp.name
            # Guardar el documento en el archivo temporal
            recibo.save(temp_path)

        # Devolver el archivo como respuesta
        response = FileResponse(temp_path, filename=f"download.docx",
                                media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        return response
