--  SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and
-- store the average score for a student. Note: An average score can be a decimal

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN

    SELECT AVG(score) INTO @avg_score
    FROM corrections
    WHERE corrections.user_id = user_id
    GROUP BY corrections.user_id;

    UPDATE users
    SET average_score = @avg_score
    WHERE users.id = user_id;
END $$
DELIMITER ;
