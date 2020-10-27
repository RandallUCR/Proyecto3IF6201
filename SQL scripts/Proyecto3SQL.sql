CREATE DATABASE IF6201_Proyecto3
USE IF6201_Proyecto3

CREATE TABLE CLIENTES(
ID_CLIENTE INT PRIMARY KEY IDENTITY(1,1),
CEDULA VARCHAR(9),
NOMBRE VARCHAR(15),
APELLIDO_UNO VARCHAR(20),
APELLIDO_DOS VARCHAR(20),
FECHA_INS DATE,
EXTRAIDO TINYINT DEFAULT 0
);

CREATE TABLE TELEFONOS(
ID INT PRIMARY KEY IDENTITY(1,1),
NUMERO VARBINARY(MAX),
ID_CLIENTE INT,
FECHA_INS DATE,
EXTRAIDO TINYINT DEFAULT 0,
AUX VARCHAR(9),
FOREIGN KEY (ID_CLIENTE) REFERENCES CLIENTES (ID_CLIENTE) ON DELETE CASCADE
);

CREATE TABLE DIRECCIONES(
ID INT PRIMARY KEY IDENTITY(1,1),
DIRECCIONES VARBINARY(MAX),
ID_CLIENTE INT,
FECHA_INS DATE,
EXTRAIDO TINYINT DEFAULT 0,
AUX VARCHAR(100),
FOREIGN KEY (ID_CLIENTE) REFERENCES CLIENTES (ID_CLIENTE) ON DELETE CASCADE
);

CREATE TABLE CORREOS(
ID INT PRIMARY KEY IDENTITY(1,1),
CORREO VARBINARY(MAX),
ID_CLIENTE INT,
FECHA_INS DATE,
EXTRAIDO TINYINT DEFAULT 0,
AUX VARCHAR(50),
FOREIGN KEY (ID_CLIENTE) REFERENCES CLIENTES (ID_CLIENTE) ON DELETE CASCADE
);

CREATE TABLE TARJETAS(
ID INT PRIMARY KEY IDENTITY(1,1),
NUM_TARJETA VARBINARY(MAX),
ID_CLIENTE INT,
FECHA_INS DATE,
EXTRAIDO TINYINT DEFAULT 0,
AUX VARCHAR(16),
FOREIGN KEY (ID_CLIENTE) REFERENCES CLIENTES (ID_CLIENTE) ON DELETE CASCADE
);

CREATE TABLE ORDENES(
ID INT PRIMARY KEY IDENTITY(1,1),
DETALLE VARCHAR(50),
ID_CLIENTE INT,
FOREIGN KEY (ID_CLIENTE) REFERENCES CLIENTES (ID_CLIENTE) ON DELETE CASCADE
);

--------------------------ENCRIPTAR-----------------------------------------
CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'Proyecto1234';
CREATE CERTIFICATE Certificado WITH SUBJECT = 'Proteccion'; 
CREATE SYMMETRIC KEY LLAVE WITH ALGORITHM = AES_128   ENCRYPTION BY CERTIFICATE Certificado;

CREATE TRIGGER TR_INS_TELEFONOS ON TELEFONOS INSTEAD OF INSERT AS BEGIN
DECLARE @NUMERO VARCHAR(9),@ID_CLIENTE INT,@FECHA_INS DATE
SELECT @NUMERO = AUX, @ID_CLIENTE = ID_CLIENTE, @FECHA_INS = FECHA_INS FROM inserted;
OPEN SYMMETRIC KEY LLAVE DECRYPTION BY CERTIFICATE Certificado;
INSERT TELEFONOS (NUMERO,ID_CLIENTE,FECHA_INS) VALUES (EncryptByKey (Key_GUID('LLAVE'),@NUMERO),@ID_CLIENTE,@FECHA_INS);
CLOSE SYMMETRIC KEY LLAVE;
END

INSERT TELEFONOS (AUX,ID_CLIENTE,FECHA_INS) VALUES ('84412423','3512557',GETDATE())

CREATE TRIGGER TR_INS_DIRECCIONES ON DIRECCIONES INSTEAD OF INSERT AS BEGIN
DECLARE @DIRECCION VARCHAR(100),@ID_CLIENTE INT,@FECHA_INS DATE
SELECT @DIRECCION = AUX, @ID_CLIENTE = ID_CLIENTE, @FECHA_INS = FECHA_INS FROM inserted;
OPEN SYMMETRIC KEY LLAVE DECRYPTION BY CERTIFICATE Certificado;
INSERT DIRECCIONES(DIRECCIONES,ID_CLIENTE,FECHA_INS) VALUES (EncryptByKey (Key_GUID('LLAVE'),@DIRECCION),@ID_CLIENTE,@FECHA_INS);
CLOSE SYMMETRIC KEY LLAVE;
END

INSERT DIRECCIONES(AUX,ID_CLIENTE,FECHA_INS) VALUES ('Cartago Centro','1','20-12-2020')

