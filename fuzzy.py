# Instalar a biblioteca SKFUZZY com o comando no prompt: pip install -U scikit-fuzzy
import numpy as np
import skfuzzy as fz
from skfuzzy import control as cf
import matplotlib.pyplot as plt

# Definição das variáveis linguísticas de ENTRADA e de SAÍDA
nivelAgua = cf.Antecedent(np.arange(0, 101, 1), "nivelAgua")  # Varia de 0% a 100% (conforme tabela)
pressao = cf.Antecedent(np.arange(0, 16, 1), "pressao")       # Pressão em PSI, varia de 3 a 15 PSI
acaoControle = cf.Consequent(np.arange(0, 101, 1), "acaoControle")  # Ação de controle (percentual ajustável de 0% a 100%)

# Definição dos Conjuntos Fuzzy para Nível de Água
nivelAgua["zerado"] = fz.trimf(nivelAgua.universe, [0, 0, 25])      # 0 a 25%
nivelAgua["baixo"] = fz.trimf(nivelAgua.universe, [0, 25, 50])      # 25 a 50%
nivelAgua["medio"] = fz.trimf(nivelAgua.universe, [25, 50, 75])     # 50 a 75%
nivelAgua["alto"] = fz.trimf(nivelAgua.universe, [50, 75, 100])     # 75 a 100%
nivelAgua["cheio"] = fz.trimf(nivelAgua.universe, [75, 100, 100])   # Cheio (100%)

# Definição dos Conjuntos Fuzzy para Pressão
pressao["baixa"] = fz.trimf(pressao.universe, [0, 0, 6])            # Baixa pressão
pressao["media"] = fz.trimf(pressao.universe, [3, 9, 15])           # Pressão média
pressao["alta"] = fz.trimf(pressao.universe, [9, 15, 15])           # Alta pressão

# Definição dos Conjuntos Fuzzy para Ação de Controle
acaoControle["minima"] = fz.trimf(acaoControle.universe, [0, 0, 50])  # Ação mínima (0 a 50%)
acaoControle["moderada"] = fz.trimf(acaoControle.universe, [25, 50, 75])  # Ação moderada (25 a 75%)
acaoControle["maxima"] = fz.trimf(acaoControle.universe, [50, 100, 100])  # Ação máxima (50 a 100%)

# Visualização das funções de pertinência
nivelAgua.view()
pressao.view()
acaoControle.view()

# Definição das Regras Fuzzy (baseadas na tabela usada como referência)
r1 = cf.Rule(nivelAgua["zerado"] | pressao["baixa"], acaoControle["minima"])    # Pouca água e baixa pressão -> Controle mínimo
r2 = cf.Rule(nivelAgua["cheio"] | pressao["alta"], acaoControle["maxima"])     # Água cheia e alta pressão -> Controle máximo
r3 = cf.Rule(nivelAgua["medio"] & pressao["media"], acaoControle["moderada"])  # Água média e pressão média -> Controle moderado
r4 = cf.Rule(nivelAgua["baixo"] & pressao["media"], acaoControle["moderada"])  # Pouca água e pressão média -> Controle moderado

# Configuração do Sistema de Controle
criterios = cf.ControlSystem([r1, r2, r3, r4])
resultado = cf.ControlSystemSimulation(criterios)

# Entradas do sistema
resultado.input["nivelAgua"] = 58  # Exemplo: nível de água 58%
resultado.input["pressao"] = 12   # Exemplo: pressão 12 PSI

# Processamento
resultado.compute()

# Resultado defuzzificado
print("Ação de controle defuzzificada:", resultado.output["acaoControle"])
acaoControle.view(sim=resultado)
plt.show()
