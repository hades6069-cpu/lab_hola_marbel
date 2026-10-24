from typing import Protocol

from domain.persona import Persona


class SaludarUseCase(Protocol):
    def ejecutar(self, persona: Persona) -> str:
        ...