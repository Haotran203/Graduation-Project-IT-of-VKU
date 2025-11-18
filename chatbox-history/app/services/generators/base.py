# app/services/generators/base.py
from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseGenerator(ABC):
    @abstractmethod
    def generate(self, prompt: str, system: str = None) -> Dict[str, Any]:
        pass