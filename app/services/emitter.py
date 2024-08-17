from typing import Any, List

from app.core.emitter import SocketIOEmitter


class EmitterHandler:
    def __init__(self):
        self.emitter = SocketIOEmitter()

    def send(self, payload: Any):
        pass

    def to(self, rooms: List[str]):
        self.emitter.to(rooms)
        return self
