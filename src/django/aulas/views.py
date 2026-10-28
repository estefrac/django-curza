from datetime import date

from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template
from django.template.loader import get_template


# Create your views here.
def hello(request):
    return HttpResponse("Hola mundo!!")


def bye(request):
    return HttpResponse("Hola luego!!")


def edad(request, valor, futuro):
    try:
        anios = int(valor)
        anio_futuro = int(futuro)
    except ValueError:
        return HttpResponse("Solo acepto numeros enteros", status=400)

    incremento = anio_futuro - date.today().year
    cumplira = anios + incremento
    mensaje = f"En el {anio_futuro} cumpliras {cumplira} años"
    return HttpResponse(mensaje)


def primer_plantilla(request):
    plantilla = """
        <html>
            <body>
                <h2>
                    Hola {{ nombre }}!, esta es mi primer plantilla!
                </h2>
            </body>
        </html>
    """

    tpl = Template(plantilla)
    ctx = Context({"nombre": "Esteban Fraccascia"})
    mensaje = tpl.render(ctx)

    return HttpResponse(mensaje)


def segunda_plantilla(request):

    tpl = get_template("segunda_plantilla.html")
    mensaje = tpl.render({"nombre": "Lorena Calvo", "fecha_actual": date.today()})

    return HttpResponse(mensaje)


def tercer_plantilla(request):

    return render(
        request,
        "tercer_plantilla.html",
        {"nombre": "Martino Fraccascia", "fecha_actual": date.today()},
    )


class Empleado:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def cuarta_plantilla(request):

    empleado = Empleado(nombre="Antonela", apellido="Fraccascia")

    laborales = ["Lunes", "Martes", "Miércoles"]

    return render(
        request,
        "cuarta_plantilla.html",
        {
            "nombre": empleado.nombre + " " + empleado.apellido,
            "fecha_actual": date.today(),
            "dias_laborales": laborales,
        },
    )
