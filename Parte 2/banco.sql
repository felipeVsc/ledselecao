-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 21-Jun-2021 às 00:18
-- Versão do servidor: 8.0.25
-- versão do PHP: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `banco`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `estabelecimento`
--

CREATE TABLE `estabelecimento` (
  `paciente_id` varchar(50) NOT NULL,
  `estabelecimento_valor` int DEFAULT NULL,
  `estabelecimento_razaosocial` varchar(50) DEFAULT NULL,
  `estalecimento_nofantasia` varchar(50) DEFAULT NULL,
  `estabelecimento_municipio_codigo` int DEFAULT NULL,
  `estabelecimento_municipio_nome` varchar(50) DEFAULT NULL,
  `estabelecimento_uf` varchar(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `pacientes`
--

CREATE TABLE `pacientes` (
  `paciente_id` varchar(50) NOT NULL,
  `paciente_datanascimento` date DEFAULT NULL,
  `paciente_enumsexobiologico` char(1) DEFAULT NULL,
  `paciente_racacor_codigo` int DEFAULT NULL,
  `paciente_racacor_valor` varchar(20) DEFAULT NULL,
  `paciente_endereco_coibgemunicipio` int DEFAULT NULL,
  `paciente_endereco_copais` int DEFAULT NULL,
  `paciente_endereco_nmmunicipio` varchar(50) DEFAULT NULL,
  `paciente_endereco_nmpais` varchar(50) DEFAULT NULL,
  `paciente_endereco_uf` varchar(2) DEFAULT NULL,
  `paciente_endereco_cep` int DEFAULT NULL,
  `paciente_nacionalidade_enumnacionalidade` char(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `vacina`
--

CREATE TABLE `vacina` (
  `paciente_id` varchar(50) NOT NULL,
  `vacina_grupoatendimento_codigo` int DEFAULT NULL,
  `vacina_grupoatendimento_nome` varchar(50) DEFAULT NULL,
  `vacina_categoria_codigo` int DEFAULT NULL,
  `vacina_categoria_nome` varchar(50) DEFAULT NULL,
  `vacina_lote` varchar(50) DEFAULT NULL,
  `vacina_fabricante_nome` varchar(50) DEFAULT NULL,
  `vacina_fabricante_referencia` varchar(50) DEFAULT NULL,
  `vacina_dataaplicacao` date DEFAULT NULL,
  `vacina_descricao_dose` varchar(50) DEFAULT NULL,
  `vacina_codigo` int DEFAULT NULL,
  `vacina_nome` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `estabelecimento`
--
ALTER TABLE `estabelecimento`
  ADD PRIMARY KEY (`paciente_id`);

--
-- Índices para tabela `pacientes`
--
ALTER TABLE `pacientes`
  ADD PRIMARY KEY (`paciente_id`);

--
-- Índices para tabela `vacina`
--
ALTER TABLE `vacina`
  ADD PRIMARY KEY (`paciente_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
