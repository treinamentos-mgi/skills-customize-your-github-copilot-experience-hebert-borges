---
name: new-assignment
description: "Crie uma nova assignment de programação para estudantes da Mergington High School. Use quando o usuário pedir para criar, adicionar, estruturar ou gerar uma assignment, exercício ou tarefa de programação."
---

# Criar uma Nova Assignment

Use este fluxo para criar uma tarefa e registrá-la no portal do curso.

## Planejar

- Identifique o conceito de programação solicitado; se ele não estiver claro, pergunte antes de criar a tarefa.
- Defina de 2 a 4 tarefas que avancem gradualmente, com objetivos claros e adequados ao nível do aluno.
- Inclua starter code quando ele ajudar o aluno a começar ou precisar estabelecer uma estrutura específica.

## Criar os Arquivos

- Crie `assignments/<id>/README.md`, usando um identificador descritivo em kebab-case.
- Siga [`templates/assignment-template.md`](../../../templates/assignment-template.md) e as instruções aplicáveis em `.github/instructions/assignments.instructions.md`.
- Se necessário, crie `starter-code.py` ou arquivos de dados dentro da mesma pasta.

## Registrar no Portal

Use os scripts oficiais; não edite `config.json` manualmente. Os scripts do dev container ficam em `.devcontainer/.github/skills/new-assignment/scripts/`.

Registre a assignment:

```sh
node .devcontainer/.github/skills/new-assignment/scripts/update-config.js <id> "<título>" "<descrição>"
```

Registre cada arquivo para download como anexo:

```sh
node .devcontainer/.github/skills/new-assignment/scripts/add-attachment.js <id> "<nome exibido>" <arquivo> <tipo>
```

Tipos comuns incluem `python`, `csv`, `json`, `txt` e `html`.

## Verificar

- Confirme que `config.json` contém a nova assignment e seus anexos.
- Confirme que o README e todos os arquivos referenciados existem dentro de `assignments/<id>/`.
- Se o site estiver disponível, abra a página da assignment no preview e verifique o conteúdo e os links para download.