CREATE TRIGGER TR_INS_CORREOS ON CORREOS INSTEAD OF INSERT AS BEGIN
DECLARE @CORREO VARCHAR(50),@ID_CLIENTE INT,@FECHA_INS DATE
SELECT @CORREO = AUX, @ID_CLIENTE = ID_CLIENTE, @FECHA_INS = FECHA_INS FROM inserted;
OPEN SYMMETRIC KEY LLAVE DECRYPTION BY CERTIFICATE Certificado;
INSERT CORREOS(CORREO,ID_CLIENTE,FECHA_INS) VALUES (EncryptByKey (Key_GUID('LLAVE'),@CORREO),@ID_CLIENTE,@FECHA_INS);
CLOSE SYMMETRIC KEY LLAVE;
END

INSERT CORREOS(AUX,ID_CLIENTE,FECHA_INS) VALUES ('pruebasDOS@gmail.com','1','2019-1-1')

CREATE TRIGGER TR_INS_TARJETAS ON TARJETAS INSTEAD OF INSERT AS BEGIN
DECLARE @TARJETA VARCHAR(16),@ID_CLIENTE INT,@FECHA_INS DATE
SELECT @TARJETA = AUX, @ID_CLIENTE = ID_CLIENTE, @FECHA_INS = FECHA_INS FROM inserted;
OPEN SYMMETRIC KEY LLAVE DECRYPTION BY CERTIFICATE Certificado;
INSERT TARJETAS(NUM_TARJETA,ID_CLIENTE,FECHA_INS) VALUES (EncryptByKey (Key_GUID('LLAVE'),@TARJETA),@ID_CLIENTE,@FECHA_INS);
CLOSE SYMMETRIC KEY LLAVE;
END

INSERT TARJETAS(AUX,ID_CLIENTE,FECHA_INS) VALUES ('7777777777777777','1','2021-03-05')

------------------------------DESENCRIPTAR-----------------------------------------------
CREATE PROCEDURE SP_CLIENTES(@fechai date, @fechaf date) AS BEGIN
SELECT ID_CLIENTE,CEDULA,NOMBRE,APELLIDO_UNO,APELLIDO_DOS, FECHA_INS FROM CLIENTES
WHERE (FECHA_INS BETWEEN @fechai AND @fechaf);
UPDATE CLIENTES SET EXTRAIDO = 1 WHERE (FECHA_INS BETWEEN @fechai AND @fechaf);
END

EXEC SP_CLIENTES '18-10-2020','20-10-2020'

CREATE PROCEDURE SP_TELEFONOS(@fechai date, @fechaf date) AS BEGIN
OPEN SYMMETRIC KEY LLAVE DECRYPTION BY CERTIFICATE Certificado;
SELECT ID,CONVERT(varchar, DecryptByKey(NUMERO)) AS 'NUMERO',ID_CLIENTE,FECHA_INS FROM TELEFONOS
WHERE (FECHA_INS BETWEEN @fechai AND @fechaf);
CLOSE SYMMETRIC KEY LLAVE;
UPDATE TELEFONOS SET EXTRAIDO = 1 WHERE (FECHA_INS BETWEEN @fechai AND @fechaf);
END

EXEC SP_TELEFONOS '18-10-2020','20-10-2020'

CREATE PROCEDURE SP_DIRECCIONES(@fechai date, @fechaf date) AS BEGIN
OPEN SYMMETRIC KEY LLAVE DECRYPTION BY CERTIFICATE Certificado;
SELECT ID,CONVERT(varchar, DecryptByKey(DIRECCIONES)) AS 'DIRECCION',ID_CLIENTE,FECHA_INS FROM DIRECCIONES
WHERE (FECHA_INS BETWEEN @fechai AND @fechaf);
CLOSE SYMMETRIC KEY LLAVE;
UPDATE DIRECCIONES SET EXTRAIDO = 1 WHERE (FECHA_INS BETWEEN @fechai AND @fechaf);
END

EXEC SP_DIRECCIONES'18-10-2020','20-10-2020'

CREATE PROCEDURE SP_CORREOS(@fechai date, @fechaf date) AS BEGIN
OPEN SYMMETRIC KEY LLAVE DECRYPTION BY CERTIFICATE Certificado;
SELECT ID,CONVERT(varchar, DecryptByKey(CORREO)) AS 'CORREO',ID_CLIENTE,FECHA_INS FROM CORREOS
WHERE (FECHA_INS BETWEEN @fechai AND @fechaf);
CLOSE SYMMETRIC KEY LLAVE;
UPDATE CORREOS SET EXTRAIDO = 1 WHERE (FECHA_INS BETWEEN @fechai AND @fechaf);
END

EXEC SP_CORREOS '18-10-2020','20-10-2020'

