# Flask S3 Uploader

This is a basic example showing how to use Flask, Flask-WTF and Boto3
to automatically upload user files to S3, bypassing storage on the server.

## Quick Start

Update config.py with your Amazon details.

## Other Notes

The most efficient way of handling the downloads is likely to be
just upload the file to the local webserver to enable a quick
as possible response to the user, then adding the "upload to S3"
task to a message/task queue that runs in the background as the
server can manage.

Requisitos
 - um ou mais serviços de computação: EC2, ECS e/ou Lambda
 - um serviço de banco de dados: RDS ou DynamoDB
 - um serviço de armazenamento: S3

Espera-se apenas que a aplicação seja implantada via CodeDeploy a partir de um repositório do GitHub usando o recurso GitHub Actions.

Quais serviços do provedor de nuvem foram utilizados? Descrever brevemente cada um dos serviços, sua classificação (IaaS, PaaS e SaaS) e sua função dentro da arquitetura;
Qual o resultado da análise de custo?
 - Como cada serviço é cobrado? Explique o modelo de precificação dos serviços utilizados.
 - Qual valor mínimo e valor esperado mensal estimado? Explique como esses dois cenários foram elaborados (mesmo que seja um "chute", precisa ser explicado ;-)) e a metodologia usada para chegar nos custos mensais.

TF_ AnaCarolinaFerreira.pdf


1. Configuração de implantação automática de código em EC2 com CodeDeploy (AWS Academy)
- instancia trabalho
- abrir PR da branch para a main

2. Configuração de implantação automática de código com GitHub Actions.
