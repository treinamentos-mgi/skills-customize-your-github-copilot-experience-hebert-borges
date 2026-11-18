# 📘 Atividade: Testando APIs com pytest

## 🎯 Objetivo

Escreva testes automatizados para uma API FastAPI usando `pytest` e `TestClient`. Você vai verificar respostas HTTP bem-sucedidas, conferir os dados retornados e testar como a API responde quando um recurso não existe.

## 📝 Tarefas

### 🛠️ Preparar o Ambiente de Testes

#### Descrição
Instale as dependências, salve o código inicial como `app.py` e crie um arquivo `test_app.py` no mesmo diretório. Use o cliente de testes do FastAPI para enviar requisições sem iniciar um servidor.

#### Requisitos
O programa concluído deve:

- Instalar `fastapi`, `pytest` e `httpx` com `python -m pip install fastapi pytest httpx`
- Importar `app` de `app.py` e criar um `TestClient` para ela
- Testar `GET /tasks` e verificar o código HTTP `200`
- Verificar que a resposta de `GET /tasks` é uma lista com tarefas contendo `id` e `title`

### 🛠️ Testar Recursos Existentes e Erros

#### Descrição
Adicione testes para consultar uma tarefa pelo identificador e para a resposta da API quando o identificador solicitado não existe.

#### Requisitos
O programa concluído deve:

- Testar `GET /tasks/{task_id}` com o ID `1` e verificar o código HTTP `200` e os dados da tarefa
- Testar `GET /tasks/{task_id}` com o ID `999` inexistente e verificar o código HTTP `404`
- Executar os testes com `python -m pytest -v` e confirmar que todos passam
