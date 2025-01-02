-- MySQL dump 10.16  Distrib 10.1.48-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: db
-- ------------------------------------------------------
-- Server version	10.1.48-MariaDB-0+deb9u2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Authentication_profile`
--

DROP TABLE IF EXISTS `Authentication_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Authentication_profile` (
  `id` varchar(0) DEFAULT NULL,
  `messages` varchar(0) DEFAULT NULL,
  `user_id` varchar(0) DEFAULT NULL,
  `is_lawyer` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Authentication_profile`
--

LOCK TABLES `Authentication_profile` WRITE;
/*!40000 ALTER TABLE `Authentication_profile` DISABLE KEYS */;
/*!40000 ALTER TABLE `Authentication_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` varchar(0) DEFAULT NULL,
  `name` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` varchar(0) DEFAULT NULL,
  `group_id` varchar(0) DEFAULT NULL,
  `permission_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` tinyint(4) DEFAULT NULL,
  `content_type_id` tinyint(4) DEFAULT NULL,
  `codename` varchar(18) DEFAULT NULL,
  `name` varchar(23) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,1,'add_logentry','Can add log entry'),(2,1,'change_logentry','Can change log entry'),(3,1,'delete_logentry','Can delete log entry'),(4,1,'view_logentry','Can view log entry'),(5,2,'add_permission','Can add permission'),(6,2,'change_permission','Can change permission'),(7,2,'delete_permission','Can delete permission'),(8,2,'view_permission','Can view permission'),(9,3,'add_group','Can add group'),(10,3,'change_group','Can change group'),(11,3,'delete_group','Can delete group'),(12,3,'view_group','Can view group'),(13,4,'add_user','Can add user'),(14,4,'change_user','Can change user'),(15,4,'delete_user','Can delete user'),(16,4,'view_user','Can view user'),(17,5,'add_contenttype','Can add content type'),(18,5,'change_contenttype','Can change content type'),(19,5,'delete_contenttype','Can delete content type'),(20,5,'view_contenttype','Can view content type'),(21,6,'add_session','Can add session'),(22,6,'change_session','Can change session'),(23,6,'delete_session','Can delete session'),(24,6,'view_session','Can view session'),(25,7,'add_profile','Can add profile'),(26,7,'change_profile','Can change profile'),(27,7,'delete_profile','Can delete profile'),(28,7,'view_profile','Can view profile'),(29,8,'add_lawyer','Can add lawyer'),(30,8,'change_lawyer','Can change lawyer'),(31,8,'delete_lawyer','Can delete lawyer'),(32,8,'view_lawyer','Can view lawyer'),(33,9,'add_contact','Can add contact'),(34,9,'change_contact','Can change contact'),(35,9,'delete_contact','Can delete contact'),(36,9,'view_contact','Can view contact'),(37,10,'add_billrequest','Can add bill request'),(38,10,'change_billrequest','Can change bill request'),(39,10,'delete_billrequest','Can delete bill request'),(40,10,'view_billrequest','Can view bill request'),(41,11,'add_profile','Can add profile'),(42,11,'change_profile','Can change profile'),(43,11,'delete_profile','Can delete profile'),(44,11,'view_profile','Can view profile');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` tinyint(4) DEFAULT NULL,
  `password` varchar(88) DEFAULT NULL,
  `last_login` varchar(10) DEFAULT NULL,
  `is_superuser` tinyint(4) DEFAULT NULL,
  `username` varchar(5) DEFAULT NULL,
  `last_name` varchar(0) DEFAULT NULL,
  `email` varchar(22) DEFAULT NULL,
  `is_staff` tinyint(4) DEFAULT NULL,
  `is_active` tinyint(4) DEFAULT NULL,
  `date_joined` varchar(10) DEFAULT NULL,
  `first_name` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$KwY9Bv26FANd8S6QgwAhT5$2QmxmbWgzXqnVZ1DhliPX2lAts37qvUuWY64AxoOSBc=','2024-12-30',1,'admin','','',1,1,'2024-12-30',''),(2,'pbkdf2_sha256$600000$xTVSYeZ5wudbARbYFTbSMB$a6TPDwDrWD/hBnoOItNsNw4q3vdwlxBr7MQ4jZcv9xo=','2024-12-30',0,'nima','','taherinima29@gmail.com',0,1,'2024-12-30','');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` varchar(0) DEFAULT NULL,
  `user_id` varchar(0) DEFAULT NULL,
  `group_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` varchar(0) DEFAULT NULL,
  `user_id` varchar(0) DEFAULT NULL,
  `permission_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` varchar(0) DEFAULT NULL,
  `object_id` varchar(0) DEFAULT NULL,
  `object_repr` varchar(0) DEFAULT NULL,
  `action_flag` varchar(0) DEFAULT NULL,
  `change_message` varchar(0) DEFAULT NULL,
  `content_type_id` varchar(0) DEFAULT NULL,
  `user_id` varchar(0) DEFAULT NULL,
  `action_time` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` tinyint(4) DEFAULT NULL,
  `app_label` varchar(14) DEFAULT NULL,
  `model` varchar(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (11,'Authentication','profile'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(10,'home','billrequest'),(9,'home','contact'),(8,'home','lawyer'),(7,'home','profile'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` tinyint(4) DEFAULT NULL,
  `app` varchar(14) DEFAULT NULL,
  `name` varchar(55) DEFAULT NULL,
  `applied` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-12-30'),(2,'auth','0001_initial','2024-12-30'),(3,'admin','0001_initial','2024-12-30'),(4,'admin','0002_logentry_remove_auto_add','2024-12-30'),(5,'admin','0003_logentry_add_action_flag_choices','2024-12-30'),(6,'contenttypes','0002_remove_content_type_name','2024-12-30'),(7,'auth','0002_alter_permission_name_max_length','2024-12-30'),(8,'auth','0003_alter_user_email_max_length','2024-12-30'),(9,'auth','0004_alter_user_username_opts','2024-12-30'),(10,'auth','0005_alter_user_last_login_null','2024-12-30'),(11,'auth','0006_require_contenttypes_0002','2024-12-30'),(12,'auth','0007_alter_validators_add_error_messages','2024-12-30'),(13,'auth','0008_alter_user_username_max_length','2024-12-30'),(14,'auth','0009_alter_user_last_name_max_length','2024-12-30'),(15,'auth','0010_alter_group_name_max_length','2024-12-30'),(16,'auth','0011_update_proxy_permissions','2024-12-30'),(17,'auth','0012_alter_user_first_name_max_length','2024-12-30'),(18,'home','0001_initial','2024-12-30'),(19,'sessions','0001_initial','2024-12-30'),(20,'Authentication','0001_initial','2024-12-30'),(21,'home','0002_alter_billrequest_user_alter_contact_user_and_more','2024-12-30'),(22,'Authentication','0002_profile_is_lawyer','2024-12-30');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(32) DEFAULT NULL,
  `session_data` varchar(54) DEFAULT NULL,
  `expire_date` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('3ng5au8gqe6ncg6vl23qs7lyuidbhlrz','e30:1tS6Ad:wcJ3xMDIS0putpiEjuE7QOcreXUK4jMNBQx1WOYYEKs','2025-01-13');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_billrequest`
--

DROP TABLE IF EXISTS `home_billrequest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_billrequest` (
  `id` varchar(0) DEFAULT NULL,
  `username` varchar(0) DEFAULT NULL,
  `file` varchar(0) DEFAULT NULL,
  `user_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_billrequest`
--

LOCK TABLES `home_billrequest` WRITE;
/*!40000 ALTER TABLE `home_billrequest` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_billrequest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_contact`
--

DROP TABLE IF EXISTS `home_contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_contact` (
  `id` varchar(0) DEFAULT NULL,
  `name` varchar(0) DEFAULT NULL,
  `email` varchar(0) DEFAULT NULL,
  `phone` varchar(0) DEFAULT NULL,
  `subject` varchar(0) DEFAULT NULL,
  `message` varchar(0) DEFAULT NULL,
  `is_read` varchar(0) DEFAULT NULL,
  `subject_type` varchar(0) DEFAULT NULL,
  `date` varchar(0) DEFAULT NULL,
  `user_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_contact`
--

LOCK TABLES `home_contact` WRITE;
/*!40000 ALTER TABLE `home_contact` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_lawyer`
--

DROP TABLE IF EXISTS `home_lawyer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_lawyer` (
  `id` varchar(0) DEFAULT NULL,
  `name` varchar(0) DEFAULT NULL,
  `email` varchar(0) DEFAULT NULL,
  `phone` varchar(0) DEFAULT NULL,
  `address` varchar(0) DEFAULT NULL,
  `city` varchar(0) DEFAULT NULL,
  `state` varchar(0) DEFAULT NULL,
  `zip_code` varchar(0) DEFAULT NULL,
  `experience` varchar(0) DEFAULT NULL,
  `is_active` varchar(0) DEFAULT NULL,
  `date` varchar(0) DEFAULT NULL,
  `image` varchar(0) DEFAULT NULL,
  `subject_type` varchar(0) DEFAULT NULL,
  `user_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_lawyer`
--

LOCK TABLES `home_lawyer` WRITE;
/*!40000 ALTER TABLE `home_lawyer` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_lawyer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sqlite_sequence`
--

DROP TABLE IF EXISTS `sqlite_sequence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sqlite_sequence` (
  `name` varchar(22) DEFAULT NULL,
  `seq` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sqlite_sequence`
--

LOCK TABLES `sqlite_sequence` WRITE;
/*!40000 ALTER TABLE `sqlite_sequence` DISABLE KEYS */;
INSERT INTO `sqlite_sequence` VALUES ('django_migrations',22),('django_admin_log',0),('django_content_type',11),('auth_permission',44),('auth_group',0),('auth_user',2),('home_billrequest',0),('home_contact',0),('home_lawyer',0),('Authentication_profile',0);
/*!40000 ALTER TABLE `sqlite_sequence` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-30 16:42:47
