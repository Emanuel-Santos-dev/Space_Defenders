Space Defenders

Space Defenders é um jogo 2D inspirado em clássicos como Space Invaders, desenvolvido usando a biblioteca PyGame. O jogador controla uma nave que atira em inimigos que descem do topo da tela. O objetivo é sobreviver o máximo possível, destruindo os inimigos e evitando os ataques.

Funcionalidades:
-Movimento da nave controlado pelo teclado.
-Tiros do jogador e inimigos.
-Sistema de pontuação e highscore persistente.
-Estrelas no fundo que simulam o espaço.
-Tela de Game Over com opção de retornar ao menu principal.

Requisitos:
-Python 3.12 ou superior.
-PyGame 2.6.0 ou superior.
-Pickle (para salvar a pontuação mais alta - já vem com o Python).

Instalação:
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/space-defenders.git
Crie um ambiente virtual (opcional, mas recomendado):

No Windows:

bash
Copiar código
python -m venv venv
venv\Scripts\activate

No Linux/MacOS:

bash
Copiar código
python3 -m venv venv
source venv/bin/activate

Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Se você não tiver o arquivo requirements.txt, adicione a dependência manualmente:

bash
Copiar código
pip install pygame
Execute o jogo:

Como jogar
Movimento da nave: Use as setas do teclado (← e →) para mover a nave para a esquerda e para a direita.
Atirar: Pressione a barra de espaço (SPACE) para atirar.
Objetivo: Destrua todos os inimigos e evite ser atingido pelos tiros inimigos.
Game Over: Quando sua nave for destruída, a tela de Game Over será exibida e você poderá voltar ao menu principal.
Pontuação e Highscore
O sistema de pontuação adiciona pontos para cada inimigo destruído. Sua pontuação mais alta (highscore) é salva localmente no arquivo high_score.pkl, e será carregada automaticamente ao iniciar o jogo.

Resetar o Highscore
Se você deseja resetar sua pontuação mais alta, exclua manualmente o arquivo high_score.pkl ou use o comando abaixo para removê-lo automaticamente:

import os
if os.path.exists('high_score.pkl'):
    os.remove('high_score.pkl')

Estrutura do Projeto:

Space_Defenders/
│
├── assets/                # Recursos do jogo (imagens, sons, etc.)
├── font/
│   ├── settings.py        # Configurações gerais (tela, FPS, etc.)
│   ├── player.py          # Classe que gerencia o jogador
│   ├── enemy.py           # Classe que gerencia os inimigos
│   ├── game_functions.py  # Funções auxiliares (estrelas, colisões, etc.)
│   ├── menu.py            # Menu principal e tela de Game Over
│
├── high_score.pkl         # Arquivo que salva o highscore (criado automaticamente)
├── main.py                # Arquivo principal que inicia o jogo
└── README.md              # Documentação do projeto

Contribuições:
Contribuições são bem-vindas! Se você encontrar algum bug, quiser adicionar novas funcionalidades ou melhorar o código existente, sinta-se à vontade para enviar um pull request.

Fork este repositório.
Crie uma nova branch (git checkout -b feature-nome-da-feature).
Commit suas alterações (git commit -m 'Adiciona nova feature').
Push para a branch (git push origin feature-nome-da-feature).
Abra um pull request.
Créditos
Este jogo foi desenvolvido como parte de um projeto de estudo da linguagem Python e da biblioteca PyGame.