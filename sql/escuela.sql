CREATE DATABASE escuela;

USE escuela;

CREATE TABLE alumnos(
    id_alumno int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    matricula int(20) NOT NULL,
    nombre varchar(50) NOT NULL,
    papellido varchar(50) NOT NULL,
    sapellido varchar(50) NOT NULL,
    edad int(3) NOT NULL,
    naci date,
    genero varchar(20) NOT NULL,
    estado varchar(20) NOT NULL
) ENGINE= InnoDB DEFAULT CHARSET=latin1;


INSERT INTO alumnos(matricula, nombre, papellido, sapellido, edad, naci, genero, estado)
values
('1718110405', 'Fernando', 'Perez', 'Suarez', '23', '1997/12/23', 'Hombre', 'Soltero/a'),
('1718110394', 'Andrea', 'Juarez', 'Munguia', '20', '2000/06/16', 'Mujer', 'Soltero/a'),
('1718110000', 'nombre', 'primer', 'segundo', '11', '1990/01/01', 'Hombre', 'Casado/a');
/**
CREATE USER 'user_escuela'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON escuela.* TO 'user_escuela'@'localhost';
FLUSH PRIVILEGES;
**/