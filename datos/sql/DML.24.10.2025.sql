USE biblioteca_system;

ALTER TABLE libro MODIFY COLUMN anio YEAR;

INSERT INTO universidad (nombre, siglas, tipo, web) 
VALUES
('INACAP', 'INACAP', 'INSTITUTO PRIVADO', 'https://www.inacap.cl');



INSERT INTO sede (nombre, detalle, direccion, region, comuna, ciudad, id_universidad) 
VALUES
('INACAP TEMUCO', 'Sede Temuco', 'Luis Durand 2150', 'La Araucania', 'Temuco', 'Temuco', 1);



INSERT INTO biblioteca (ubicacion, telefono_contacto, correo_contacto, horario_atencion, id_sede) 
VALUES
('Edificio A, Piso 2', '56 45 229 6000', 'biblioteca.temuco@inacap.cl', 'Lunes a Viernes 08:30 - 19:00', 1);



INSERT INTO autor (nombre, apellido, nacionalidad, biografia)
VALUES
('Robert', 'Lafore', 'Estadounidense', 'Autor de “Object-Oriented Programming in C++”, referente en programación estructurada y POO.'),
('Andrew S.', 'Tanenbaum', 'Neerlandes', 'Profesor y autor de obras clásicas en redes y sistemas operativos como “Computer Networks”.'),
('Stepthen R.', 'Covey', 'Estadounidense', 'Autor de “Los 7 hábitos de la gente altamente efectiva”, influyente en administración y liderazgo.'),
('Paul', 'Horowitz', 'Estadounidense', 'Coautor de “The Art of Electronics”, obra fundamental en electrónica aplicada.'),
('Don', 'Norman', 'Estadounidense', 'Referente del diseño centrado en el usuario, autor de “The Design of Everyday Things”.'),
('Douglas E.', 'Comer', 'Estadounidense', 'Escritor de libros sobre redes e Internet, profesor de Purdue University.'),
('Tony', 'Gaddis', 'Estadounidense', 'Autor de múltiples libros introductorios de programación, muy usados en educación técnica.'),
('Simon', 'Sinek', 'Britanico', 'Orador y autor de liderazgo, reconocido por “Start With Why”.'),
('Raymond', 'Murphy', 'Britanico', 'Autor de “English Grammar in Use”, libro de gramática inglesa más usado en el mundo.'),
('James F.', 'Kurose', 'Estadounidense', 'Coautor de “Computer Networking: A Top-Down Approach”.');



INSERT INTO libro (titulo, editorial, anio, categoria, ISBN, id_autor, id_biblioteca) 
VALUES
('Object-Oriented Programming in C++', 'Pearson', 2013, 'Programación', '9780672323089', 1, 1),
('Computer Networks', 'Pearson', '2011', 'Redes', '9780132126953', 2, 1),
('Los 7 hábitos de la gente altamente efectiva', 'Paidos', 2013, 'Administración', '9788497594250', 3, 1),
('The Art of Electronics', 'Cambridge University Press', 2015, 'Electrónica', '9780521809269', 4, 1),
('The Design of Everyday Things', 'Basic Books', 2013, 'Diseño', '9780465050659', 5, 1),
('Internetworking with TCP/IP', 'Pearson', 2013, 'Redes', '9780136085300', 6, 1),
('Starting Out with Python', 'Pearson', 2020, 'Programación', '9780135929032', 7, 1),
('Start With Why', 'Penguin Books', 2011, 'Administración', '9781591846444', 8, 1),
('English Grammar in Use', 'Cambridge University Press', 2019, 'Inglés', '9781108457651', 9, 1),
('Computer Networking: A Top-Down Approach', 'Pearson', 2017, 'Redes', '9780133594140', 10, 1),
('Python Programming: An Introduction to Computer Science', 'Franklin, Beedle & Associates', 2016, 'Programación', '9781590282755', 7, 1),
('Human-Centered Design', 'CRC Press', 2019, 'Diseño', '9781498764378', 5, 1),
('Effective Leadership', 'Penguin Books', 2017, 'Administración', '9780241970058', 8, 1),
('Electronic Principles', 'McGraw-Hill', 2016, 'Electrónica', '9781259250995', 4, 1),
('Practical Electronics for Inventors', 'McGraw-Hill', 2016, 'Electrónica', '9781259587541', 4, 1);



INSERT INTO usuario(nombre, apellido, rut, telefono, correo, sancionado, tipo_usuario) 
VALUES
('JUAN', 'PEREZ', '12123123-3', '+569 77889987', 'juanperez@gmail.com', 0, 'estudiante'),
('PEDRO', 'PAZ', '12121121-1', '+569 9863452', 'ppaz@gmail.com', 0, 'profesor'),
('Martin', 'Aguilera', '21.345.678-9', '+56 9 8765 1234', 'maguilera@inacapmail.cl', 0, 'Estudiante'),
('Sofia', 'Rojas', '20.234.567-8', '+56 9 6543 9988', 'srojas@inacapmail.cl', 0, 'Estudiante'),
('Diego', 'Perez', '19.876.543-2', '+56 9 7777 4321', 'dperez@inacapmail.cl', 0, 'Estudiante'),
('Fernanda', 'Muñoz', '22.123.456-1', '+56 9 5555 6789', 'fmunoz@inacapmail.cl', 0, 'Estudiante'),
('Camilo', 'Araya', '18.567.890-3', '+56 9 4444 2211', 'caraya@inacapmail.cl', 0, 'Estudiante'),
('Valentina', 'Silva', '23.234.567-4', '+56 9 9876 2345', 'vsilva@inacapmail.cl', 0, 'Estudiante'),
('Rodrigo', 'Torres', '15.111.222-3', '+56 9 3456 7890', 'rtorres@inacapmail.cl', 0, 'Docente'),
('Natalia', 'González', '17.555.666-7', '+56 9 9988 7766', 'ngonzalez@inacapmail.cl', 0, 'Docente'),
('Jorge', 'Paredes', '13.345.987-2', '+56 9 2233 4455', 'jparedes@inacapmail.cl', 0, 'Administrativo'),
('Ana', 'Vidal', '19.234.876-5', '+56 9 1122 3344', 'avidal@inacapmail.cl', 0, 'Estudiante');



INSERT INTO ejemplar (codigo, ubicacion, estado, id_libro)
 VALUES
('EJP-001', 'Estante A1', 'Disponible', 1),
('EJP-002', 'Estante A1', 'Disponible', 1),
('EJP-003', 'Estante B2', 'Disponible', 2),
('EJP-004', 'Estante B3', 'Disponible', 3),
('EJP-005', 'Estante C1', 'Disponible', 4),
('EJP-006', 'Estante C2', 'Disponible', 5),
('EJP-007', 'Estante D1', 'Disponible', 6),
('EJP-008', 'Estante D2', 'Disponible', 7),
('EJP-010', 'Estante E1', 'Disponible', 9),
('EJP-011', 'Estante E2', 'Disponible', 10),
('EJP-012', 'Estante F1', 'Disponible', 11),
('EJP-013', 'Estante F2', 'Disponible', 12),
('EJP-014', 'Estante G1', 'Disponible', 13),
('EJP-015', 'Estante G2', 'Disponible', 14),
('EJP-016', 'Estante G3', 'Disponible', 15),
('EJP-017', 'Estante H1', 'Disponible', 3),
('EJP-018', 'Estante H2', 'Disponible', 5),
('EJP-019', 'Estante H3', 'Disponible', 7),
('EJP-020', 'Estante I1', 'Disponible', 9);