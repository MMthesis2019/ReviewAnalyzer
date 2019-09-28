CREATE DATABASE ReviewsDB2;
USE ReviewsDB2;

CREATE TABLE `places` (
  `place_id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `location` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `category` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`place_id`)
);

CREATE TABLE `reviews` (
  `review_id` int(10) NOT NULL,
  `name` varchar(500) COLLATE utf8mb4_bin DEFAULT NULL,
  `title` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `review_text` mediumtext COLLATE utf8mb4_bin,
  `review_date` date DEFAULT NULL,
  `rating` tinyint(4) DEFAULT NULL,
  `exp_date` date DEFAULT NULL,
  `helpful` int(5) DEFAULT NULL,
  `author_helpful` int(5) DEFAULT NULL,
  `author_all` int(5) DEFAULT NULL,
  `SOURCE_URL` varchar(700) COLLATE utf8mb4_bin DEFAULT NULL,
  `place_id` int(10) DEFAULT NULL,
  PRIMARY KEY (`review_id`),
  KEY `place_id` (`place_id`),
  CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`place_id`) REFERENCES `places` (`place_id`)
);