<hr>
<h1> O que é arquitetura de software? </h1>

Um projeto de arquitetura está preocupado em como organizar um sistema e em como deve ser sua estrutura. Em sistemas tradicionais (ERP, aplicações web, entre outros, ou seja, sistemas não jogos - em sua maioria), a arquitetura de software está preocupada em criar um modelo abstrato do sistema em questão, apresentando os diversos componentes que o formam e as maneiras como tais componentes interagem entre si. 

Podemos projetar arquiteturas de software em dois níveis: pequena ou grande escala. 
 * Pequena escala: uma arquitetura preocupada em programas individuais. Nesse nível, estamos interessados em como um software individualmente, deve ser organizado, em como seus componentes internos devem interagir entre si. Exemplos desse tipo de arquitetura são os modelos de aplicações Web (que seguem padrões MVC, por exemplo).
 * Grande escala: nesse tipo de arquitetura, estamos interessados nos chamados sistemas corporativos complexos e de grande escala, nos quais cada sistema interage direta ou indiretamente com vários outros sistemas. São relevantes, nesse nível, as definições de como esses sistemas se comunicam e as regras de negócio geral presentes nesse ambiente. Por exemplo, um sistema de vendas online precisa integrar-se ao sistema de controle de estoque, sistema de controle de logística etc.

 Os softwares criados para ambientes comptuacionais também apresentam estilos de arquitetura. Normalmente, seguimos padrões específicos de arquiteturas para facilitar o trabalho de análise, implementação e evolução do sistema. Esses padrões podem ser utilizados como forma de dar uma estrutura global ao sistema. 

 * Arquiteturas de fluxo de dados: são aplicadas quando dados de entrada devem ser transformados por meio de uma série de componentes computacionais ou até mesmo de manipulação de dados de saída. Nesse caso, utilizamos uma série de componentes chamados filtros que ao serem empregados de forma serial ou paralela, auxiliam na busca e disposição. 

 * Arquiteturas orientadas a objetos: os componentes de um sistema neste estilo encapsulam os dados e as operações que devem ser aplicadas para manipular esses dados. 

 * Arquiteturas em camadas: nesta arquitetura são definidas várias camadas diferentes, cada uma realizando operações que progressivamente se tornam mais próximas do conjunto de instruções de máquina. Na camada mais externa, os componentes atendem às operações da interface do usuário. Na camada mais interna, fazem a interface com o sistema operacional. As camadas intermediárias fornecem serviços utilitários e funções de software de aplicação. 

 <h1> PADRÕES DE PROJETO </h1>

 Os padrões de projeto, normalmente são associados a um projeto orientado a objetos e, desta forma, a linguagens de programação que também suportam a orientação a objetos. Tais padrões definem estratégias de implementações utilizando mecanismos tradicionais desse paradigma como herança, poliformismo etc. 

 <h3> PANORAMA </h3>

O que é?
O projeto baseado em padrões cria uma nova aplicação por meio da busca de um conjunto de soluções comprovadas para problemas claramente delineados. Cada problema e sua respectiva solução são descritos por um padrão de projeto, catalogado e investigado por outros engenheiros de software que se depararam com a questão e implementaram a solução ao projetarem outras aplicações. Cada padrão nos oferece uma abordagem comprovada para parte do problema a ser resolvido.

Quem realiza?
Um engenheiro de software examina cada problema que surge em uma nova aplicação e busca uma solução relevante por meio de pesquisa em um ou mais repositórios de padrões.

Por que é importante?
Você já ouviu a expressão “reinventar a roda”? Essa situação ocorre frequentemente no desenvolvimento de software e resulta em perda de tempo e energia. Ao utilizarmos padrões de projeto, podemos encontrar uma solução comprovada para um problema específico. À medida que cada padrão é aplicado, as soluções se integram, e a aplicação a ser construída se aproxima cada vez mais de um projeto completo.

