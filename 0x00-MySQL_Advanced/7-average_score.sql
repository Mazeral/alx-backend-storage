-- Write a SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student. Note: An average score can be a decimal
-- Requirements:
--     Procedure ComputeAverageScoreForUser is taking 1 input:
--         user_id, a users.id value (you can assume user_id is linked to an existing users)
CREATE PROCEDURE ComputeAverageScoreForUser(
	-- Defining the inputs:
	IN user_id INT
)
BEGIN
	-- Declaring variables that will contain the number of projects and the sum of the degrees
	DECLARE projects_num DECIMAL(10,2);
	DECLARE degrees_sum DECIMAL(10,2);
	-- Count the number of projects:
	SELECT COUNT(*) INTO projects_num FROM corrections WHERE corrections.user_id = user_id;
	SELECT SUM(score) INTO degrees_sum FROM corrections WHERE corrections.user_id = user_id;
	UPDATE users SET average_score = ( degrees_sum / projects_num ) WHERE id = user_id;
END;
