# Chatbot de Previsão COVID-19

***

### Funcionalidade
 
Tendo em vista o contexto do enfrentamento do congestionamento do sistema de saúde, particularmente durante a pandemia da COVID-19, foi desenvolvido este chatbot utilizando o Amazon Lex a fim de solucionar esse problema. O modelo preditivo foi treinado com base em um amplo conjunto de dados que inclui informações sobre sintomas, resultados de exames e comorbidades de pacientes, fornecido pelo governo do estado do Espírito Santo. Este modelo de aprendizado de máquina é agora a principal fonte de orientações e previsões, utilizando os dados fornecidos pelos usuários. Ao informar seus sintomas, o chatbot avalia a probabilidade de o usuário estar infectado pelo vírus. Além disso, é importante destacar que os dados inseridos pelo usuário serão devidamente armazenados em uma tabela no banco de dados DynamoDB, com a finalidade de ser utilizado futuramente para o planejamento de tomada de decisões de políticas públicas. Vale resaltar que os modelos não atingiram uma acertividade considerável, sendo o projeto apenas um objete de estudo de caso para uma possivel aplicação real. 

***

### Desenvolvimento do projeto

- Durante o processo de desenvolvimento do modelo de aprendizado de máquina, foi escolhido o algoritmo **XGBoost**, utilizando a linguagem de programação **Python**. Embora três conjuntos de dados tenham sido encontrados, apenas um foi utilizado para prever a probabilidade de infecção pelo vírus, com foco em informações como sintomas, comorbidades e resultados de exames. Após a seleção e tratamento dos dados relevantes, uma limpeza do conjunto de dados foi realizada, mantendo somente as informações necessárias. Foram realizados testes com os modelos Random Forest e regressão logística, no entanto, os resultados obtidos não foram satisfatórios, e, portanto, esses modelos não foram adotados. Em vez disso, o modelo de aprendizado XGBoost foi escolhido para o treinamento, embora também tenha apresentado resultados parcialmente insatisfatórios. A biblioteca `scikit-learn` não pôde ser usada na função Lambda devido a restrições de recursos e tamanho. Para superar essa limitação, optamos por implementar a inferência do modelo por meio de um endpoint. Esse método permitiu que o modelo fosse utilizado com eficiência em um chatbot, proporcionando a previsão da probabilidade de infecção pelo vírus.

#### Random forest:

  #### Regressão Logística:



  #### XG Boost:

)

#### Matriz de confusão do XG Boost:



- Concomitantemente, foi desenvolvido um chatbot na plataforma **Amazon Lex v2**. Este chatbot foi integrado ao modelo XGBoost, possibilitando aos usuários a inserção de informações sobre seus sintomas e comorbidades. A resposta do modelo foi avaliada pelos endpoints, permitindo ao chatbot fornecer orientações personalizadas.

- Reconhecendo a importância de preparar hospitais para futuras demandas, foi implementado um sistema de armazenamento de dados eficiente no **Amazon DynamoDB**. Isso possibilitou o registro de dados dos usuários, contribuindo para a identificação de tendências e o planejamento estratégico dos recursos de saúde.

- Com a finalidade de disponibilizar o chatbot foi utilizado o **Slack**.

### Dados utilizados

##### foram analisados os seguintes conjuntos de dados para a utilização no projeto:

- microdados-painel-covid-19 (Governo do Estado do Espirito Santo): https://dados.es.gov.br/dataset/dados-sobre-pandemia-covid-19/resource/38cc5066-020d-4c5a-b4c0-e9f690deb6d4
- Covid-19 Dataset (Kaggle): https://www.kaggle.com/datasets/meirnizri/covid19-dataset
- COVID-19 Symptoms Checker (Kaggle): https://www.kaggle.com/datasets/iamhungundji/covid19-symptoms-checker

***
### Arquitetura do Chatbot

##### O chat bot possui as seguites Intents:

- initial-intent: Apresenta uma breve descrição e mostra ao usuário possiveis frases para a utilização do chatbot.
- bot-details: Apresenta mais detalhes do bot ao usuário.
- collect-informations: Coleta as informações do usuário e faz a predição de infecção utilizando o modelo treinado e envia esses dados ao branco de dados (DynamoDB).
- cancel-intent: Captura possiveis palavras que podem indicar que o usuário não quer mais proseguir em algum processo do bot.
- fallback: Invocada quando ocorre algum erro durante a execução exibindo uma mensagem ao usuário.

##### Fluxo de informações collect-informations intent:



***

#### Arquitetura do projeto:



***
 
### Como utilizar a aplicação?

- Abra o navegador de sua preferencia e siga o link: ***LINK INATIVO**.
- Click no canto inferior esquerdo no app 'Coleta de informações Covid-19' e inicie a conversa com bot.

  ![videochatbot](https://github.com/Compass-pb-aws-2023-FATEC/sprint-7-pb-aws-fatec/assets/127274078/89df0819-9291-4605-8558-cee45c7c5ead)

***
