# test_oferta.py
from Jornadas import Jornada
from factories import CarreraFactory, SedeFactory
from Universidad import Universidad
from OfertaAcademica import OfertaAcademica

# 1️⃣ Universidad
uni = Universidad("Universidad Laica Eloy Alfaro de Manabí")

# 2️⃣ Jornadas
j1 = Jornada("Matutina")
j2 = Jornada("Vespertina")
uni.agregar_jornada(j1)
uni.agregar_jornada(j2)

# 3️⃣ Sedes usando Factory
s1 = SedeFactory.crear_sede("matriz", "Matriz Manta", "Av. Principal 123", 500)
s2 = SedeFactory.crear_sede("extension", "Extensión Chone", "Calle Secundaria 45", 200)
uni.agregar_sede(s1)
uni.agregar_sede(s2)

# 4️⃣ Carreras usando Factory
c1 = CarreraFactory.crear_carrera("ingenieria", "Ingeniería de Software", 5, 50, j1)
c2 = CarreraFactory.crear_carrera("salud", "Medicina", 6, 40, j2)
uni.agregar_carrera(c1)
uni.agregar_carrera(c2)

# 5️⃣ Oferta Académica
oferta = OfertaAcademica()
oferta.agregar_carrera(c1)
oferta.agregar_carrera(c2)
oferta.agregar_sede(s1)
oferta.agregar_sede(s2)
oferta.agregar_jornada(j1)
oferta.agregar_jornada(j2)

oferta.publicar()
uni.asignar_oferta_academica(oferta)

# 6️⃣ Mostrar Universidad
uni.mostrar_info()