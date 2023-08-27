# Teste MedRoom - Equipe de inteligência artificial - Arquiteto de Sistemas

A análise de similaridade de texto é um dos domínios de aplicação do Processamento de Linguagem Natural (NLP).
Através dessas técnicas, torna-se possível avaliar se os textos exibem semelhanças. Esse procedimento viabiliza a
identificação de plágio, a categorização de textos com fundamentação na similaridade, bem como várias outras aplicações.

Neste projeto, o objetivo é criar um modelo capaz de fornecer um escore de semelhança entre frases fornecidas por meio
de um prompt de comando. Além disso, a aplicação deve ter a capacidade de ser executada em um container Docker.
A [especificação](docs/activity_specification.md) pode ser encontrada no arquivo `activity_specification.md` na pasta `docs`.

## Objetivos e resultados-chave

Os objetivos são as metas que devem ser alcançar com esse projeto. Já o resultados-chave são os passos que precisam
ser dados para atingir esses objetivos. A seguir, os objetivos definidos baseados na [especificação](docs/activity_specification.md)
do projeto juntamente com os seus resultados-chave.
 -  ### Criar um calculador de similaridade de texto
    - Criar um pre-processador de texto capaz de remover stopwords, pontuações, caracteres especiais
    dentre outros tipos de ruídos que não são relevantes para a análise de similaridade. Além disso, o pre-processador
    deve ser capaz de executar outros métodos que facilitem a análise de similaridade.
    - Realizar a tokenização do texto, ou seja, quebrar o texto em porções menores, como palavras, frases, etc.
    - Transformar os textos em representações numéricas, para que se possa fazer cálculos para determinar a similaridade
    dentre eles.
    - Criar funções que possam calcular a similaridade entre os textos baseado em suas representações numéricas.
 - ### Criar um container Docker para a aplicação
    - Criar um arquivo Dockerfile com a definição da imagem.
    - A imagem a ser criada deverá conter o arquivo .py que será executado através do comando docker exec.

## Conteúdo

Nessa seção você encontrará uma breve descrição as etapas desenvolvidas, bem como as técnicas utilizadas.

### Pre-processamento de texto utilizado

No processamento de texto, foram aplicadas diversas etapas para otimizar a análise de similaridade:

1. **Redução do texto para letras minúsculas:** O texto é convertido para letras minúsculas, garantindo uniformidade e
tratamento equitativo das palavras, independentemente da capitalização.

2. **Remoção de Pontuações e Caracteres Especiais:** Pontuações e caracteres especiais são eliminados do texto,
simplificando-o para uma análise mais precisa.

3. **Remoção de Links:** Links e URLs são removidos do texto, links para mesma página podem ser apresentados de formas
variadas, o que pode prejudicar a análise de similaridade.

4. **Remoção de Stopwords:** Palavras comuns, conhecidas como "stopwords", que não contribuem significativamente para o
contexto, são removidas para focar a análise nas palavras mais relevantes.

5. **Lematização:** As palavras são reduzidas às suas formas lematizadas, ou seja, à forma base da palavra, considerando
diferentes formas verbais ou conjugações como equivalentes.

6. **Aglutinação de Emojis:** Emojis diferentes são aglutinados em um único termo, simplificando a análise e tratando os
emojis como um único token comum. Poderiam ter sido adicionados outros padrões para aglutinação, porém seria necessário
um conhecimento mais aprofundado do domínio para identificar os padrões mais relevantes.

Essas etapas combinadas ajudam a reduzir variações irrelevantes e a destacar as características semânticas fundamentais
do texto, criando uma base sólida para avaliar a similaridade entre frases de maneira mais precisa.

### Vetorização de Texto com BERT

