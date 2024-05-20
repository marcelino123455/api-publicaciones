from pydantic import BaseModel
class Item(BaseModel):
    titulo: str
    texto: str
    canti_likes: int=0
    id_usuario: int
