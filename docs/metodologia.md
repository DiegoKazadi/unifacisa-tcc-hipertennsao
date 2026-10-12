# Metodologia de reprodução

## Referência documental
O TCC descreve quatro classificadores no WEKA: Rede Bayesiana, LogitBoost, Multilayer Perceptron e J48. A seção de coleta cita a base Cleveland Heart Disease com 303 registros e 14 atributos, com preenchimento de três campos ausentes pela moda. O documento também registra resultados de acurácia, sensibilidade e especificidade.

## Procedimento
1. Auditar arquivos e identificar versões/duplicatas.
2. Confirmar a base e a variável-alvo pela metodologia e tabelas do TCC.
3. Recuperar versões do WEKA/Java e configurações dos algoritmos.
4. Replicar pré-processamento e validação conforme o documento.
5. Registrar métricas, matrizes de confusão e divergências.

## Limitação inicial
Nomes de arquivos não comprovam a definição da classe. Cleveland Heart Disease e hipertensão não são conceitos equivalentes; no Framingham, `prevalentHyp` e `TenYearCHD` representam alvos diferentes. Não misturar as bases nem renomear a classe sem evidência documental.
