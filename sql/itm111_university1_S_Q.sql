#-------------Begin Forward Engineer-------------
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema university
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `university` ;

-- -----------------------------------------------------
-- Schema university
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `university` DEFAULT CHARACTER SET utf8 ;
USE `university` ;

-- -----------------------------------------------------
-- Table `university`.`term`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `university`.`term` ;

CREATE TABLE IF NOT EXISTS `university`.`term` (
  `term_id` INT NOT NULL,
  `term` VARCHAR(45) NOT NULL,
  `year` INT NOT NULL,
  PRIMARY KEY (`term_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `university`.`faculty`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `university`.`faculty` ;

CREATE TABLE IF NOT EXISTS `university`.`faculty` (
  `faculty_id` INT NOT NULL,
  `faculty_fname` VARCHAR(45) NOT NULL,
  `faculty_lname` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`faculty_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `university`.`college`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `university`.`college` ;

CREATE TABLE IF NOT EXISTS `university`.`college` (
  `college_id` INT NOT NULL,
  `college_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`college_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `university`.`department`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `university`.`department` ;

CREATE TABLE IF NOT EXISTS `university`.`department` (
  `department_id` INT NOT NULL,
  `department_name` VARCHAR(45) NOT NULL,
  `department_code` VARCHAR(45) NOT NULL,
  `college_id` INT NOT NULL,
  PRIMARY KEY (`department_id`),
  INDEX `fk_department_college1_idx` (`college_id` ASC) VISIBLE,
  CONSTRAINT `fk_department_college1`
    FOREIGN KEY (`college_id`)
    REFERENCES `university`.`college` (`college_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `university`.`course`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `university`.`course` ;

CREATE TABLE IF NOT EXISTS `university`.`course` (
  `course_id` INT NOT NULL,
  `course_num` INT NOT NULL,
  `course_title` VARCHAR(45) NOT NULL,
  `credits` INT NOT NULL,
  `department_id` INT NOT NULL,
  PRIMARY KEY (`course_id`),
  INDEX `fk_course_department1_idx` (`department_id` ASC) VISIBLE,
  CONSTRAINT `fk_course_department1`
    FOREIGN KEY (`department_id`)
    REFERENCES `university`.`department` (`department_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `university`.`section`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `university`.`section` ;

CREATE TABLE IF NOT EXISTS `university`.`section` (
  `section_id` INT NOT NULL,
  `section` INT NOT NULL,
  `capacity` INT NOT NULL,
  `term_id` INT NOT NULL,
  `faculty_id` INT NOT NULL,
  `course_id` INT NOT NULL,
  PRIMARY KEY (`section_id`),
  INDEX `fk_section_term_idx` (`term_id` ASC) VISIBLE,
  INDEX `fk_section_faculty1_idx` (`faculty_id` ASC) VISIBLE,
  INDEX `fk_section_course1_idx` (`course_id` ASC) VISIBLE,
  CONSTRAINT `fk_section_term`
    FOREIGN KEY (`term_id`)
    REFERENCES `university`.`term` (`term_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_section_faculty1`
    FOREIGN KEY (`faculty_id`)
    REFERENCES `university`.`faculty` (`faculty_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_section_course1`
    FOREIGN KEY (`course_id`)
    REFERENCES `university`.`course` (`course_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `university`.`student`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `university`.`student` ;

CREATE TABLE IF NOT EXISTS `university`.`student` (
  `student_id` INT NOT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `gender` ENUM('M', 'F') NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  `state` VARCHAR(2) NOT NULL,
  `birthdate` DATE NOT NULL,
  PRIMARY KEY (`student_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `university`.`enrollement`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `university`.`enrollement` ;

CREATE TABLE IF NOT EXISTS `university`.`enrollement` (
  `section_id` INT NOT NULL,
  `student_id` INT NOT NULL,
  PRIMARY KEY (`section_id`, `student_id`),
  INDEX `fk_section_has_student_student1_idx` (`student_id` ASC) VISIBLE,
  INDEX `fk_section_has_student_section1_idx` (`section_id` ASC) VISIBLE,
  CONSTRAINT `fk_section_has_student_section1`
    FOREIGN KEY (`section_id`)
    REFERENCES `university`.`section` (`section_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_section_has_student_student1`
    FOREIGN KEY (`student_id`)
    REFERENCES `university`.`student` (`student_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


#-------------End Forward Engineer---------------
#------------------------------------------------
#-------------Inserts for college table-----------
INSERT INTO college VALUES
	-- id, name
    (1, 'College of Physical Science and Engineering')
    , (2, 'College of Business and Communication')
    , (3, 'College of Language and Letters');
    
#-------------Inserts for department table--------
INSERT INTO department VALUES
	-- id, name, code, college_id
    (1, 'Computer Information Technology', 'CIT', 1)
    , (2, 'Economics', 'ECON', 2)
    , (3, 'Humanities and Philosophy', 'HUM', 3);

#-------------Inserts for course table------------
INSERT INTO course VALUES
	-- id, number, title, credits, department_id
    (1, 111, 'Intro to Databses', 3, 1)
    , (2, 388, 'Econometrics', 4, 2)
    , (3, 150, 'Micro Economics', 3, 2)
    , (4, 376, 'Classical Heritage', 2, 3);

#-------------Inserts for faculty table-----------
INSERT INTO faculty VALUES
	-- id, first name, last name
    (1, 'Marty', 'Morring')
    , (2, 'Nate', 'Nathan')
    , (3, 'Ben', 'Barrus')
    , (4, 'John', 'Jensen')
    , (5, 'Bill', 'Barney');

#-------------Inserts for term table--------------
INSERT INTO term VALUES
	-- id, term, year
    (1, 'Fall', 2019)
    , (2, 'Winter', 2018);

#-------------Inserts for student table-----------
INSERT INTO student VALUES
	-- id, first, last, gender, city, state, birthdate (year-day-month)
	(1,'Paul','Miller','M','Dallas','TX', '1996-02-22')
    , (2,'Katie','Smith','F','Provo','UT', '1995-07-22')
    , (3,'Kelly','Jones','F','Provo','UT', '1998-06-22')
    , (4,'Devon','Merrill','M','Mesa','AZ', '2000-07-22')
    , (5,'Mandy','Murdock','F','Topeka','KS', '1996-11-22')
    , (6,'Alece','Adams','F','Rigby','ID', '1997-05-22')
    , (7,'Bryce','Carlson','M','Bozeman','MT', '1997-11-22')
    , (8,'Preston','Larson','M','Decatur','TN', '1996-09-22')
    , (9,'Julia','Madsen','F','Rexburg','ID', '1998-09-22')
    , (10,'Susan','Sorenson','F','Mesa','AZ', '1998-08-09');
    
#-------------Inserts for section table-----------
INSERT INTO section VALUES
	-- section_id, section, capacity, course_id, faculty_id, year_id) 
	(1,1,30,1,1,1)     -- CIT 111 1 Fall
    , (2,1,50,1,4,2)   -- ECON 150 1 Fall
    , (3,2,50,1,4,2)   -- ECON 150 2 Fall
    , (4,1,35,1,3,4)   -- ECON 388 1 Fall
    , (5,1,30,1,5,3)   -- HUM 376 1 Fall
    , (6,2,30,2,1,1)   -- CIT 111 2 Winter
    , (7,3,35,2,2,1)   -- CIT 111 3 Winter
    , (8,1,50,2,4,2)   -- ECON 150 1 Winter
    , (9,2,50,2,4,2)   -- ECON 150 2 Winter
    , (10,1,30,2,5,3); -- HUM 376 1 Winter
    
#-------------Inserts for enrollment table--------
INSERT INTO enrollement VALUES
	-- section_id, student_id
    (7,6)     -- Alece in CIT 111 Winter 2018 Section 3
    , (6,7)   -- Bryce in CIT 111 Winter 2018 Section 2
    , (8,7)   -- Bryce in ECON 150 Winter 2018 Section 1
    , (10,7)  -- Bryce in HUM 376 Winter 2018 Section 1
    , (5,4)   -- Devon in HUM 376 Fall 2019 Section 1
    , (9,9)   -- Julia in ECON 150 Winter 2018 Section 2
    , (4,2)   -- Katie in ECON 388 Fall 2019 Section 1
    , (4,3)   -- Kelly in ECON 388 Fall 2019 Section 1
    , (4,5)   -- Mandy in ECON 388 Fall 2019 Section 1
    , (5,5)   -- Mandy in HUM 376 Fall 2019 Section 1
    , (1,1)   -- Paul in CIT 111 Fall 2019 Section 1
    , (3,1)   -- Paul in ECON 150 Fall 2019 Section 1
    , (9,8)   -- Preston in ECON 150 Winter 2018 Section 2
    , (6,10); -- Susan in CIT 111 Winter 2018 Section 2
    
    
    
    
    
    
    
    
    
    
    
    
    