Quais são as etapas envolvidas?
O modelo de requisitos é examinado para isolar o conjunto hierárquico de problemas a serem resolvidos. O espaço de problemas é subdividido, permitindo a identificação de subconjuntos associados a funções e características específicas de software. Os problemas também podem ser organizados por tipo: arquitetura, componentes, algorítmicos, interfaces do usuário etc. Uma vez definido um subconjunto de problemas, pesquisam-se um ou mais repositórios de padrões para determinar se existe um padrão de projeto representado em um nível de abstração apropriado. Padrões aplicáveis são adaptados às necessidades específicas do software a ser construído. A solução de problemas personalizados é aplicada em situações nas quais nenhum padrão foi encontrado.

Qual é o artefato?
Um modelo de projeto é desenvolvido, representando a estrutura da arquitetura, a interface do usuário e os detalhes em nível de componentes.

Como garantir que o trabalho foi realizado corretamente?
À medida que cada padrão de projeto é traduzido em elementos do modelo, os artefatos são revistos em termos de clareza, correção, completude e consistência em relação aos requisitos e entre si.

<hr>

<h3> TIPOS DE PADRÕES </h3>
Os padrões de projeto abrangem um amplo espectro de abstração e aplicação.

    Padrões de arquitetura: descrevem problemas de projeto de caráter amplo e diverso, que são resolvidos por meio de uma abordagem estrutural.
    Padrões de dados: abordam tanto os problemas orientados a dados recorrentes quanto as soluções de modelagem de dados que podem ser utilizadas para resolvê-los.
    Padrões de componentes (padrões de projeto): tratam dos problemas associados ao desenvolvimento de subsistemas e componentes, à forma como eles se comunicam entre si e ao seu posicionamento em uma arquitetura maior.
    Padrões de projeto para interfaces: descrevem problemas comuns de interfaces do usuário e suas respectivas soluções, considerando as características específicas dos usuários.
    Padrões para WebApp: tratam de um conjunto de problemas encontrados na construção de WebApps e, em geral, incorporam muitas das categorias de padrões mencionadas anteriormente.
    Padrões móveis: descrevem problemas comumente encontrados no desenvolvimento de soluções para plataformas móveis.
    Padrões de idiomas: em um nível de abstração mais baixo, descrevem como implementar total ou parcialmente um algoritmo específico, além de indicar a estrutura de dados para um componente de software no contexto de uma linguagem de programação específica.

TIPOS DE PADRÕES – GOF

    Padrões criacionais: concentram-se na criação, composição e representação de objetos, dispondo de mecanismos que facilitam a instanciação de objetos em um sistema e impõem restrições sobre o tipo e número de objetos que podem ser criados.
    Padrões estruturais: focalizam problemas e soluções associadas à organização e integração de classes e objetos para construir uma estrutura maior.
    Padrões comportamentais: tratam de problemas associados à atribuição de responsabilidade entre objetos e à forma como a comunicação ocorre entre eles.

FRAMEWORKS

    Um framework é uma "mini-arquitetura" reutilizável que serve como base para a aplicação de outros padrões de projeto.
    Um framework não é um padrão de arquitetura, mas sim um esqueleto com um conjunto de “pontos de conexão” (também chamados de ganchos e encaixes), que permitem a adaptação desse esqueleto a um domínio de problemas específico. Um framework inclui aspectos estáticos/estruturais e dinâmicos/comportamentais que dão suporte ao uso dos padrões de projeto. Os pontos de conexão possibilitam a integração de classes ou funcionalidades específicas de um problema. Em um contexto orientado a objetos, um framework é um conjunto de classes que cooperam entre si.

FRAMEWORKS VERSUS PADRÕES DE PROJETO – GOF

    Os padrões de projeto são mais abstratos do que os frameworks. Os frameworks podem ser incorporados ao código, enquanto apenas exemplos de padrões podem ser utilizados dessa forma. Um ponto forte dos frameworks que utilizam padrões é que eles podem ser escritos em linguagens de programação e não apenas estudados, mas também executados e reutilizados diretamente.
    Os padrões de projeto são elementos arquiteturais menores do que os frameworks. Esses frameworks podem conter vários padrões de projeto, mas a recíproca nunca é verdadeira.
    Os padrões de projeto são menos especializados do que os frameworks. Os frameworks têm um domínio de aplicação particular, enquanto os padrões de projeto podem ser usados em praticamente qualquer tipo de aplicação. Embora existam padrões de projeto mais especializados, até mesmo esses não determinam uma arquitetura de aplicação.

