-- SQL script that creates a stored procedure
-- AddBonus that adds a new correction for a student.

DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE proid INT;

    IF ((SELECT id FROM projects WHERE name = project_name) <=> NULL)
    THEN
        INSERT INTO projects (projects.name) VALUES(project_name);
    END IF;

    SELECT id INTO proid FROM projects WHERE name = project_name;

    INSERT INTO corrections (corrections.user_id, project_id, score)
    VALUES(user_id, proid, score);
END $$
DELIMITER ;
