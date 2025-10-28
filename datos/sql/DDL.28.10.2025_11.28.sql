USE iei-171-n2
"""
NUEVA ESTRUCTURA DE LA BD, BORRAR LA ANTERIOR UNA VEZ ESTEN LISTOS LOS INSErt
"""

CREATE TABLE IF NOT EXISTS UNIVERSIDAD(
    id INTEGER AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    siglas VARCHAR(10) NULL,
    tipo VARCHAR(20) NOT NULL,
    web VARCHAR(40) NOT NULL,
    CONSTRAINT pk_universidad PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS AUTOR(
    id INTEGER AUTO_INCREMENT,
    nombre VARCHAR(60) NOT NULL,
    apellido VARCHAR(60) NOT NULL,
    nacionalidad VARCHAR(20) NOT NULL,
    pseudonimo VARCHAR(120) NULL,
    biografia VARCHAR(255) NOT NULL,
    CONSTRAINT pk_autor PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS USUARIO(
    id INTEGER AUTO_INCREMENT,
    nombre VARCHAR(60) NOT NULL,
    apellido VARCHAR(60) NOT NULL,
    rut VARCHAR(15) NOT NULL,
    telefono VARCHAR(15) NULL,
    correo VARCHAR(255) NOT NULL,
    sancionado BOOLEAN NOT NULL,
    tipo_usuario VARCHAR(20) NOT NULL,
    CONSTRAINT pk_usuario PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS SEDE(
    id INTEGER AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    detalle VARCHAR(60) NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    region VARCHAR(60) NOT NULL,
    comuna VARCHAR(60) NOT NULL,
    ciudad VARCHAR(60) NOT NULL,
    codigo_postal INTEGER NULL,
    id_universidad INTEGER NOT NULL,
    CONSTRAINT pk_sede PRIMARY KEY(id),
    CONSTRAINT fk_sede_universidad FOREIGN KEY(id_universidad) REFERENCES UNIVERSIDAD(id)
);

CREATE TABLE IF NOT EXISTS BIBLIOTECA(
    id INTEGER AUTO_INCREMENT,
    ubicacion VARCHAR(80) NOT NULL,
    telefono_contacto VARCHAR(20) NOT NULL,
    correo_contacto VARCHAR(100) NOT NULL,
    horario_atencion VARCHAR(255) NOT NULL,
    id_sede INTEGER NOT NULL,
    CONSTRAINT pk_biblioteca PRIMARY KEY(id),
    CONSTRAINT fk_biblioteca_sede FOREIGN KEY(id_sede) REFERENCES SEDE(id)
);

CREATE TABLE IF NOT EXISTS LIBRO(
    id INTEGER AUTO_INCREMENT,
    titulo VARCHAR(255) NOT NULL,
    editorial VARCHAR(50) NOT NULL,
    anio_publicacion DATE NOT NULL,
    categoria VARCHAR(40) NOT NULL,
    ISBN VARCHAR(13) NOT NULL,
    id_autor INTEGER NOT NULL,
    id_biblioteca INTEGER NOT NULL,
    CONSTRAINT pk_libro PRIMARY KEY(id),
    CONSTRAINT fk_libro_autor FOREIGN KEY(id_autor) REFERENCES AUTOR(id),
    CONSTRAINT fk_libro_biblioteca FOREIGN KEY(id_biblioteca) REFERENCES BIBLIOTECA(id)
);


CREATE TABLE IF NOT EXISTS EJEMPLAR(
    id INTEGER AUTO_INCREMENT,
    codigo VARCHAR(50) NOT NULL,
    ubicacion VARCHAR(60) NOT NULL,
    estado VARCHAR(30) NOT NULL,
    id_libro INTEGER NOT NULL,
    CONSTRAINT pk_ejemplar PRIMARY KEY(id),
    CONSTRAINT fk_ejemplar_libro FOREIGN KEY(id_libro) REFERENCES LIBRO(id)
);

CREATE TABLE IF NOT EXISTS PRESTAMO(
    id INTEGER AUTO_INCREMENT,
    fecha_prestamo DATE NOT NULL,
    fecha_devolucion_estimado DATE NOT NULL,
    fecha_devolucion_real DATE NOT NULL,
    multa BOOLEAN NOT NULL,
    id_usuario INTEGER NOT NULL,
    id_ejemplar INTEGER NOT NULL,
    CONSTRAINT pk_prestamo PRIMARY KEY(id),
    CONSTRAINT fk_prestamo_usuario FOREIGN KEY(id_usuario) REFERENCES USUARIO(id),
    CONSTRAINT fk_prestamo_ejemplar FOREIGN KEY(id_ejemplar) REFERENCES EJEMPLAR(id)
);