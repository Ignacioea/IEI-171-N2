"""
SCRIPT DE PRUEBA PARA SACAR LOS DATOS DE LA BD
"""

INSERT INTO usuario(nombre, apellido, rut, sancionado, telefono, correo, tipo_usuario)
VALUES(
    'JUAN', 'PEREZ', '12123123-3', 0, '+569 77889987', 'juanperez@gmail.com', 'estudiante'
);

INSERT INTO usuario(nombre, apellido, rut, sancionado, telefono, correo, tipo_usuario)
VALUES(
    'PEDRO', 'PAZ', '12121121-1', 0, '+569 9863452', 'ppaz@gmail.com', 'profesor'
);  