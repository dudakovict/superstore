-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: superstore
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `country`
--

DROP TABLE IF EXISTS `country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `country` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `region_fk` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`),
  KEY `region_id` (`region_fk`),
  CONSTRAINT `region_id` FOREIGN KEY (`region_fk`) REFERENCES `region` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=148 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `country`
--

LOCK TABLES `country` WRITE;
/*!40000 ALTER TABLE `country` DISABLE KEYS */;
INSERT INTO `country` VALUES (1,'Algeria',1),(2,'Australia',2),(3,'Hungary',3),(4,'Sweden',4),(5,'Bangladesh',5),(6,'United States',6),(7,'Angola',1),(8,'China',7),(9,'Panama',8),(10,'Iran',3),(11,'France',8),(12,'Italy',9),(13,'Germany',8),(14,'Canada',10),(15,'United Kingdom',4),(16,'Ukraine',3),(17,'Japan',7),(18,'Indonesia',11),(19,'Nigeria',1),(20,'South Korea',7),(21,'Peru',9),(22,'Philippines',11),(23,'Colombia',9),(24,'Ireland',4),(25,'Nicaragua',8),(26,'Mexico',4),(27,'Brazil',9),(28,'Turkey',3),(29,'Spain',9),(30,'Poland',3),(31,'India',5),(32,'Somalia',1),(33,'El Salvador',8),(34,'Sudan',1),(35,'Slovakia',3),(36,'Egypt',1),(37,'Saudi Arabia',3),(38,'Democratic Republic of the Congo',1),(39,'Norway',4),(40,'New Zealand',2),(41,'Kenya',1),(42,'Cuba',13),(43,'Venezuela',9),(44,'Singapore',11),(45,'Honduras',8),(46,'Tanzania',1),(47,'Dominican Republic',13),(48,'Morocco',1),(49,'Albania',3),(50,'Belgium',8),(51,'Afghanistan',5),(52,'Bolivia',9),(53,'Vietnam',11),(54,'Guatemala',8),(55,'Guinea-Bissau',1),(56,'Thailand',11),(57,'Iraq',3),(58,'Myanmar (Burma)',11),(59,'Ecuador',9),(60,'Netherlands',8),(61,'Ghana',1),(62,'Cote d\'Ivoire',1),(63,'Austria',3),(64,'Argentina',9),(65,'Madagascar',1),(66,'Russia',3),(67,'South Africa',1),(68,'Bosnia and Herzegovina',3),(69,'Malaysia',11),(70,'Romania',3),(71,'Israel',3),(72,'Burundi',1),(73,'Cameroon',1),(74,'Paraguay',9),(75,'Senegal',1),(76,'Georgia',3),(77,'Kazakhstan',3),(78,'United Arab Emirates',3),(79,'Pakistan',5),(80,'Liberia',1),(81,'Czech Republic',3),(82,'Jamaica',13),(83,'Benin',1),(84,'Taiwan',7),(85,'Rwanda',1),(86,'Switzerland',8),(87,'Denmark',4),(88,'Haiti',13),(89,'Qatar',3),(90,'Chile',9),(91,'Bulgaria',3),(92,'Mozambique',1),(93,'Lebanon',3),(94,'Barbados',13),(95,'Uzbekistan',3),(96,'Moldova',3),(97,'Cambodia',11),(98,'Guinea',1),(99,'Azerbaijan',3),(100,'Zambia',1),(101,'Uruguay',9),(102,'Portugal',9),(103,'Uganda',1),(104,'Martinique',13),(105,'Togo',1),(106,'Zimbabwe',1),(107,'Finland',4),(108,'Belarus',3),(109,'Libya',1),(110,'Lithuania',3),(111,'Republic of the Congo',1),(112,'Tunisia',1),(113,'Papua New Guinea',2),(114,'Turkmenistan',3),(115,'Yemen',3),(116,'Trinidad and Tobago',13),(117,'Kyrgyzstan',3),(118,'Croatia',3),(119,'Nepal',5),(120,'Mali',1),(121,'Namibia',1),(122,'Syria',3),(123,'Sierra Leone',1),(124,'Gabon',1),(125,'Mauritania',1),(126,'Guadeloupe',13),(127,'Niger',1),(128,'Sri Lanka',5),(129,'Djibouti',1),(130,'Jordan',3),(131,'Equatorial Guinea',1),(132,'Hong Kong',7),(133,'Mongolia',3),(134,'Eritrea',1),(135,'Slovenia',3),(136,'Ethiopia',1),(137,'Tajikistan',3),(138,'Montenegro',3),(139,'Central African Republic',1),(140,'Lesotho',1),(141,'Chad',1),(142,'Armenia',3),(143,'Swaziland',1),(144,'Estonia',3),(145,'South Sudan',1),(146,'Bahrain',3),(147,'Macedonia',3);
/*!40000 ALTER TABLE `country` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-26 12:56:43
