SELECT u.unique_id, e.name --We select just this two columns, the unique id and the name employee
FROM Employees e --This will be the left table, so we can show employees without unique id too
LEFT JOIN EmployeeUNI u
    ON e.id = i.id

