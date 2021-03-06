CREATE DATABASE b61976_aplicada

CREATE TABLE aplicada.clientes(
ID_CLIENTE INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
CEDULA VARCHAR(9),
NOMBRE VARCHAR(15),
APELLIDO_UNO VARCHAR(20),
APELLIDO_DOS VARCHAR(20),
FECHA_INS DATE
);

CREATE TABLE aplicada.telefonos(
ID INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
NUMERO INT,
ID_CLIENTE INT,
FECHA_INS DATE,
FOREIGN KEY (ID_CLIENTE) REFERENCES aplicada.clientes(id_cliente) ON DELETE CASCADE
);

CREATE TABLE aplicada.direcciones(
ID INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
DIRECCIONES VARCHAR(200),
ID_CLIENTE INT,
FECHA_INS DATE,
FOREIGN KEY (ID_CLIENTE) REFERENCES aplicada.clientes (id_cliente) ON DELETE CASCADE
);

CREATE TABLE aplicada.correos(
ID INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
CORREO VARCHAR(100),
ID_CLIENTE INT,
FECHA_INS DATE,
FOREIGN KEY (ID_CLIENTE) REFERENCES aplicada.clientes (id_cliente) ON DELETE CASCADE
);

CREATE TABLE aplicada.tarjetas(
ID INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
NUM_TARJETA VARCHAR(50),
ID_CLIENTE INT,
FECHA_INS DATE,
FOREIGN KEY (ID_CLIENTE) REFERENCES aplicada.clientes (id_cliente) ON DELETE CASCADE
);

CREATE TABLE aplicada.ordenes(
ID INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
DETALLE VARCHAR(50),
ID_CLIENTE INT,
FOREIGN KEY (ID_CLIENTE) REFERENCES aplicada.clientes (id_cliente) ON DELETE CASCADE
);