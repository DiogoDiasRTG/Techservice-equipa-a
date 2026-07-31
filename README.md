# Equipa A - Técnicos

Módulo responsável pela gestão de técnicos no sistema **TechService**.

## Descrição

Este repositório contém a implementação da entidade **Técnicos**, responsável por armazenar e gerir a informação dos técnicos que executam as ordens de serviço.

## Responsabilidades

- **CRUD de Técnicos** - criação, leitura, atualização e remoção (lógica) de registos de técnicos.
- **Atribuição de Técnicos às Ordens de Serviço** - através da chave estrangeira `id_tecnico` na tabela `ordens_servico`.

## Relacionamentos

A tabela `tecnicos` relaciona-se com a tabela `ordens_servico` através de uma chave estrangeira (FK), permitindo associar cada ordem de serviço a um técnico responsável.

## Equipa

**Equipa A - Técnicos**

- Andre Augusto
- Diogo Dias
- João Martins
- Maria Ribeiro
- Miguel Neves
