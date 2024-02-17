## Bem-vindo(a) ao repositório do ConversorSped
Olá, eu sou Pedro, e este é mais um dos meus projetos pessoais onde compartilho soluções práticas para desafios do dia a dia. Ao navegar pela vasta rede, é possível encontrar inúmeros projetos interessantes, mas muitos deles carecem de aplicabilidade prática em situações reais.

A proposta deste repositório é oferecer soluções para problemas que surgiram no meu cotidiano e que foram resolvidos por meio deste código. Cada projeto reflete uma experiência pessoal e uma abordagem prática para resolver desafios específicos.

## Motivação ##
Em vez de simplesmente buscar projetos por sua complexidade ou inovação, concentro-me em questões reais que encontrei no meu caminho. Acredito que soluções simples e eficazes são valiosas e podem beneficiar outros desenvolvedores e entusiastas.

A ideia para esse projeto surgiu quando precisei fazer uma análise e vi o formato que os SPED vem da Receita Federal. Um formato que torna a manipulação muito mais difícil, e pior ainda para fazer qualquer tipo de análise.

Com o ConversorSped essa tarefa se torna bem mais fácil e rápida, possibilitando todo tipo de manipulação dos dados com auxilio do programa de planilha eletrônica da sua preferência, além de possibilitar a extração de apenas dos blocos que interessam.

O projeto ainda está em desenvolvimento, mas a ideia é possibilitar a conversão e extração de todos os blocos e tipos de SPED. 

## Como Usar Este Repositório ##

Este repositório foi projetado com simplicidade em mente. Seguir estes passos simples permitirá que você aproveite as soluções apresentadas:

1. **Baixe o Script**

 - No diretório principal do projeto, você encontrará o script necessário para a ler, converter seus SPED em planilhas ou o que quiser. Faça o download do script para o seu ambiente local.

2. **Instale as Dependências:**

 - Antes de executar o script, certifique-se de instalar todas as dependências necessárias e o pacote autoral "SpedUtils" e seus módulos também autorais. Você pode fazer isso executando o seguinte comando no terminal:

```
pip freeze install requirements.txt
```

3. **Execute o Script:**

 - Com as dependências instaladas, agora você pode executar o script. Por enquanto não existe uma interface, mas a funcionalidade pode ser usava da seguinte forma:

1. Faça a chamada pela classe SpedContribuicoes passando como parâmetro o caminho com o SPED em questão.

2. Atribua a uma variável o bloco que deseja extrair.

3. Faça a chamada do método record_reader passando como parâmetro a variável que contém o bloco a ser extraído.

4. Faça a chamada do método generate_sped_csv e passe como parâmetro a variável que contém os registros a serem gravados.


```sped_contribuicoes = SpedContribuicoes(caminho do sped)
    bloco_zero = sped_contribuicoes.block_zero
    registros = sped_contribuicoes.record_reader(bloco_zero)
    sped_contribuicoes.generate_sped_csv(registros)
```

Espero que esta ferramenta torne sua vida um pouco mais fácil!

Contribuição:
Se você encontrar maneiras de melhorar ou otimizar as soluções apresentadas, fique à vontade para contribuir. Sua participação é valiosa para tornar esses projetos ainda mais úteis e abrangentes.

Agradeço por explorar este repositório e espero que as soluções apresentadas aqui sejam úteis para você!

Pedro.
