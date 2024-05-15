CREATE DATABASE  IF NOT EXISTS `moringa` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `moringa`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: moringa
-- ------------------------------------------------------
-- Server version	8.4.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `batch_id`
--

DROP TABLE IF EXISTS `batch_id`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `batch_id` (
  `Batch_ID` int NOT NULL AUTO_INCREMENT,
  `RawWeight` int NOT NULL,
  `InTime(Raw)` datetime NOT NULL,
  `InTime(Wet)` datetime NOT NULL,
  `OutTime(Wet)` datetime NOT NULL,
  `WetWeight` int NOT NULL,
  `InTime(Dry)` datetime NOT NULL,
  `OutTime(Dry)` int NOT NULL,
  `Centra_ID` int NOT NULL,
  `DryWeight` int NOT NULL,
  `InTime(Powder)` int NOT NULL,
  `OutTime(Powder)` int NOT NULL,
  `PowderWeight` int NOT NULL,
  `Status` text COLLATE utf8mb4_general_ci NOT NULL,
  `Package_ID` int NOT NULL,
  `WeightRescale` int NOT NULL,
  PRIMARY KEY (`Batch_ID`),
  UNIQUE KEY `Centra_ID` (`Centra_ID`),
  UNIQUE KEY `Package_ID` (`Package_ID`),
  CONSTRAINT `batch_id_ibfk_1` FOREIGN KEY (`Centra_ID`) REFERENCES `centra` (`Centra_ID`) ON UPDATE CASCADE,
  CONSTRAINT `batch_id_ibfk_2` FOREIGN KEY (`Package_ID`) REFERENCES `delivery` (`Package_ID`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `batch_id`
--

LOCK TABLES `batch_id` WRITE;
/*!40000 ALTER TABLE `batch_id` DISABLE KEYS */;
/*!40000 ALTER TABLE `batch_id` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-15 20:10:53
