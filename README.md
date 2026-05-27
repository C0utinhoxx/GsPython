# Mission Control AI - Sistema Inteligente de Monitoramento de Missão Espacial

O Mission Control AI é um sistema desenvolvido em Python focado na simulação e monitoramento de parâmetros críticos em missões aeroespaciais experimentais. O programa recebe e processa dados simulados de telemetria divididos em ciclos, avaliando instantaneamente os riscos de cada indicador, gerando recomendações automáticas de segurança e consolidando as métricas em um relatório geral de encerramento.

## Nome da Missão e Equipe
* **Missão:** New Era
* **Equipe:** Equipe Alpha

## Funcionalidades do Sistema
* **Análise Multivariada:** Processamento síncrono de 5 indicadores de telemetria por ciclo.
* **Cálculo Ponderado de Risco:** Atribuição de pesos de risco (`NORMAL = 0`, `ATENÇÃO = 1`, `CRÍTICO = 2`).
* **Sistema de Recomendação:** Geração de respostas imediatas de segurança baseadas na severidade das falhas.
* **Análise de Tendência:** Comparação algorítmica entre o estado inicial e final da missão.
* **Diagnóstico Estatístico:** Relatório final detalhado com médias aritméticas de performance por sensor.


##  Parâmetros e Regras de Negócio

O sistema avalia cada ciclo com base em intervalos lógicos rígidos para os cinco componentes de telemetria monitorados:

### 1. Temperatura Interna (°C)
* **Abaixo de 18 °C:** ATENÇÃO (Temperatura baixa demais)
* **De 18 °C até 30 °C:** NORMAL (Temperatura estável)
* **De 31 °C até 35 °C:** ATENÇÃO (Temperatura elevada)
* **Acima de 35 °C:** CRÍTICO (Risco de superaquecimento)

### 2. Comunicação com a Base (%)
* **Abaixo de 30%:** CRÍTICO (Comunicação com a base em nível crítico)
* **De 30% até 59%:** ATENÇÃO (Comunicação instável)
* **60% ou mais:** NORMAL (Comunicação estável)

### 3. Sistema de Energia / Bateria (%)
* **Abaixo de 20%:** CRÍTICO (Bateria em nível crítico)
* **De 20% até 49%:** ATENÇÃO (Bateria abaixo do recomendado)
* **50% ou mais:** NORMAL (Energia estável)

### 4. Suporte de Oxigênio (%)
* **Abaixo de 80%:** CRÍTICO (Oxigênio em nível crítico)
* **De 80% até 89%:** ATENÇÃO (Oxigênio abaixo do ideal)
* **90% ou mais:** NORMAL (Oxigênio adequado)

### 5. Estabilidade Operacional (%)
* **Abaixo de 40%:** CRÍTICO (Estabilidade operacional crítica)
* **De 40% até 69%:** ATENÇÃO (Estabilidade operacional reduzida)
* **70% ou mais:** NORMAL (Estabilidade operacional adequada)

### Classificação do Ciclo por Pontuação
A somatória dos pesos individuais de cada parâmetro determina o estado geral do ciclo:
* **0 a 2 pontos:** MISSÃO ESTÁVEL
* **3 a 5 pontos:** MISSÃO EM ATENÇÃO
* **6 a 10 pontos:** MISSÃO CRÍTICA

##  Estrutura de Arquivos do Repositório



## mission_control.py  (Código-fonte principal da aplicação) 
## README.md (Documentação técnica do projeto)