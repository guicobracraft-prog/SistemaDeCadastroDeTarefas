# 📝 Sistema de Cadastro de Tarefas

Aplicação web desenvolvida em **Flask** para gerenciar tarefas com prioridade, status e prazo. Os dados são persistidos localmente em um arquivo JSON, então nada se perde ao fechar o programa.

---

## ✨ Funcionalidades

- ✅ Adicionar tarefas com nome, tipo, status e prazo
- 🎯 Definir prioridade: **Urgente**, **Normal** ou **Baixa**
- 📌 Definir status: **Pendente**, **Fazendo** ou **Concluída**
- 📅 Adicionar prazo com destaque para tarefas **atrasadas**
- ✔️ Marcar tarefa como concluída com um clique
- 🗑️ Excluir tarefas individualmente
- 🔀 Ordenação automática por prazo (mais próximo primeiro)
- 💾 Persistência em arquivo `tarefas.json`
- 🎨 Interface responsiva com CSS moderno

---

## 🖼️ Preview

| Prioridade | Aparência |
|------------|-----------|
| 🔴 Urgente | Faixa vermelha à esquerda |
| 🟡 Normal  | Faixa amarela à esquerda |
| 🟢 Baixa   | Faixa verde à esquerda |

Tarefas concluídas ficam **riscadas** e com opacidade reduzida.
Prazos vencidos aparecem com **fundo vermelho**.

---

## 🚀 Como rodar o projeto

### Pré-requisitos

- **Python 3.10+** instalado
- **pip** disponível

### Passo a passo

1. Clone o repositório:

   git clone https://github.com/guicobracraft-prog/SistemaDeCadastroDeTarefas.git

2. (Opcional, mas recomendado) Crie um ambiente virtual:

   python -m venv .venv
   .venv\Scripts\activate      (Windows)
   source .venv/bin/activate   (Linux/macOS)

3. Instale o Flask:

   pip install flask
   py pip install flask ( caso o de cima não funcionar )

5. Rode a aplicação:

   python app.py

6. Abra no navegador:

   http://127.0.0.1:5000

---

## 📁 Estrutura do projeto

SistemaDeCadastroDeTarefas/
├── app.py                 # Aplicação Flask (rotas e lógica)
├── tarefas.json           # Banco de dados local (gerado automaticamente)
├── templates/
│   └── index.html         # Página principal
├── static/
│   └── style.css          # Estilos da aplicação
├── .gitignore
└── README.md

---

## 🧠 Como funciona

### Estrutura de cada tarefa

{
    "id": 1,
    "nome": "Estudar Flask",
    "tipo": "urgente",
    "condicao": "pendente",
    "prazo": "2026-09-20"
}

### Rotas da aplicação

| Método | Rota             | Descrição                                |
|--------|------------------|------------------------------------------|
| GET    | /                | Lista todas as tarefas ordenadas por prazo |
| POST   | /adicionar       | Cria uma nova tarefa                     |
| GET    | /concluir/<id>   | Marca a tarefa como concluída            |
| GET    | /excluir/<id>    | Remove a tarefa                          |

---

## 🛠️ Tecnologias utilizadas

- **Python 3**
- **Flask** — microframework web
- **HTML5 + Jinja2** — templates dinâmicos
- **CSS3** — estilização moderna com variáveis CSS
- **JSON** — persistência simples de dados

---

## 📌 Melhorias futuras

- [ ] Filtro por tipo e status
- [ ] Edição de tarefas já criadas
- [ ] Contador de tarefas (pendentes / concluídas)
- [ ] Migração para banco de dados SQLite
- [ ] Autenticação de usuários
- [ ] API REST

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Sinta-se livre para usar, estudar e modificar.

---

## 👤 Autor

Desenvolvido por **Guilherme**

- GitHub: @guicobracraft-prog

---

⭐ Se este projeto te ajudou, deixe uma estrela no repositório!
