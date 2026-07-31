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