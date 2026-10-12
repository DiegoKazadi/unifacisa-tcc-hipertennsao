<<<<<<< HEAD
# UNIFACISA — TCC Hipertensão
=======
# unifacisa-tcc-hipertensao
Reprodução experimental do TCC da UNIFACISA sobre aprendizagem de máquina aplicada à previsão de hipertensão arterial, com preparação do ambiente, análise dos dados e comparação de modelos.
>>>>>>> 26429452d1ce07cf7b2d8dec8778109c8ce24371

Repositório de reprodução experimental do TCC **Aplicando Modelos de Aprendizagem de Máquina para Prever Hipertensão Arterial: Uma Análise Comparativa**, defendido em 07/12/2020, em Campina Grande — PB.

## Objetivos
- Organizar e auditar os arquivos originais.
- Identificar a base e o atributo-alvo usados no TCC.
- Recuperar o ambiente WEKA/Java e os parâmetros dos modelos.
- Reproduzir Redes Bayesianas, LogitBoost, Multilayer Perceptron e J48.
- Comparar métricas calculadas com os resultados documentados.

## Estrutura
- `data/raw/`: dados recebidos, preservados sem alteração.
- `data/processed/`: dados derivados após documentar o pré-processamento.
- `src/`: scripts de auditoria, preparação, modelos e avaliação.
- `notebooks/`: exploração de dados.
- `results/`: tabelas, figuras e artefatos históricos.
- `docs/`: TCC original e documentação.

## Primeiro passo
Com Python 3.10+ instalado, execute na raiz do repositório:

```powershell
python src/audit_data.py
```

O script faz somente leitura dos arquivos em `data/raw/` e grava um inventário em `results/tables/data_inventory.csv`.

## Atenção metodológica
Os arquivos Cleveland estão rotulados em alguns lugares como hipertensão, mas são descritos no próprio TCC como Cleveland Heart Disease. O arquivo Framingham contém `prevalentHyp` (hipertensão prevalente) e `TenYearCHD` (doença cardíaca coronariana em dez anos), que são alvos diferentes. **Não treinar nem interpretar modelos como preditores de hipertensão até confirmar no TCC qual coluna foi usada como classe.** Os arquivos brutos não serão alterados.

## Estado
Etapa inicial: estruturação e auditoria dos dados. Resultados ainda não reproduzidos.

## Contexto acadêmico
UNIFACISA · Bacharelado em Sistemas de Informação · Defesa em 7 de dezembro de 2020 · Campina Grande, Paraíba, Brasil.

Uso acadêmico e experimental; os modelos não são ferramentas clínicas validadas. Licenças e condições de redistribuição dos dados devem ser verificadas antes de publicação.
