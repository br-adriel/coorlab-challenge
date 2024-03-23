# Resultado - Desáfio CoorLab

A implementação do desafio transcorreu de forma tranquila e foi implmentada
conforme especificado.

![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Vue.js](https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)

## Desenvolvimento

A seguir é detalhado as bibliotecas/frameworks adotados em cada parte do projeto
e informações acerca da implementação.

### Backend

Para a implementação do Backend eu escolhi utilizar o framework Django. A
escolha foi motivada por eu ter familiaridade no desenvolvimento com essa
ferramenta. Para que a aplicação se comportasse como uma api, foi utilizado o
pacote `django_rest_framework`, que facilita a construção de APIs REST com
esse framwork.

Foram implementadas três endpoints: um para ao retorno dos destinos disponíveis,
outro para o retorno das opções de viagem mais rápida/confortável e mais barata,
conforme especificado no caso de uso, e um endpoint de retorno de todas as
opções de viagem cadastras no banco de dados.

Esse último foi utilizado apenas para a verificação dos dados durante o
desenvolvimento, não sendo utilizado no frontend em nenhum momento.

### Frontend

Para o frontend foi escolhida a versão 3 do Vue e foi adotada a composition API
durante todo o desenvolvimento. Em relação a dependencias, foram utilizados os
pacotes `axios` (requisições a API), `tailwind` (estilização), `vueform`
(elementos de formulário) e `clsx` (utilitário para construção condicional de
classes CSS). Desses, o único que não havia utilizado antes foi o `vueform`.

No frontend, o desenvolvimento do select conforme o design do prototype foi o
principal empecilho durante o desenrolar do projeto, pois o pacote que planejei
utilizar inicialmente não permitia a customização conforme o pedido na
especificação e as outras alternativas encontradas antes da escolha do
`vueform` estavam defasadas (compatíveis apenas com vue 2) ou permitiam uma
customização muito limitada.

Algumas partes do design foram implementadas de maneira diferente do protótipo,
elas estão listadas abaixo junto ao motivo.

- Fonte e ícones: não havia especificação de qual foi a fonte ou pacote de
ícones utilizados, então tentei encontrar opções semelhantes entre as que
conheço. Foi adotada a fonte
[Noto Sans](https://fonts.google.com/noto/specimen/Noto+Sans) e os pacotes de
ícone [Phosphor Icons](https://phosphoricons.com/) e
[Bootstrap Icons](https://icons.getbootstrap.com/).

- Sombra flutuante no topo da página: no protótipo em vídeo é possível notar uma
espécie de sombra que não parece pertencer a nenhum elemento. Ela foi
interpretada como erro de design e desconsiderada no layout desktop. No layout
mobile ela foi incorporada como sendo a sombra do header/navbar.

- Ícone de seta do select: no protótipo o ícone do select é apresentado como uma
seta para a direita que gira 90 graus ao select ser ativado, como o select do
pacote `vueform` não permitia esse tipo de customização, foi mantida a fornecida
por ele, que é similar a do protótipo.

## Considerações

- Para o script de execução foram utilizados os servidores de desenvolvimento
das duas implementações, o backend também utiliza o banco de dados padrão de
desenvolvimento (SQLite).

- O script de execução contém comandos que exibem o PID dos dois processos no
terminal durante a sua execução para que eles possam ser parados após a
visualização do resultado.
