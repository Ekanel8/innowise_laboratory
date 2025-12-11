CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT,
    birth_year INTEGER
);

DELETE FROM students;
DELETE FROM sqlite_sequence WHERE name='students';

INSERT INTO students (full_name, birth_year)
VALUES
    ('Alice Johnson', 2005),
    ('Brian Smith', 2004),
    ('Carla Reyes', 2006),
    ('Daniel Kim', 2005),
    ('Eva Thompson', 2003),
    ('Felix Nguyen', 2007),
    ('Grace Patel', 2005),
    ('Henry Lopez', 2004),
    ('Isabella Martinez', 2006);

CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER REFERENCES students(id),
    subject TEXT,
    grade INTEGER
);

DELETE FROM grades;
DELETE FROM sqlite_sequence WHERE name='grades';

INSERT INTO grades (student_id, subject, grade)
VALUES
    (1, 'Math', 88),
    (1, 'English', 92),
    (1, 'Science', 85),
    (2, 'Math', 75),
    (2, 'History', 83),
    (2, 'English', 79),
    (3, 'Science', 95),
    (3, 'Math', 91),
    (3, 'Art', 89),
    (4, 'Math', 84),
    (4, 'Science', 88),
    (4, 'Physical Education', 93),
    (5, 'English', 90),
    (5, 'History', 85),
    (5, 'Math', 88),
    (6, 'Science', 72),
    (6, 'Math', 78),
    (6, 'English', 81),
    (7, 'Art', 94),
    (7, 'Science', 87),
    (7, 'Math', 90),
    (8, 'History', 77),
    (8, 'Math', 83),
    (8, 'Science', 80),
    (9, 'English', 96),
    (9, 'Math', 89),
    (9, 'Art', 92);

SELECT grades.grade
FROM students
INNER JOIN grades ON students.id = grades.student_id
WHERE students.full_name = 'Alice Johnson';

SELECT AVG(grade)
FROM grades
GROUP BY student_id;

SELECT *
FROM students
WHERE birth_year > 2004;

SELECT subject, AVG(grade)
FROM grades
GROUP BY subject;

SELECT students.*
FROM students
INNER JOIN (
    SELECT student_id, AVG(grade) AS average
    FROM grades
    GROUP BY student_id
) map ON students.id = map.student_id
ORDER BY average DESC
LIMIT 3;

SELECT *
FROM students
WHERE id IN (
    SELECT student_id
    FROM grades
    WHERE grade < 80
);