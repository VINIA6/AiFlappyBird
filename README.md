# Ai Flappy Bird

Em um cenário de desenvolvimento notamos que teríamos que gerenciar varias versões de pacotes e do próprio Python na maquina, o que poderia rapidamente se transformar em uma grande confusão de versões entre projetos, um verdadeiro caos. Por isso utilizamos o método de criação de um ambiente virtual, veja abaixo os comandos para criar o ambiente virtual e baixar as dependencias do projeto. 

Criação de ambiente virtual: 
      
    py -m venv venv

Instalação das dependências: 

    pip install -r requirements.txt
    
Com o ambiente configurado, podemos rodar o projeto:

    py JogoFlappyBird.py

O projeto consiste na criação de uma réplica do jogo Flappy Bird e o controle do jogo por meio de uma inteligência artificial criada com Redes Neurais e Algoritmos Genéticos.  

## Inteligência Artificial - NEAT

Neural Evolution Augment Topology (NEAT) é um algoritmo genético (AG) para a geração de redes neurais artificiais em evolução (uma técnica de neuroevolução). 

### Algoritimos Genéticos 

Algoritmos Genéticos (AG) são implementados como uma simulação de computador em que uma população de representações abstratas de solução é selecionada em busca de soluções melhores. A evolução geralmente se inicia a partir de um conjunto de soluções criado aleatoriamente e é realizada por meio de gerações. A cada geração, a adaptação de cada solução na população é avaliada, alguns indivíduos são selecionados para a próxima geração, e recombinados ou mutados para formar uma nova população. A nova população então é utilizada como entrada para a próxima iteração do algoritmo.
Neste caso o indivíduo a ser evoluído será o passáro, para cada caracteristica recebida será evoluida através de mutações que podem ou não serem eliminadas como indivíduo fraco daquela determinada geração. 

<img src="https://github.com/VINIA6/AiFlappyBird/blob/master/imgs/bird1.png" width="100" height="85" />

### Redes Neurais Artificiais

Redes neurais Artificiais são modelos computacionais inspirados pelo sistema nervoso central de um animal (em particular o cérebro) que são capazes de realizar o aprendizado de máquina bem como o reconhecimento de padrões. Redes neurais artificiais geralmente são apresentadas como sistemas de "neurônios interconectados, que podem computar valores de entradas", simulando o comportamento de redes neurais biológicas.

<img src="https://github.com/VINIA6/AiFlappyBird/blob/master/imgs/config/rn.png" width="300" height="300" />

### NEAT

Neural Evolution Augment Topology (NEAT) utiliza as duas técnicas acima pra definir um indivíduo evoluído e inteiramente capaz de repoduzir as ações de inteligência do jogo, para cada pássaro, temos uma rede neural. 

<img src="https://github.com/VINIA6/AiFlappyBird/blob/master/imgs/config/birdRN.png" width="450" height="300" />

E todos os pássaros gerados devemos entender como um indivíduo diferente um do outro, assim feterminamos 100 pássaros para cada geração. 

<img src="https://github.com/VINIA6/AiFlappyBird/blob/master/imgs/config/100.png" width="450" height="300" />

Os indivíduos que ficam por último em cada geração servem para gerar novas mutações, onde serão os ancestrais de um espécie mais evoluída, assim fazendo com que um passáro em determinada geração seja evoluído suficiente para não morrer mais.

## Desenvolvimento do jogo 

Pygame é uma biblioteca escrita em Python e baseada em SDL.
Voltada para o desenvolvimento de games e interfaces gráficas, o Pygame fornece acesso a áudios, imagens, teclados, controles, mouses e hardwares gráficos via OpenGL e Direct3D.
Com essa biblioteca podemos criar uma cópia do jogo Flappy Bird, na criação do jogo optamos por utilizar programação orientada a objeto, tendo 3 classes principais que criam o esquema do jogo. 

### class Passaro: 

* pular() - O passaro deve iniciar em uma altura relativa e saltar no eixo y em uma velocidade constante determinada no código.
                  
* mover() - O calculo do deslocamento é feito pela formula S=So+V*T, nesta função também deve ser calculada a rotação do passaro para o ângulo de queda.
                  
* desenhar() - Deve definir qual imagem do passaro vai usar para o desenho do jogo. 

### class Cano: 

* definir_altura() - A altura dos canos deve ser randomica e devem seguir um padrão de altura tanto para o cano de cima para como o cano de baixo.
                  
* mover() - A movimentação dos canos devem seguir a velocidade padrão estabalecida no jogo. 
                  
* desenhar() - Desenha o cano de baixo e a mesma imagem serve para desenhar o cano de cima só que com uma rotação.
                  
* colidir() - O passaro deve identificar o cano ao colidir, pra isso usamos funções prontas do pygame para ajudar na construção da colisão.

### class Chao: 
                  
* mover() - O chão deve se movimentar de acordo com a referencia da velocidade estabelecida pelo jogo.
                  
* desenhar() - Mostrar em tela a imagem do chão em loop infinito até o fim do jogo. 