![Padrões](https://media.discordapp.net/attachments/1271502905492504698/1288147120192360498/padraosoftware.png?ex=66f41ffe&is=66f2ce7e&hm=70667030fcc000a00c2a797b54aa593035ef0bf19f5f0f735b065ea6374146dd&=&format=webp&quality=lossless)

* FactoryMethod: define uma interface para criar um objeto, mas deixa que subclasses decidam que classe instanciar.
* Prototype: especifica tipos a criar usando uma instância como protótipo e cria novos objetos ao copiar este protótipo.
* Singleton: garante que uma classe só tenha uma única instância a qual provê um ponto de acesso global a ela. 
* Builder: separa a construção de objetos complexo da representação para criar representações diferentes com o mesmo processo.
* Abstract Factory: provê interface para criar famílias de objetos relacionaods ou dependentes, sem especificar suas classes concretas. 

<hr>
<h3> PADRÕES DE PROJETO GOF MAIS UTILIZADOS NO CONTEXTO DE JOGOS DIGITAIS: </h3>

* Singleton
Intenção: garantir que uma classe tem apenas uma instância e prover um ponto de acesso global a ela. O seu propósito é garantir que apenas uma única instância desse classe seja criada. 
Solução: fazer com que a própria classe seja responsável pela manutenção da instância única, de tal forma que: quanto a instância for requisitada pela primeira vez, esta deve ser criada. Em requisições subsequentes, a instância criada na primeira vez é retornada. 

A classe Singleton deve: armazenar a única instância existente; garantir que apenas uma instância seja criada. 
    * Instância refere-se a um ÚNICO OBJETO que é criado a partir de uma classe.

    '''
    public final class Singleton{
    private static Singleton instance = null;
    private Singleton () {
        ...
    }

    public static Singleton getInstance() { 
        if (instance == null) {
            instance = new Singleton(); 
        }
        return instance;
    }
    ...
}
''' 


<h3> DECORATOR </h3>
Decorator

Problema:
Adicionar funcionalidades a objetos individuais, de forma dinâmica ou estática, sem afetar o comportamento de outras classes e objetos.

Motivação:
Um objeto possui funcionalidades básicas, mas é necessário adicionar a ele novas funcionalidades que podem ser executadas antes ou depois da funcionalidade básica.

Aplicações:
Quando você precisa usar a classe, mas a interface não corresponde ao que você precisa; Para evitar a explosão de subclasses.
![Decorator: sistema](https://media.discordapp.net/attachments/1271502905492504698/1288149788847505408/decorator.png?ex=66f4227a&is=66f2d0fa&hm=e73a963697dc022d697b61467751db4961902defe32c9522c265e7ef445be993&=&format=webp&quality=lossless)

<h3> Observer </h3>

Problema:
Define uma dependência um-para-muitos entre objetos, de modo que, quando um objeto muda de estado, todos os seus dependentes são notificados e atualizados automaticamente.

Motivação:
Quando uma mudança em um objeto implica uma mudança em outros.; Quando um objeto deve poder notificar outros objetos sem assumir nada sobre eles.

Aplicações:
Broadcast.; Publish/Subscribe.; Notificação de eventos.


![Observer figura](https://media.discordapp.net/attachments/1271502905492504698/1288150183363743857/observer.png?ex=66f422d8&is=66f2d158&hm=8f5426fe665089e6c983033a2234122d00e624fa16c100cc011a7f3aecfdf800&=&format=webp&quality=lossless)

<hr>
REFERÊNCIA BIBLIOGRÁFICA

GAMMA, E. et al. Design patterns: abstraction and reuse of object-oriented design.
In:European Conference on Object-Oriented Programming. Berlin, Heidelberg,

1993, p. 406-431.
PRESSMAN, R.; MAXIM, B. R. Engenharia de software: uma abordagem profissional.
8. ed. Porto Alegre: AMGH, 2016.