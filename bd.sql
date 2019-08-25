CREATE SCHEMA v1;

CREATE TABLE v1.parametros(
    paramID VARCHAR(20) NOT NULL,
    paramValor VARCHAR(255) NOT NULL,
    paramDesc VARCHAR(1000) NOT NULL
);

CREATE TABLE v1.roles(
	rolID UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
	rolName VARCHAR(50) NOT NULL,
    rolDescripcion VARCHAR(255),
    rolEstado integer NOT NULL
);

CREATE TABLE v1.funciones_rol(
    funcrolID UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    rolID UUID NOT NULL,
    actionID VARCHAR(255) NOT NULL,
    funcrolEstado INTEGER NOT NULL,
    funcrolPermiso INTEGER NOT NULL,
    CONSTRAINT funciones_rol_rolID_fkey FOREIGN KEY(rolID)
    REFERENCES v1.roles(rolID)
);

CREATE TABLE v1.usuarios(
	userID UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
	userEmail VARCHAR(255) NOT NULL,
	userPassword VARCHAR(255) NOT NULL,
	userToken VARCHAR(255),
	userFullName VARCHAR(255),
    rolID UUID NOT NULL,
    userLevelType INTEGER NOT NULL,
    userEstado INTEGER NOT NULL,    
    CONSTRAINT usuarios_rolID_fkey FOREIGN KEY(rolID)
    REFERENCES v1.roles(rolID)
);

CREATE TABLE v1.proyectos(
	proyID UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    proyNombre VARCHAR(255) NOT NULL,
    proyDescripcion VARCHAR(1000) NOT NULL,
    proyIDExterno VARCHAR(255),
    proyFechaCreacion TIMESTAMP NOT NULL,
    proyFechaCierre TIMESTAMP,
    proyEstado INTEGER NOT NULL
);

CREATE TABLE v1.equipos(
	equID UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
	userID UUID NOT NULL,
    proyID UUID NOT NULL,
    miembroEstado INTEGER NOT NULL,
    CONSTRAINT equipos_userID_fkey FOREIGN KEY(userID)
    REFERENCES v1.usuarios(userID),
    CONSTRAINT equipos_proyID_fkey FOREIGN KEY(proyID)
    REFERENCES v1.proyectos(proyID)
);

CREATE TABLE v1.decisiones(
    desiID UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    desiDescripcion VARCHAR(1000),
    userID UUID NOT NULL,
    CONSTRAINT decisiones_userID_fkey FOREIGN KEY(userID)
    REFERENCES v1.usuarios(userID)
);

CREATE TABLE v1.decisiones_proyecto(
    desproID UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    proyID UUID NOT NULL,
    desiID UUID NOT NULL,
    CONSTRAINT decisiones_proyecto_proyID_fkey FOREIGN KEY(proyID)
    REFERENCES v1.proyectos(proyID),
    CONSTRAINT decisiones_proyecto_desiID_fkey FOREIGN KEY(desiID)
    REFERENCES v1.decisiones(desiID)
);


CREATE TABLE v1.datos_contexto(
	dataID UUID PRIMARY KEY DEFAULT uuid_generate_v4(),	
	hdxTag VARCHAR(20) NOT NULL,
    dataValor VARCHAR(20) NOT NULL,
    dataTipe INTEGER NOT NULL,
    proyID UUID NOT NULL,
    CONSTRAINT datos_contexto_proyID_fkey FOREIGN KEY(proyID)
    REFERENCES v1.proyectos(proyID)
);

CREATE TABLE v1.instrumentos(
	instrID UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
	instrIDExterno VARCHAR(255) NOT NULL,
    instrTipo INTEGER NOT NULL 
);

CREATE TABLE v1.tareas(
	tareID UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
	tareNombre VARCHAR(255) NOT NULL,
    tareTipo INTEGER NOT NULL,
    tareRestricGeo JSON NOT NULL,
    tareRestricCant INTEGER NOT NULL,
    tareRestricTime JSON NOT NULL,
    instrID UUID NOT NULL,
	proyID UUID NOT NULL,
    CONSTRAINT tareas_instrID_fkey FOREIGN KEY(instrID)
    REFERENCES v1.instrumentos(instrID),
	CONSTRAINT tareas_proyID_fkey FOREIGN KEY(proyID)
	REFERENCES v1.proyectos(proyID)
);