Para a vetorização do texto, utilizou-se uma versão do modelo pré-treinado BERT denominado
[BERTimbau](https://huggingface.co/neuralmind/bert-base-portuguese-cased). Esse modelo foi treinado com um corpus gerado
por artigos da Wikipedia em português. O artigo que descreve em detalhes em está nas referências deste documento.

Com o auxílio deste modelo, é possível converter o texto em uma representação numérica, que pode ser empregada para
calcular a similaridade entre os textos. É importante destacar que o BERT é classificado como um modelo semântico, uma
vez que, para construir os embeddings, ele leva em consideração o contexto das palavras, ou seja, as palavras que
circundam a palavra em foco.

## Cálculo de Similaridade Utilizando Distância de Cosseno

No processo de avaliar a similaridade entre os embeddings que representam o texto, optou-se por utilizar a distância de
cosseno como medida. Essa abordagem quantifica a relação angular entre os vetores, fornecendo uma medida de similaridade
semântica.

Nesse procedimento, os embeddings individuais de cada token são combinados pela obtenção da média, o que resulta em um
único vetor representativo para o texto como um todo. Isso, por sua vez, viabiliza o cálculo da distância de cosseno
entre os vetores resultantes.

Conforme os testes realizados, a estratégia de calcular a média dos embeddings apresentou resultados mais positivos,
contribuindo para avaliações de similaridade mais precisas entre os textos.

## Utilização

Para utilizar o projeto, algumas etapas são necessárias. A seguir, um passo a passo para que você possa utilizar o projeto.

### Requisitos

Este projeto foi feito e validado com as seguintes versões de software:
 - Python `3.11`
 - Docker `24.0.2`
 - git `2.41.0`
 - Poetry `1.6.1`(opcional)

Provavelmente você não terá problemas com versões diferentes, especialmente se forem mais novas. Portanto, sinta-se livre para utilizar versões mais novas dos softwares citados acima.
Caso tenha problemas, recomendo que utilize as versões citadas acima.

### Utilização

Após criar o repositório, para começar a modificá-lo e/ou contribuir com repositórios já criados, você precisa cloná-lo. Para isso, siga os seguintes passos:

1. Cole o comando abaixo no seu terminal e pressione **Enter**:

    ```
    git clone https://github.com/PauloMarvin/MedRoom.AI.Test.Architecture.git
    ```

2. Com o repositório clonado, você precisa navegar até a pasta raiz do projeto, usando o comando:

    ```
    cd MedRoom.AI.Test.Architecture
    ```

3. Estando na pasta do repositório, basta instalar as dependências do projeto utilizando o comando:

    ```
    poetry install
    ```

    Ele irá instalar todas as dependências contidas no arquivo `pyproject.toml`. Depois disso basta ativar o ambiente virtual criado pelo Poetry utilizando o comando:

    ```
    poetry shell
    ```
    Para mais informações sobre os comandos do Poetry, visite a [documentação oficial](https://python-poetry.org/do).

4. Caso prefira, poderá utilizar o arquivo `requirements.txt` para instalar as dependências do projeto com pip. Para isso, execute o comando:

    Para criar um ambiente virtual com o `venv`:
    ```
    python -m venv .venv
    ```

    Para ativar o ambiente virtual em ambiente Linux/MacOS:
    ```
    source .venv/bin/activate
    ```
    Para ativar o ambiente virtual em ambiente Windows:
    ```
    .venv\Scripts\activate.bat
    ```
    Para instalar as dependências:
    ```
    pip install -r requirements.txt
    ```
    A partir daqui, você já pode abrir seu editor preferido e começar a modificar o projeto caso queira.

5. Para executar o programa, em um container Docker, são necessários os seguintes comandos:

    Build da imagem:

    ```
    docker build --no-cache -t medroom .
    ```
    Executar o container a partir da imagem gerada:
    ```
    docker run --name medroom-app -d medroom
    ```
    Acessar o terminal interno do container:
    ```
    docker exec -it medroom-app /bin/bash
    ```
    Executar a aplicação:
    ```
    python main.py
    ```

    Na primeira execução, será baixado os modelos de linguagem necessários para o funcionamento do programa.
    Após isso, o programa estará pronto para ser utilizado. Não se preocupe, os modelos de linguagem serão baixados
    apenas uma única vez.

### Teste
Este projeto possui testes unitários para garantir o funcionamento correto do programa, caso modificações sejam feitas.
Esses testes estão localizados na pasta `tests` e podem ser executados com o comando abaixo na pasta raiz do projeto:

```
pytest
```

## Desenvolvedores
 - [Paulo Marvin](https://github.com/PauloMarvin)

## Referências

- [souza2020bertimbau] Fábio Souza, Rodrigo Nogueira, Roberto Lotufo. "BERTimbau: pretrained BERT models for Brazilian Portuguese". In: 9th Brazilian Conference on Intelligent Systems, BRACIS, Rio Grande do Sul, Brazil, October 20-23 (to appear), 2020.
    Disponível em: https://repositorio.unicamp.br/Busca/Download?codigoArquivo=466423
- Sentence Similarity using BERT: https://www.kaggle.com/code/eriknovak/pytorch-bert-sentence-similarity
- BERT Explained: State of the art language model for NLP: https://towardsdatascience.com/bert-explained-state-of-the-art-language-model-for-nlp-f8b21a9b6270
