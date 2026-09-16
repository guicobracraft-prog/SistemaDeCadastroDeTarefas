from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

ARQUIVO = "tarefas.json"


def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)


@app.route("/")
def index():
    tarefas = carregar_tarefas()

    # Ordena por prazo — quem não tem prazo vai pro final
    tarefas = sorted(
        tarefas,
        key=lambda t: t.get("prazo") or "9999-12-31"
    )

    return render_template("index.html", tarefas=tarefas)


@app.route("/adicionar", methods=["POST"])
def adicionar():
    nome = request.form.get("tarefa")
    tipo = request.form.get("tipo", "normal")
    condicao = request.form.get("condicao", "pendente")
    prazo = request.form.get("prazo", "")

    if nome:
        tarefas = carregar_tarefas()
        tarefas.append({
            "id": len(tarefas) + 1,      # id único simples
            "nome": nome,
            "tipo": tipo,
            "condicao": condicao,
            "prazo": prazo
        })
        salvar_tarefas(tarefas)

    return redirect("/")


@app.route("/concluir/<int:id_tarefa>")
def concluir(id_tarefa):
    tarefas = carregar_tarefas()
    for t in tarefas:
        if t["id"] == id_tarefa:
            t["condicao"] = "concluida"
            break
    salvar_tarefas(tarefas)
    return redirect("/")


@app.route("/excluir/<int:id_tarefa>")
def excluir(id_tarefa):
    tarefas = carregar_tarefas()
    tarefas = [t for t in tarefas if t["id"] != id_tarefa]
    salvar_tarefas(tarefas)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)