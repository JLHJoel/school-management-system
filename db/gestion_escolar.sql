-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 20, 2025 at 09:22 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gestion_escolar`
--

-- --------------------------------------------------------

--
-- Table structure for table `asistencias`
--

CREATE TABLE `asistencias` (
  `id` int(11) NOT NULL,
  `id_estudiante` int(11) NOT NULL,
  `id_materia` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `presente` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `calificaciones`
--

CREATE TABLE `calificaciones` (
  `id` int(11) NOT NULL,
  `id_estudiante` int(11) NOT NULL,
  `id_materia` int(11) NOT NULL,
  `calificacion` decimal(5,2) NOT NULL,
  `fecha_registro` date DEFAULT curdate()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `estudiantes`
--

CREATE TABLE `estudiantes` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `matricula` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `id_maestro` int(11) NOT NULL,
  `asistencia_total` int(11) DEFAULT 0,
  `promedio` decimal(5,2) DEFAULT 0.00
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `estudiantes`
--

INSERT INTO `estudiantes` (`id`, `nombre`, `apellido`, `matricula`, `password`, `id_maestro`, `asistencia_total`, `promedio`) VALUES
(4, 'Carlos', 'Salinas', '1274294', 'scrypt:32768:8:1$tJli2S7Nv1R1FF03$d34e9facbc331dd22eace1f126403a5478023f284688aed713098e89cf5a13b890d314f61af68f7d41a611c2e8401ef2cbab3ac7b91a56b8b1ae384798632fc9', 1, 20, 75.00),
(5, 'Roberto', 'Gomez Bolaños', '3241534', 'scrypt:32768:8:1$tqkBFWhC2mS973TB$c3f6d2f825045053238b5a99a51cc3aaaba56da16d6314d83a6c43c91a3552e83458056c1a94fbbc561b7ba7169e19de02b7bcc693e70f4dde973675c47c7b94', 1, 0, 0.00),
(6, 'Carlos', 'Villagran', '434121', 'scrypt:32768:8:1$KlaWXL2SPG6R5ZGH$2ce138d3266a03c8e983428bdc952aaa12fc4955be5679f5f02958c892e2b21293b59eb254798da3aa6d331899aaaed3ba979d67317e9b93a68fde376a4bc07f', 1, 0, 0.00),
(7, 'Nose', 'Nose', '43243441', 'scrypt:32768:8:1$iCKaObqGEhhbjGR9$bbeda729ac76a34f2c7c9dcbf191b5b4871d17a7e02aff057aa71afebe97b51488ede021bc6dc7131db35e37846ccf4b407e7b6a605d8dfacf07f0fa2ba1eaf8', 1, 0, 0.00),
(8, 'JOEL', 'nose', '12343422', 'scrypt:32768:8:1$mK9Jnj07aqXhuSV1$701238fef982f4a9ce4dbe4cd234644534913d357733d2438fda4a19eba119a7cd8a7c33ae000e8639ccfb7fb3633e2d6f5e48c93ae2b66fa5190163741ee031', 1, 0, 0.00),
(9, 'adasd', 'dasdas', '2312414', 'scrypt:32768:8:1$7XBEx1YxfDyASxjS$98a314d9c822c1a8fed76b4de7ecb09d8de47216cf96a87e8d6b295e03266f3371787e666d01eb6ceb303743e49749c46e32405b08cf8794586589dcecd3d41f', 1, 0, 0.00);

-- --------------------------------------------------------

--
-- Table structure for table `maestros`
--

CREATE TABLE `maestros` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `fecha_registro` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `maestros`
--

INSERT INTO `maestros` (`id`, `nombre`, `apellido`, `email`, `password`, `fecha_registro`) VALUES
(1, 'Joel', 'Lozano', 'lozano.joel@uabc.edu.mx', 'scrypt:32768:8:1$7h499pL3r0J8ArFd$2d25444344420f352072ddc9f8f6f9ef8e727df61a3c7c34c85ce07972a5229d8d7dd536c3fe6f8fde21ad560664d29c54e26ef49f2eb51958797ddd04f9506c', '2025-05-19 16:09:30');

-- --------------------------------------------------------

--
-- Table structure for table `materias`
--

CREATE TABLE `materias` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` text DEFAULT NULL,
  `id_maestro` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `asistencias`
--
ALTER TABLE `asistencias`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_estudiante` (`id_estudiante`),
  ADD KEY `id_materia` (`id_materia`);

--
-- Indexes for table `calificaciones`
--
ALTER TABLE `calificaciones`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_estudiante` (`id_estudiante`),
  ADD KEY `id_materia` (`id_materia`);

--
-- Indexes for table `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `matricula` (`matricula`),
  ADD KEY `fk_id_maestro` (`id_maestro`);

--
-- Indexes for table `maestros`
--
ALTER TABLE `maestros`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `materias`
--
ALTER TABLE `materias`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_maestro` (`id_maestro`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `asistencias`
--
ALTER TABLE `asistencias`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `calificaciones`
--
ALTER TABLE `calificaciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `estudiantes`
--
ALTER TABLE `estudiantes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `maestros`
--
ALTER TABLE `maestros`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `materias`
--
ALTER TABLE `materias`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `asistencias`
--
ALTER TABLE `asistencias`
  ADD CONSTRAINT `asistencias_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiantes` (`id`),
  ADD CONSTRAINT `asistencias_ibfk_2` FOREIGN KEY (`id_materia`) REFERENCES `materias` (`id`);

--
-- Constraints for table `calificaciones`
--
ALTER TABLE `calificaciones`
  ADD CONSTRAINT `calificaciones_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiantes` (`id`),
  ADD CONSTRAINT `calificaciones_ibfk_2` FOREIGN KEY (`id_materia`) REFERENCES `materias` (`id`);

--
-- Constraints for table `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD CONSTRAINT `fk_id_maestro` FOREIGN KEY (`id_maestro`) REFERENCES `maestros` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `materias`
--
ALTER TABLE `materias`
  ADD CONSTRAINT `materias_ibfk_1` FOREIGN KEY (`id_maestro`) REFERENCES `maestros` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
