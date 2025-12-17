from modulo_oferta.Dominio_Uni.Universidad import Universidad
from modulo_oferta.Servicios_Uni.Universidad_Service import UniversidadService
from modulo_oferta.Sede import Sede
from modulo_oferta.Carrera import Carrera
from modulo_oferta.Jornada import Jornada
from modulo_oferta.OfertaAcademica import OfertaAcademica
from modulo_oferta.factories.CarreraFactory import CarreraFactory


factory = CarreraFactory()
service = UniversidadService()

u = Universidad("Universidad Laica Eloy Alfaro de Manabí")

j1 = Jornada("Matutina")
j2 = Jornada("Vespertina")

u.agregar_jornada(j1)
u.agregar_jornada(j2)

s1 = Sede("Matriz Manta", "Av. Universitaria", 500)
s2 = Sede("Extensión Chone", "Calle Bolívar", 300)

u.agregar_sede(s1)
u.agregar_sede(s2)

c1 = factory.crear_carrera(
    "ingenieria",
    "Ingeniería de Software",
    4,
    120,
    j1
)
c2 = Carrera("Medicina", 6, 80, j2)

u.agregar_carrera(c1)
u.agregar_carrera(c2)

oferta = OfertaAcademica()
oferta.agregar_carrera(c1)
oferta.agregar_carrera(c2)
oferta.agregar_sede(s1)
oferta.agregar_sede(s2)
oferta.agregar_jornada(j1)
oferta.agregar_jornada(j2)

u.asignar_oferta(oferta)

service.mostrar_universidad(u)
oferta.publicar()