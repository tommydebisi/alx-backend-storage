-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done_us, user_iden INT DEFAULT 0;

    DECLARE curs_1 CURSOR FOR SELECT id FROM users;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done_us = 1;

    OPEN curs_1;

    REPEAT
        -- FETCH values in each row and store them
        FETCH NEXT FROM curs_1 INTO user_iden;

        IF NOT done_us
        THEN
            -- use BEGIN...END when nesting cursors
            BEGIN
                DECLARE weigh_score, weigh_sum, user_id, done_cor INT DEFAULT 0;
                DECLARE cor_pro, cor_score, weighted INT DEFAULT 0;

                DECLARE curs_2 CURSOR FOR
                SELECT project_id, score FROM corrections
                WHERE corrections.user_id = user_iden;

                DECLARE CONTINUE HANDLER FOR NOT FOUND SET done_cor = 1;

                OPEN curs_2;

                REPEAT
                    FETCH NEXT FROM curs_2 INTO cor_pro, cor_score;

                    IF NOT done_cor
                    THEN
                        -- get weighted value
                        SELECT projects.weight INTO weighted
                        FROM projects
                        WHERE projects.id = cor_pro;

                        -- get summation of the product weighted val and score
                        SET weigh_score = weigh_score + (weighted * cor_score);

                        -- get summation of initial weighted val and current weighted val
                        SET weigh_sum = weigh_sum + weighted;
                    END IF;
                UNTIL done_cor END REPEAT;

                UPDATE users
                SET average_score = (weigh_score / weigh_sum)
                WHERE users.id = user_iden;
                CLOSE curs_2;
            END;
        END IF;
    UNTIL done_us END REPEAT;
    CLOSE curs_1;
END ;

DELIMITER ;
