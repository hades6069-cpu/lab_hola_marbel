from domain.persona import Persona


class SaludarService:
    def ejecutar(self, persona: Persona) -> str:
        return f'hola {persona.nombre.lower()}'