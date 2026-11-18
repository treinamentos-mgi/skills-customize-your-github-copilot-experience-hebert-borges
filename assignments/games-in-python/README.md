
# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Crie uma versão em Python do jogo da Forca. O jogador deve adivinhar uma palavra secreta, letra por letra, antes de esgotar as tentativas disponíveis. Nesta atividade, você praticará manipulação de strings, seleção aleatória, condicionais, loops e entrada de dados.

## 📝 Tarefas

### 🛠️ Preparar a Palavra e o Estado do Jogo

#### Descrição
Escolha aleatoriamente uma palavra de uma lista predefinida e prepare as variáveis necessárias para acompanhar a partida.

#### Requisitos
O programa concluído deve:

- Selecionar uma palavra aleatória da lista `words` fornecida no código inicial
- Criar uma estrutura para registrar as letras já adivinhadas
- Definir e inicializar a quantidade máxima de palpites incorretos

### 🛠️ Implementar as Rodadas e o Resultado

#### Descrição
Crie o loop principal da partida. Em cada rodada, mostre o progresso da palavra, receba uma letra do jogador e atualize o estado do jogo até que ele vença ou fique sem tentativas.

#### Requisitos
O programa concluído deve:

- Mostrar as letras adivinhadas nas posições corretas e indicar as letras ainda não descobertas
- Receber um palpite de letra e atualizar o progresso ou o contador de palpites incorretos
- Encerrar a partida quando a palavra for descoberta ou as tentativas incorretas acabarem
- Informar se o jogador venceu ou perdeu e revelar a palavra secreta ao final