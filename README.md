# IA-ControladorPressaoCaldeira
Este algoritmo utiliza-se da biblioteca SKFuzzy para criação de um sistema que retorna a resposta correta para um controlador de válvula na qual é responsável por alimentar o tambor d'água de uma caldeira gerando na qual gera pressão que juntamente com o calor resulta em vapor.

O controle de nível de água em caldeiras é um sistema importante para garantir o funcionamento seguro e eficiente desses equipamentos industriais. Aqui estão os principais pontos sobre como ocorre esse controle:

Funcionamento Básico

1. O sistema consiste em três componentes principais [2][3]:

   - Transmissor de nível (LT): Detecta continuamente o nível de água no tambor de vapor e gera um sinal eletrônico ou pneumático.
   
   - Controlador (LIC): Compara o sinal do transmissor com um valor de set-point definido pelo operador e gera um sinal de controle.
   
   - Válvula de controle: Regula a vazão de água na caldeira em resposta ao sinal do controlador.

2. O transmissor geralmente usa um sinal de 4-20 mA para indicar o nível de água [2].

3. O controlador compara o sinal do transmissor com o set-point e ajusta a posição da válvula para manter o nível constante [2][3].

[4]

Importância e Benefícios

1. Garante eficiência operacional:
   - Evita ressecamento dos tubos de água, prevenindo danos catastróficos [3].
   - Previne transporte excessivo de água líquida junto com o vapor [3].

2. Melhora a segurança:
   - Mantém o nível de água dentro de limites seguros, evitando riscos de explosão [3].
   - Permite operação contínua da caldeira sem interrupções [2].

3. Facilita o controle operacional:
   - Oferece um modo manual para ajustes rápidos durante inicialização e parada [3].
   - Permite diagnóstico de problemas através do controle direto da válvula [3].

Considerações Técnicas

1. O sistema pode usar tecnologia pneumática ou eletrônica para o controle [2][3].

2. Em sistemas pneumáticos, comuns são faixas de pressão de 3-15 PSI ou 3-27 PSI [3].

3. O controlador ajusta continuamente a posição da válvula em resposta às variações de carga e demanda de vapor [2][3].

4. É possível ajustar o set-point para diferentes condições operacionais [2].

Em resumo, o controle de nível de água em caldeiras é essencial para garantir eficiência, segurança e confiabilidade no funcionamento desses equipamentos industriais críticos. Ele permite manter condições ideais para produção de vapor, prevenir danos e facilitar o controle operacional.

Imagens referente ao código, e entrada dos dados

Definição das variáveis linguísticas de ENTRADA e de SAÍDA:
nivelAgua = cf.Antecedent(np.arange(0, 101, 1), "nivelAgua")  # Varia de 0% a 100% (conforme tabela)
pressao = cf.Antecedent(np.arange(0, 16, 1), "pressao")       # Pressão em PSI, varia de 3 a 15 PSI
acaoControle = cf.Consequent(np.arange(0, 101, 1), "acaoControle")  # Ação de controle (percentual ajustável de 0% a 100%)


Definição dos Conjuntos Fuzzy para Pressão:
pressao["baixa"] = fz.trimf(pressao.universe, [0, 0, 6])            # Baixa pressão
pressao["media"] = fz.trimf(pressao.universe, [3, 9, 15])           # Pressão média
pressao["alta"] = fz.trimf(pressao.universe, [9, 15, 15])           # Alta pressão


Definição dos Conjuntos Fuzzy para Ação de Controle:
acaoControle["minima"] = fz.trimf(acaoControle.universe, [0, 0, 50])  # Ação mínima (0 a 50%)
acaoControle["moderada"] = fz.trimf(acaoControle.universe, [25, 50, 75])  # Ação moderada (25 a 75%)
acaoControle["maxima"] = fz.trimf(acaoControle.universe, [50, 100, 100])  # Ação máxima (50 a 100%)


Definição das regras baseadas na tabela mencionada anteriormente e todas as demais explicações fornecidas no site [3].
r1 = cf.Rule(nivelAgua["zerado"] | pressao["baixa"], acaoControle["minima"])    # Pouca água e baixa pressão -> Controle mínimo
r2 = cf.Rule(nivelAgua["cheio"] | pressao["alta"], acaoControle["maxima"])     # Água cheia e alta pressão -> Controle máximo
r3 = cf.Rule(nivelAgua["medio"] & pressao["media"], acaoControle["moderada"])  # Água média e pressão média -> Controle moderado
r4 = cf.Rule(nivelAgua["baixo"] & pressao["media"], acaoControle["moderada"])  # Pouca água e pressão média -> Controle moderado


Entradas para o algoritmo:
resultado.input["nivelAgua"] = 58  # Exemplo: nível de água 58%
resultado.input["pressao"] = 12   # Exemplo: pressão 12 PSI


Referências:
[1] https://lincebrasil.com/medicao-de-nivel-em-caldeiras-como-funciona/
[2] https://www.dicasdeinstrumentacao.com/controle-de-nivel-em-caldeiras/
[3] https://www.dicasdeinstrumentacao.com/sistema-de-controle-de-nivel-de-agua-de-caldeira-pneumatico/
[4] https://vaporparalaindustria.com/pt/instalacion-de-controles-de-nivel-de-agua-en-calderas-de-vapor/
[5] https://www.youtube.com/watch?v=GHsqtD2DqDc
[6] https://www.youtube.com/watch?v=C9dlXOAjxdc
[7] https://pt.linkedin.com/pulse/controle-de-n%C3%ADvel-em-caldeiras-aquatubulares-e-eng%C2%BA-denilson-camargo-xxknf
[8] https://pt.chemtreat.com/water-essentials-handbook-fundamentals-of-industrial-boilers-and-steam-generation-systems/
[9] https://vaporparalaindustria.com/pt/alarmas-de-nivel-de-agua-en-calderas-de-vapor/
[10] https://www.kufunda.net/publicdocs/Automa%C3%A7%C3%A3o%20Industrial%20(Marco%20Antonio%20Ribeiro).pdf
