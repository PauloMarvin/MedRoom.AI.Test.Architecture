# Teste - Equipe de inteligência artificial - Arquiteto de Sistemas

## Introdução
Antes de iniciar sua jornada como integrante da equipe de IA da MedRoom, convidamos você a criar um pequeno projeto de exemplo, assim poderemos conhecer melhor suas habilidades técnicas e entender seus conhecimentos!

## Objetivo
Neste projeto o seu objetivo é devolver um score de semelhança entre frases. Para isso, você poderá criar um modelo, utilizar um já existente ou apenas aplicar métodos matemáticos na comparação.


Para a entrega deste projeto, você deverá utilizar seus conhecimentos em Docker e Python!

## Dados
O usuário deverá entrar com 2 frases que ele deseja comparar a semelhança e, após isso, o programa deverá devolver um percentual indicando o quão uma frase é parecida com a outra.

Exemplo:
- **Frase 1**: "De 0 a 10, qual o nível de intensidade da sua dor atualmente?"
- **Frase 2**: "Qual a intensidade da sua dor?"
- **Score**: 80%

A comparação pode ser feita tanto estruturalmente (levando em conta apenas as palavras entre as duas frases), quanto semanticamente (levando em conta o sentido entre as duas frases). A escolha fica por sua conta!

## Entrega esperada
- Arquivo Dockerfile com a definição da imagem
- A imagem a ser criada deverá conter o arquivo .py que será executado

Exemplo:
```shell
# Executando a imagem
docker run <nome-img>

# Entrando no container
docker exec -it <nome-container> /bin/bash

# Executando o arquivo .py dentro do container
python3 programa.py

# --------
# Saída esperada do programa:
# --------
# Entre com a primeira frase: ...
# Entre com a segunda frase: ...
# O score de semelhança entre as frases é de <x>%
# --------
```

## Como entregar
Faça um fork deste repositório e coloque os arquivos Dockerfile e .py dentro dele. Depois, nos avise via e-mail, WhatsApp ou LinkedIn e envie o link do repositório para analisarmos a entrega.

Boa sorte! ;)
