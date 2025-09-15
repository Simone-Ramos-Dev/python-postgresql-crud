from flask import Flask, request, jsonify
from database import SessionLocal
from models import Tarefa

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)
# Criar uma sessão nova a cada request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota inicial (teste)
@app.route("/")
def home():
    return {"message": "API de Tarefas funcionando 🚀"}

# Criar tarefa
@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    data = request.get_json()
    titulo = data.get("titulo")
    descricao = data.get("descricao")

    db = next(get_db())
    tarefa = Tarefa(titulo=titulo, descricao=descricao)
    db.add(tarefa)
    db.commit()
    db.refresh(tarefa)
    return jsonify({"id": tarefa.id, "titulo": tarefa.titulo, "descricao": tarefa.descricao}), 201

# Listar todas as tarefas
@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    db = next(get_db())
    tarefas = db.query(Tarefa).all()
    return jsonify([{"id": t.id, "titulo": t.titulo, "descricao": t.descricao} for t in tarefas])

# Atualizar tarefa
@app.route("/tarefas/<int:tarefa_id>", methods=["PUT"])
def atualizar_tarefa(tarefa_id):
    data = request.get_json()
    db = next(get_db())
    tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()

    if not tarefa:
        return jsonify({"error": "Tarefa não encontrada"}), 404

    tarefa.titulo = data.get("titulo", tarefa.titulo)
    tarefa.descricao = data.get("descricao", tarefa.descricao)
    db.commit()
    return jsonify({"message": "Tarefa atualizada com sucesso!"})

# Deletar tarefa
@app.route("/tarefas/<int:tarefa_id>", methods=["DELETE"])
def deletar_tarefa(tarefa_id):
    db = next(get_db())
    tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()

    if not tarefa:
        return

