-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: localhost    Database: moulay_rachid
-- ------------------------------------------------------
-- Server version	5.7.29-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `posts` (
  `title` varchar(50) DEFAULT NULL,
  `author` varchar(50) DEFAULT NULL,
  `file` varchar(150) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `subject` varchar(100) DEFAULT NULL,
  `field` varchar(50) DEFAULT NULL,
  `post_id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`post_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
INSERT INTO `posts` VALUES ('tonalité','hanan','tonalité.pdf','2020-04-10 21:50:34','fr','[\'1BSMF\', \'1BSMA\', \'1BSEX\']',3),('énonciation','Nawal SADIK','Ã©nonciation.pdf','2020-04-10 22:41:32','fr','[\'1BSMF\', \'1BSMA\', \'1BSEX\']',4),('tkhrbik','bouchera','le discours direct et indirect.pdf','2020-04-10 22:41:32','fr','[\'1BSMF\', \'1BSMA\', \'1BSEX\']',5),('test 1','Nawal SADIK','fiche-de-lecture-Antigone.pdf','2020-04-12 13:05:47','fr','[\'1BSMA\']',6),('test 2','Nawal SADIK','I.docx','2020-04-12 13:05:47','fr','[\'1BSMA\']',7),('test3','Nawal SADIK','I.docx','2020-04-12 13:05:47','fr','[\'1BSEX\', \'2BSMF\', \'2BSEX\']',8),('test 5','Nawal SADIK','le discours direct et indirect.pdf','2020-04-12 13:05:47','fr','[\'1BSMA\', \'2BSMA\']',9),('jhg','Nawal SADIK','tonalité.pdf','2020-04-12 13:05:47','fr','[\'1BSMA\', \'2BSMA\']',10),('jhv','Nawal SADIK','le discours direct et indirect.pdf','2020-04-12 13:05:47','fr','[\'1BSEX\']',11);
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-13 23:00:17
