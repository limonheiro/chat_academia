# GymBot - Documentação do Projeto

# Docker

## Build
``
docker build --no-cache --build-arg AWS_ACCESS_KEY_ID=YOUR_AWS_ACESS_KEY_ID \
  --build-arg  AWS_SECRET_ACCESS_KEY=YOUR_AWS_SECRET_ACCESS_KEY \
  --build-arg  AWS_DEFAULT_REGION=YOUR_AWS_DEFAULT_REGION \
  -t gymbot .
``
## RUN
``
docker run -p 80:80 gymbot
``

---

## Equipe
- **Scrum Master:** [Krisley Almeida](https://www.linkedin.com/in/krisley-almeida/)
- **Líder Técnica:** [Lisandra Tkaczuk](https://www.linkedin.com/in/lisandra-tkaczuk-9b4529a7/)
- **Desenvolvedores:** [Jamir Fadul](https://www.linkedin.com/in/jamir-fadul-042376221/), [Letícia Santos](https://www.linkedin.com/in/leticiareginasantos), Jhonney Lima, [Nicolas Timoteu](https://www.linkedin.com/in/nicolas-timoteu/), [Kyska Harrington](https://www.linkedin.com/in/kyskaharrington/), [Maiara Lira](https://www.linkedin.com/in/maiaraslira/)
- **Arquitetos:** [Ricardo Simines](https://www.linkedin.com/in/ricardosiminesscopim/), [Clayton Vieira](https://www.linkedin.com/in/claytonvieiracv/)

---

## Objetivo do Projeto

Conceber, planejar, desenvolver e apresentar uma solução de Inteligência Artificial utilizando Python, integrada a um modelo de linguagem do Amazon Bedrock. Este projeto cobre todo o ciclo de desenvolvimento, incluindo:
- Definição de requisitos
- Arquitetura
- Design Thinking
- Implementação e apresentação final

### Habilidades Exercitadas
- Técnicas: Python, arquitetura de software, data sourcing e integração com IA
- Organizacionais: comunicação, colaboração em equipe e gestão de projetos

---

## Proposta de Valor

- **Foco no Bem-Estar e Saúde**
- **Adolescentes e Jovens Adultos**
- **Redução de Custos**
- **Acesso à Informação Personalizada**
- **Flexibilidade na Rotina**

---

## Solução

O GymBot é um chatbot que:
- Interage com o usuário de forma satisfatória
- Armazena dados para personalizar informações
- Calcula IMC e indica categorias baseadas nos dados coletados
- Fornece dicas personalizadas de exercícios

---

## Metodologia Ágil
- **Kanban**
- Ferramentas utilizadas: [Notion](https://handsomely-thistle-b4f.notion.site/Documenta-o-GymBot-01cce6fd5a784e41a97479930e29f84e?pvs=4) e [Trello](https://trello.com/b/atTd4cQN/projeto-personal-trainer-40)

---

## Requisitos

### Funcionais
- **Cálculo de IMC:** Serviço implementado em Python
- **Armazenamento e Segurança:** AWS Lambda e DynamoDB
- **Geração de Plano de Treino:** Amazon S3 e Bedrock
- **Integração:** Amazon OpenSearch

### Não Funcionais
- **Responsividade:** Tempo de resposta rápido
- **Tecnologias:** Python com biblioteca Boto3 e Amazon Bedrock

---

## Tecnologias Utilizadas

- **Frameworks Web:** Streamlit e FastAPI
- **Linguagem:** Python
- **Integração com IA:** Amazon Bedrock (Titan Text G1 - Premier)

---

## Serviços AWS

- **Amazon Route 53:** Gerenciamento de DNS
- **Amazon CloudFront:** Entrega de conteúdo com baixa latência
- **Amazon Lex:** Chatbot com interação em linguagem natural
- **AWS Lambda:** Execução de funções sem servidor
- **Amazon S3:** Armazenamento de objetos
- **Amazon DynamoDB:** Banco de dados NoSQL
- **Amazon OpenSearch:** Serviço de busca elástica
- **Amazon Bedrock:** Geração de conteúdo personalizado
- **AWS IAM:** Gerenciamento de identidades e permissões
- **Boto3:** Biblioteca Python para interação com AWS

---

## Arquitetura

O GymBot foi projetado inicialmente como um Produto Mínimo Viável (MVP), com ênfase em:
- Python
- Amazon Bedrock

![Fluxograma da arquitetura](https://i.imgur.com/1GbdG6b.jpeg)


### Evoluções Planejadas
- Inclusão de serviços como CloudWatch, Backup, MFA, criptografia e feedback dos usuários
- Uso de documentos no S3 para expandir capacidades do Bedrock

---

## Links Importantes
- [Trello](https://trello.com/b/atTd4cQN/projeto-personal-trainer-40)
- [Notion](https://handsomely-thistle-b4f.notion.site/Documenta-o-GymBot-01cce6fd5a784e41a97479930e29f84e?pvs=4)

---

## Demonstação
[![GymBot demonstração](https://img.youtube.com/vi/gUGX9FsRBa0/0.jpg)](https://www.youtube.com/watch?v=gUGX9FsRBa0)


---


## Conclusão

O GymBot representa uma solução acessível para promover saúde e bem-estar com tecnologia de ponta, aproveitando os recursos da AWS e Python.

**Obrigado à [Escola da Nuvem](https://escoladanuvem.org/), [Núclea](https://www.nuclea.com.br/) e ao instrutor [Júlio Jeronymo](https://www.linkedin.com/in/julio-jeronymo/)!**
