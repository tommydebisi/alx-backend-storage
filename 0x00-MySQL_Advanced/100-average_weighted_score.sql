-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE pro_id, scor, weighted, done_l INT DEFAULT 0;
    DECLARE weigh_score, avg_weighted, weigh_sum INT DEFAULT 0;

    DECLARE curs_1 CURSOR FOR
    SELECT project_id, score FROM corrections
    WHERE corrections.user_id = user_id;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done_l = 1;

    OPEN curs_1;

    getAvgWeight: LOOP
        -- FETCH values in each row and store them
        FETCH curs_1 INTO pro_id, scor;

        IF (done_l = 1)
        THEN
            LEAVE getAvgWeight;
        END IF;
        -- get weighted value
        SELECT projects.weight INTO weighted
        FROM projects
        WHERE projects.id = pro_id;

        -- get summation of the product weighted val and score
        SET weigh_score = weigh_score + (weighted * scor);

        -- get summation of initial weighted val and current weighted val
        SET weigh_sum = weigh_sum + weighted;
    END LOOP getAvgWeight;

    SET avg_weighted = (weigh_score / weigh_sum);

    UPDATE users
    SET average_score = avg_weighted
    WHERE users.id = user_id;

    CLOSE curs_1;
END $$
DELIMITER ;
