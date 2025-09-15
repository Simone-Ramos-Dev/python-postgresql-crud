from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Tarefa(Base):
    __tablename__ = 'tarefas'
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    descricao = Column(String(255), nullable=False)
    
    def __repr__(self):
        return f"<Tarefa(id={self.id}, titulo='{self.titulo}', descricao={self.descricao})>"