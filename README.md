# Projeto: Biblioteca Online📚

### 🖥️ *Biblioteca Online* é uma aplicação desenvolvida em Flask com Python, que apresenta livros em PDF para leitura sem utilizar espaço do próprio armazenamento. 
#### 📂 O projeto inclui livros com acesso aos respectivos PDF'S para leitura e envio de sugestões diretas dos usuários que ficam armazenadas em nosso banco de dados
---
### 🛠️ FUNCIONALIDADES:
#### 🔎 Selecionar livros para leitura.
#### 📋 Ver a lista de livros, e seus PDF'S.
#### 📬 Enviar sugestões de livros e autores para a contribuição do site.
---
### 🛠️ TECNOLOGIAS UTILIZADAS:
#### *Flask:* Framework para o desenvolvimento rápido e eficiente de aplicações web.
#### *Python:* Linguagem principal utilizada no desenvolvimento.
#### *SQLAlchemy:* Utilizado para a integração e o gerenciamento de dados à um banco de dados externo.
---
### 📂 ESTRUTURA DO PROJETO:
#### *Static:*  Definições de cada parte da estilização do site. Imagens, PDF'S e o estilo de cada página que estruturam o design do site.
#### *Templates:* Inclui as páginas de interface do usuário, implementadas em HTML. Essas páginas são responsáveis pela apresentação e a interação com o usuário.
#### *App:* Implementa a lógica de acesso às páginas e ao banco de dados. Essa camada abstrai os detalhes de comunicação com as páginas e com o banco, mantendo o código mais organizado e testável.
---
### ⚙️ COMO UTILIZAR?
#### Pela instalação das dependências por meio do ambiente de desenvolvimento de sua preferência, primeiramente é necessário instalar o Python, por segundo é necessário instalar o Flask, após o Flask, instalar o pacote SQLAlchemy no ambiente Python com o Flask, por último instalar o psycopg2 no mesmo ambiente.
#### Após isso o site estará pronto para ser compilado e executado.