CREATE PROCEDURE SP_TARJETAS(@fechai date, @fechaf date) AS BEGIN
OPEN SYMMETRIC KEY LLAVE DECRYPTION BY CERTIFICATE Certificado;
SELECT ID,CONVERT(varchar, DecryptByKey(NUM_TARJETA)) AS 'TARJETA',ID_CLIENTE,FECHA_INS FROM TARJETAS
WHERE (FECHA_INS BETWEEN @fechai AND @fechaf);
CLOSE SYMMETRIC KEY LLAVE;
UPDATE TARJETAS SET EXTRAIDO = 1 WHERE (FECHA_INS BETWEEN @fechai AND @fechaf);
END

EXEC SP_TARJETAS '2020-10-10','2020-10-20'

CREATE PROCEDURE SP_ORDENES(@fechai date, @fechaf date) AS BEGIN
SELECT O.ID,O.DETALLE,O.ID_CLIENTE FROM CLIENTES C INNER JOIN ORDENES O
ON C.ID_CLIENTE = O.ID_CLIENTE AND (C.FECHA_INS BETWEEN @fechai AND @fechaf);
END

EXEC SP_ORDENES '2020-10-18','2020-12-23'

-------------------------------JOB----------------------------------------
CREATE PROCEDURE SP_EXTRAIDOS AS BEGIN
DELETE TELEFONOS WHERE EXTRAIDO = 1;
DELETE DIRECCIONES WHERE EXTRAIDO = 1;
DELETE CORREOS WHERE EXTRAIDO = 1;
DELETE TARJETAS WHERE EXTRAIDO = 1;
END

EXEC SP_EXTRAIDOS
----------------------------------MANUAL------------------------------------------

CREATE PROCEDURE SP_CLIENTES_ORDENES AS BEGIN
DELETE CLIENTES WHERE EXTRAIDO = 1;
SELECT 'Los clientes y sus ordenes fueron eliminados'
END

EXEC SP_CLIENTES_ORDENES

CREATE PROCEDURE SP_ASIGNAR_FKS AS BEGIN
DECLARE @CONTADOR INT, @RANDOM INT
SET @CONTADOR = 1
WHILE @CONTADOR < 1001 BEGIN

SET @RANDOM = FLOOR(RAND()*(1000-1+1)+1)
UPDATE TELEFONOS SET ID_CLIENTE = @RANDOM WHERE ID = (SELECT ID FROM (SELECT ID,ROW_NUMBER() OVER (ORDER BY ID) AS RN FROM TELEFONOS) XD WHERE XD.RN = @CONTADOR)
SET @RANDOM = FLOOR(RAND()*(1000-1+1)+1)
UPDATE DIRECCIONES SET ID_CLIENTE = @RANDOM WHERE ID = (SELECT ID FROM (SELECT ID,ROW_NUMBER() OVER (ORDER BY ID) AS RN FROM DIRECCIONES) XD WHERE XD.RN = @CONTADOR)
SET @RANDOM = FLOOR(RAND()*(1000-1+1)+1)
UPDATE CORREOS SET ID_CLIENTE = @RANDOM WHERE ID = (SELECT ID FROM (SELECT ID,ROW_NUMBER() OVER (ORDER BY ID) AS RN FROM CORREOS) XD WHERE XD.RN = @CONTADOR)
SET @RANDOM = FLOOR(RAND()*(1000-1+1)+1)
UPDATE TARJETAS SET ID_CLIENTE = @RANDOM WHERE ID = (SELECT ID FROM (SELECT ID,ROW_NUMBER() OVER (ORDER BY ID) AS RN FROM TARJETAS) XD WHERE XD.RN = @CONTADOR)
SET @RANDOM = FLOOR(RAND()*(1000-1+1)+1)
UPDATE ORDENES SET ID_CLIENTE = @RANDOM WHERE ID = (SELECT ID FROM (SELECT ID,ROW_NUMBER() OVER (ORDER BY ID) AS RN FROM ORDENES) XD WHERE XD.RN = @CONTADOR)

SET @CONTADOR = @CONTADOR+1
END
END

EXEC SP_ASIGNAR_FKS

SELECT * FROM CLIENTES WHERE (FECHA_INS BETWEEN '2019-01-01' AND '2020-12-31')
SELECT * FROM TELEFONOS WHERE (FECHA_INS BETWEEN '2019-01-01' AND '2020-12-31')
SELECT * FROM DIRECCIONES WHERE (FECHA_INS BETWEEN '2019-01-01' AND '2020-12-31')
SELECT * FROM CORREOS WHERE (FECHA_INS BETWEEN '2019-01-01' AND '2020-12-31')
SELECT * FROM TARJETAS WHERE (FECHA_INS BETWEEN '2019-01-01' AND '2020-12-31')
SELECT * FROM ORDENES INNER JOIN CLIENTES ON ORDENES.ID_CLIENTE = CLIENTES.ID_CLIENTE AND (CLIENTES.FECHA_INS BETWEEN '2019-01-01' AND '2020-12-31')



