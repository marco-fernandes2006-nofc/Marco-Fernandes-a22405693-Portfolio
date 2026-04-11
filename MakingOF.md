# Criação inicial dos modelos

---

![Imagem Diagrama](media/data/images/Imagem%20Making%20OF.jpg)

---

## Licenciatura
- Nome  
- Sigla  
- Descrição  
- Duração por Anos  
- Faculdade  

Para a licenciatura era necessário a identificação básica sendo o Nome e a Sigla, uma breve descrição para saber o que consiste a licenciatura, a duração dos anos que leva para fazer a licenciatura e a localidade de onde foi tirada a licenciatura.

---

## Unidades Curricular
- Nome  
- Descrição  
- Ano Curricular  
- Semestre  

O Nome serve para identificar a UC, a descrição serve para demonstrar os objetivos da UC, o Ano Curricular e o Semestre foram escolhidos para identificar quando que vai ser introduzida essa UC, sendo que o semestre serve também para dizer se a UC é anual ou semestral em certos casos.

---

## Projeto
- Nome  
- Descrição  
- Conceitos Aplicados  
- Tecnologias  
- Data de realização  

O nome serve como identificação do projeto, descrição serve para indicar o que é feito nesse projeto, conceitos aplicados para identificar certos conceitos utilizados durante a produção desse projeto, tecnologias para identificar que tecnologias foram utilizadas para o projeto e a data de realização para saber quando que foi realizado o projeto.

---

## Tecnologia
- Nome  
- Tipo  
- Descrição  
- Logo  
- Website Oficial  

Nome para uma simples identificação da tecnologia, tipo para saber se é uma linguagem de programação, uma ferramenta, uma framework etc., descrição para dar uma pequena entrada para saber do que se trata a tecnologia, a logo para uma identificação mais visual e o site oficial que contém mais informações sobre a tecnologia.

---

## TFC
- Nome  
- Descrição  
- Ano  
- Autores  
- Orientadores  
- Tecnologias  
- Repositório Git  
- Documento  

Nome para identificação simples, descrição simples para saber em que consiste o TFC, Ano em que foi realizado (que futuramente foi substituído pelo Rating), autores que fizeram o TFC, orientadores que ajudaram no TFC, tecnologias utilizadas para fazer o TFC, repositório git (removido posteriormente por falta de informação) e documento que possui mais informação sobre o TFC.

---

## Competência
- Nome  
- Tipo  
- Descrição  
- Nível  

Nome para identificação simples, tipo para saber se é uma soft skill ou uma tecnologia, descrição como um breve resumo do que consiste a competência e o nível que tenho nessa competência.

---

## Formação
- Nome  
- Instituição  
- Tipo  
- Descrição  
- Data Início  
- Data Fim  

Nome como identificação básica, Instituição para saber onde a formação foi tirada, Tipo de formação, Descrição breve da formação, data de início e fim para identificar o período em que foi realizada.

---

## Making OF
- Descrição  
- Erros  
- Justificação de Opções  
- Imagem  
- Projeto  

Descrição breve para saber do que se trata o Making OF, erros que possam ter acontecido, justificação de opções para explicar decisões tomadas, imagem como registo e projeto como chave estrangeira para identificar a que projeto pertence.

---

## Contribuição Open-Source
- Nome  
- Descrição Projeto  
- Descrição Contribuição  
- Repositório  
- Website Oficial  

Nome do projeto onde foi feita a contribuição, descrição breve do projeto, descrição da contribuição realizada, repositório do projeto e website oficial caso exista.

---

## Considerações Gerais

Em resumo, muitos dos atributos são essenciais para identificação ou explicação do modelo, sendo na maioria casos escolhas óbvias e fundamentais. Por esse motivo, foi utilizada apenas uma descrição simples para justificar a sua inclusão.

Optou-se também por não criar modelos separados para autores ou orientadores dos TFCs, uma vez que o objetivo é um portfólio pessoal. Em vez disso, foi priorizado o modelo de contribuições open-source, considerado mais relevante neste contexto.

---

# Problemas encontrados durante a criação do projeto

O principal problema encontrado foi que, ao atualizar atributos durante a criação dos loaders, era necessário reiniciar a base de dados, pois as alterações não eram refletidas automaticamente.

Felizmente, o único dado que precisava de ser reinserido manualmente era o utilizador Admin.

De resto, os principais desafios foram decisões iniciais de modelação, onde alguns atributos foram removidos, modificados ou substituídos.

---

# Utilização de AI

A utilização de AI neste projeto foi focada no apoio a decisões criativas, incluindo:
- Escolha de melhores atributos para cada modelo  
- Definição de relações entre entidades  
- Sugestões estruturais no código  

Além disso, foi utilizada para converter este conteúdo para formato Markdown.