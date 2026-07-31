# Equipa A - Técnicos

Módulo responsável pela gestão de técnicos no sistema **TechService**.

## Descrição

Este repositório contém a implementação da entidade **Técnicos**, responsável por armazenar e gerir a informação dos técnicos que executam as ordens de serviço.

## Tabela: Tecnicos

| Campo | Tipo | Descrição |
|---|---|---|
| `id_tecnico` (PK) | INT | Identificador único |
| `nome` | VARCHAR(150) | Nome do técnico |
| `telefone` | VARCHAR(20) | Contacto |
| `email` | VARCHAR(150) | Email |
| `especialidade` | VARCHAR(100) | Área de especialidade |
| `ativo` | TINYINT(1) | Ativo (1) ou Inativo (0) |
| `criado_em` | DATETIME | Data do registo |

### Script SQL de criação

```sql
CREATE TABLE tecnicos (
    id_tecnico      INT AUTO_INCREMENT,
    nome            VARCHAR(150)    NOT NULL,
    telefone        VARCHAR(20)     NULL,
    email           VARCHAR(150)    NULL,
    especialidade   VARCHAR(100)    NULL,
    ativo           TINYINT(1)      NOT NULL DEFAULT 1,
    criado_em       DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id_tecnico)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

## Tabelas criadas

<img width="1842" height="1652" alt="image" src="https://github.com/user-attachments/assets/dcdce4a6-3332-4528-9d5c-faf49369b256" />

## Responsabilidades

- **CRUD de Técnicos** - criação, leitura, atualização e remoção (lógica) de registos de técnicos.
- **Atribuição de Técnicos às Ordens de Serviço** - através da chave estrangeira `id_tecnico` na tabela `ordens_servico`.

## Equipa desenvolvedora

**Equipa A - Técnicos**
- Andre Augusto
- Diogo Dias
- João Martins
- Maria Ribeiro
- Miguel Neves

## 📄 Licença

Este projeto está sob a licença que a organização definir para o repositório principal.
