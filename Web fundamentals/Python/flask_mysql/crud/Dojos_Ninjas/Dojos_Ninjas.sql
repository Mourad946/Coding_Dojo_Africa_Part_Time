INSERT INTO dojos_and_ninjas_schema.dojos (name) VALUES ('Dojo 1'), ('Dojo 2'), ('Dojo 3');
DELETE FROM dojos_and_ninjas_schema.dojos WHERE id IN (SELECT id FROM (SELECT id FROM dojos_and_ninjas_schema.dojos ORDER BY id DESC LIMIT 3) AS t);
INSERT INTO dojos_and_ninjas_schema.dojos (name) VALUES ('Dojo 4'), ('Dojo 5'), ('Dojo 6');
INSERT INTO dojos_and_ninjas_schema.ninjas (first_name, last_name, age, dojo_id) VALUES ('Ninja 1', 'Surname', 25, 1), ('Ninja 2', 'Surname', 28, 1), ('Ninja 3', 'Surname', 22, 1);
INSERT INTO dojos_and_ninjas_schema.ninjas (first_name, last_name, age, dojo_id) VALUES ('Ninja 4', 'Surname', 30, 2), ('Ninja 5', 'Surname', 26, 2), ('Ninja 6', 'Surname', 29, 2);
INSERT INTO dojos_and_ninjas_schema.ninjas (first_name, last_name, age, dojo_id) VALUES ('Ninja 7', 'Surname', 27, 3), ('Ninja 8', 'Surname', 31, 3), ('Ninja 9', 'Surname', 24, 3);
SELECT * FROM dojos_and_ninjas_schema.ninjas WHERE dojo_id = 1;SELECT * FROM dojos_and_ninjas_schema.ninjas WHERE dojo_id = (SELECT MAX(id) FROM dojos_and_ninjas_schema.dojos);
SELECT dojos.* FROM dojos_and_ninjas_schema.dojos INNER JOIN dojos_and_ninjas_schema.ninjas ON dojos.id = ninjas.dojo_id ORDER BY ninjas.id DESC LIMIT 1;



