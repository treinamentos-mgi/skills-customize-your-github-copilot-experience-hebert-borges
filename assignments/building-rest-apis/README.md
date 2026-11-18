# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Construa uma API REST para cadastrar e gerenciar tarefas usando o framework FastAPI. Você praticará rotas HTTP, validação de dados com modelos, códigos de status e documentação interativa, mantendo os dados em memória.

## 📝 Tarefas

### 🛠️ Modelar e Listar Tarefas

#### Descrição
Instale FastAPI e Uvicorn com `python -m pip install fastapi uvicorn`. Complete o código inicial para criar a aplicação, definir o modelo de uma tarefa e listar as tarefas cadastradas.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI que possa ser iniciada com `uvicorn starter-code:app --reload`
- Definir um modelo de tarefa com título, descrição e estado de conclusão
- Implementar `GET /tasks` para retornar a lista de tarefas, inicialmente vazia
- Expor a documentação interativa em `/docs` para explorar e testar a API

### 🛠️ Implementar as Operações de Gerenciamento

#### Descrição
Expanda a API para criar, consultar, atualizar e excluir tarefas. Use os identificadores das tarefas para consultar, alterar ou remover um item específico.

#### Requisitos
O programa concluído deve:

- Implementar `POST /tasks` para criar uma tarefa e responder com o código HTTP `201`
- Implementar `GET /tasks/{task_id}` para retornar uma tarefa ou responder `404` quando o identificador não existir
- Implementar `PUT /tasks/{task_id}` para atualizar uma tarefa existente ou responder `404` quando ela não existir
- Implementar `DELETE /tasks/{task_id}` para excluir uma tarefa existente e responder `204`, ou responder `404` quando ela não existir
- Testar as rotas pela documentação em `/docs` e confirmar que os dados são mantidos apenas enquanto a aplicação estiver em execução
