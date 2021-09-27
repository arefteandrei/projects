-- MySQL dump 10.13  Distrib 8.0.24, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: assignment_retele_sociale
-- ------------------------------------------------------
-- Server version	8.0.24

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
-- Table structure for table `friendliness`
--

DROP TABLE IF EXISTS `friendliness`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `friendliness` (
  `friendliness_id` int NOT NULL AUTO_INCREMENT,
  `user_1_id` int NOT NULL,
  `user_2_id` int NOT NULL,
  `friendship_status` enum('waiting','accepted','rejected') NOT NULL,
  `friendship_datetime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`friendliness_id`),
  KEY `fk_user_1_id_idx` (`user_1_id`),
  KEY `fk_user_2_id_idx` (`user_2_id`),
  CONSTRAINT `fk_user_1_id` FOREIGN KEY (`user_1_id`) REFERENCES `users` (`user_id`),
  CONSTRAINT `fk_user_2_id` FOREIGN KEY (`user_2_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `friendliness`
--

LOCK TABLES `friendliness` WRITE;
/*!40000 ALTER TABLE `friendliness` DISABLE KEYS */;
INSERT INTO `friendliness` VALUES (1,1,2,'waiting','2021-05-10 01:36:03'),(2,3,5,'accepted','2021-05-10 01:36:57'),(3,2,4,'accepted','2021-05-10 01:37:38'),(4,1,5,'rejected','2021-05-10 01:37:51'),(5,1,3,'waiting','2021-05-10 01:38:22');
/*!40000 ALTER TABLE `friendliness` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `status`
--

DROP TABLE IF EXISTS `status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `status` (
  `status_id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(45) NOT NULL,
  `content` varchar(100) DEFAULT NULL,
  `status_publication_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `user_id` int NOT NULL,
  PRIMARY KEY (`status_id`),
  KEY `fk_user_id_idx` (`user_id`),
  CONSTRAINT `fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `status`
--

LOCK TABLES `status` WRITE;
/*!40000 ALTER TABLE `status` DISABLE KEYS */;
INSERT INTO `status` VALUES (1,'Happy',NULL,'2021-05-10 01:40:26',1),(2,'Happy','Los Angeles','2021-05-10 01:41:08',1),(3,'Eating','Seattle','2021-05-10 01:41:27',3),(4,'Swiming','Miami','2021-05-10 01:41:59',4),(5,'Running','Chicago','2021-05-10 01:42:21',5),(6,'Sad',NULL,'2021-05-10 01:43:12',3),(7,'Bike Ride',NULL,'2021-05-10 01:44:04',2);
/*!40000 ALTER TABLE `status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `date_of_birth` date NOT NULL,
  `place_of_birth` varchar(45) NOT NULL,
  `email` varchar(45) DEFAULT NULL,
  `username` varchar(45) NOT NULL,
  `cv` mediumtext,
  `photo` blob,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Jhon','Smith','1978-09-05','Los Angeles','jhon.smith@yahoo.com','jhonsmith',NULL,NULL),(2,'Bruce','Lee','1922-01-01','Tokyo','bruce.lee@yahoo.com','brucelee',NULL,NULL),(3,'Christian','Gray','1982-11-09','Seattle','christian.gray@yahoo.com','christiangray',NULL,NULL),(4,'Michael','Jackson','1956-08-11','Chicago','michael.jackson@yahoo.com','michaeljackson',NULL,NULL),(5,'Mila','Kunis','1995-12-24','Kiev','mila.kunis@yahoo.com','milakunis',NULL,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-11  0:20:34
