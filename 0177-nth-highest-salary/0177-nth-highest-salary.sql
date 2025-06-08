CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE result INT;
  SET N = N - 1;

  SELECT salary INTO result
  FROM (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT N, 1
  ) AS temp;

  RETURN result;
END
