class UniversidadService:
    """
    Servicio de aplicación para coordinar operaciones
    relacionadas con la Universidad
    """

    def mostrar_universidad(self, universidad):
        print("\n📘 Universidad:", universidad.nombre)

        print("Sedes:")
        for sede in universidad.listar_sedes():
            print(" -", sede.nombre)

        print("Carreras:")
        for carrera in universidad.listar_carreras():
            print(" -", carrera.nombre)

        print("Jornadas:")
        for jornada in universidad.listar_jornadas():
            print(" -", jornada.tipo)
