--
-- PostgreSQL database dump
--

-- Dumped from database version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: v1; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA v1;


ALTER SCHEMA v1 OWNER TO postgres;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


--
-- Name: uuid-ossp; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;


--
-- Name: EXTENSION "uuid-ossp"; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: acciones; Type: TABLE; Schema: v1; Owner: postgres
--

CREATE TABLE v1.acciones (
    accionid uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    descripcion character varying,
    nombre character varying(255) NOT NULL
);


ALTER TABLE v1.acciones OWNER TO postgres;

--
-- Name: contextos; Type: TABLE; Schema: v1; Owner: postgres
--

CREATE TABLE v1.contextos (
    contextoid uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    descripcion character varying NOT NULL
);


ALTER TABLE v1.contextos OWNER TO postgres;

--
-- Name: contextos_proyecto; Type: TABLE; Schema: v1; Owner: postgres
--

CREATE TABLE v1.contextos_proyecto (
    contproyid uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    proyid uuid NOT NULL,
    contextoid uuid NOT NULL
);


ALTER TABLE v1.contextos_proyecto OWNER TO postgres;

--
-- Name: datos_contexto; Type: TABLE; Schema: v1; Owner: postgres
--

CREATE TABLE v1.datos_contexto (
    dataid uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    hdxtag character varying(20) NOT NULL,
    datavalor character varying(20) NOT NULL,
    datatipe integer NOT NULL,
    contextoid uuid NOT NULL
);


ALTER TABLE v1.datos_contexto OWNER TO postgres;

--
-- Name: decisiones; Type: TABLE; Schema: v1; Owner: postgres
--

CREATE TABLE v1.decisiones (
    desiid uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    desidescripcion character varying(1000),
    userid uuid NOT NULL
);


ALTER TABLE v1.decisiones OWNER TO postgres;

--
-- Name: decisiones_proyecto; Type: TABLE; Schema: v1; Owner: postgres
--

CREATE TABLE v1.decisiones_proyecto (
    desproid uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    proyid uuid NOT NULL,
    desiid uuid NOT NULL
);


ALTER TABLE v1.decisiones_proyecto OWNER TO postgres;

--
-- Name: equipos; Type: TABLE; Schema: v1; Owner: postgres
--

CREATE TABLE v1.equipos (
    equid uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    userid uuid NOT NULL,
    proyid uuid NOT NULL,
    miembroestado integer NOT NULL
);


ALTER TABLE v1.equipos OWNER TO postgres;

--
-- Name: funciones_rol; Type: TABLE; Schema: v1; Owner: postgres
--

CREATE TABLE v1.funciones_rol (
    funcrolid uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    rolid uuid NOT NULL,
    funcrolestado integer NOT NULL,
    funcrolpermiso integer NOT NULL,
    accionid uuid NOT NULL
);


ALTER TABLE v1.funciones_rol OWNER TO postgres;

--
-- Name: instrumentos; Type: TABLE; Schema: v1; Owner: postgres
--

CREATE TABLE v1.instrumentos (
    instrid uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    instridexterno character varying(255) NOT NULL,
    instrtipo integer NOT NULL,
    instrnombre character varying(255) NOT NULL,
    instrdescripcion text
);


ALTER TABLE v1.instrumentos OWNER TO postgres;

--
-- Name: parametros; Type: TABLE; Schema: v1; Owner: postgres
--

CREATE TABLE v1.parametros (
    paramid character varying(20) NOT NULL,
    paramvalor character varying(255) NOT NULL,
    paramdesc character varying(1000) NOT NULL
);


ALTER TABLE v1.parametros OWNER TO postgres;

--
-- Name: proyectos; Type: TABLE; Schema: v1; Owner: postgres
--

CREATE TABLE v1.proyectos (
    proyid uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    proynombre character varying(255) NOT NULL,
    proydescripcion character varying(1000) NOT NULL,
    proyidexterno character varying(255),
    proyfechacreacion timestamp without time zone NOT NULL,
    proyfechacierre timestamp without time zone,
    proyestado integer NOT NULL
);


ALTER TABLE v1.proyectos OWNER TO postgres;

--
-- Name: roles; Type: TABLE; Schema: v1; Owner: postgres
--

CREATE TABLE v1.roles (
    rolid uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    rolname character varying(50) NOT NULL,
    roldescripcion character varying(255),
    rolestado integer NOT NULL
);


ALTER TABLE v1.roles OWNER TO postgres;

--
-- Name: tareas; Type: TABLE; Schema: v1; Owner: postgres
--

CREATE TABLE v1.tareas (
    tareid uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    tarenombre character varying(255) NOT NULL,
    taretipo integer NOT NULL,
    tarerestricgeo json NOT NULL,
    tarerestriccant integer NOT NULL,
    tarerestrictime json NOT NULL,
    instrid uuid NOT NULL,
    proyid uuid NOT NULL
);


ALTER TABLE v1.tareas OWNER TO postgres;

--
-- Name: usuarios; Type: TABLE; Schema: v1; Owner: postgres
--

CREATE TABLE v1.usuarios (
    userid uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    useremail character varying(255) NOT NULL,
    password character varying(255) NOT NULL,
    usertoken character varying(255),
    userfullname character varying(255),
    rolid uuid NOT NULL,
    userleveltype integer NOT NULL,
    userestado integer NOT NULL,
    last_login timestamp without time zone
);


ALTER TABLE v1.usuarios OWNER TO postgres;

--
-- Data for Name: acciones; Type: TABLE DATA; Schema: v1; Owner: postgres
--

COPY v1.acciones (accionid, descripcion, nombre) FROM stdin;
0ff17033-7e9a-4f6d-a66b-b80b69860ec0	\N	Gestión de proyectos
1f471664-7209-4053-85f5-e49cd506e9d9	\N	Gestión de Tareas
dd9a202b-3c2c-4a69-97b6-1c13b8f4792f	\N	Gestión de Instrumentos
07225737-ca27-4f9a-bae9-1be6bfe8d15c	\N	Gestión de Decisiones
cf49d486-f6fe-4667-b155-51eda0fb7382	\N	Gestión de Contextos
e0be3e0e-b127-4fe7-8478-b78a35faf845	\N	Gestión de usuarios
00add5dd-7d17-4c93-b3a7-22ac9a1f3c76	\N	Gestión de roles
\.


--
-- Data for Name: contextos; Type: TABLE DATA; Schema: v1; Owner: postgres
--

COPY v1.contextos (contextoid, descripcion) FROM stdin;
a914fbcd-9c26-4a4c-b0dc-5090e363fb05	Indice de robos 2019
d2647c5e-cf3d-4084-8619-4a399dcb4154	Indice de homicidios 2019
6cd582d9-f7f1-4ef3-8974-9ef12b1bd424	indice de amotinamientos 2019
67525331-f032-4cb3-99c9-a511536f0395	Indice de Suicidios 2019
\.


--
-- Data for Name: contextos_proyecto; Type: TABLE DATA; Schema: v1; Owner: postgres
--

COPY v1.contextos_proyecto (contproyid, proyid, contextoid) FROM stdin;
259bff87-17a3-4406-a788-3345bc615e50	0a98f186-cfa9-4e18-962b-418fe90cbd17	a914fbcd-9c26-4a4c-b0dc-5090e363fb05
d8e61d96-b8fb-4025-9ece-298120db395a	0a98f186-cfa9-4e18-962b-418fe90cbd17	d2647c5e-cf3d-4084-8619-4a399dcb4154
16636a86-a707-451b-bef2-b60e6f11412b	0a98f186-cfa9-4e18-962b-418fe90cbd17	6cd582d9-f7f1-4ef3-8974-9ef12b1bd424
59160586-c291-41a9-ba1a-6f4cbc5c2643	4e904db9-8c09-4883-bfaa-0c768bb20d95	a914fbcd-9c26-4a4c-b0dc-5090e363fb05
\.


--
-- Data for Name: datos_contexto; Type: TABLE DATA; Schema: v1; Owner: postgres
--

COPY v1.datos_contexto (dataid, hdxtag, datavalor, datatipe, contextoid) FROM stdin;
5f9fa914-ccec-400e-842d-e5990406eda2	#dead	 	1	d2647c5e-cf3d-4084-8619-4a399dcb4154
9ab6605d-0776-4cb7-b55d-c7635f3d40ce	#dead 2	 	1	d2647c5e-cf3d-4084-8619-4a399dcb4154
1d8a6f2d-5f6c-42dd-a6f2-71d6324abb84	#robe	 	1	a914fbcd-9c26-4a4c-b0dc-5090e363fb05
9e736a90-39f3-4071-b00a-37d526e70d96	#robe 2	 	1	a914fbcd-9c26-4a4c-b0dc-5090e363fb05
21c7bd2e-0d13-4e48-aca2-31d765793ef8	#help	 	1	67525331-f032-4cb3-99c9-a511536f0395
\.


--
-- Data for Name: decisiones; Type: TABLE DATA; Schema: v1; Owner: postgres
--

COPY v1.decisiones (desiid, desidescripcion, userid) FROM stdin;
ff64f28b-90a4-42ba-a36a-1a6f0ed0f2a8	Reducción de Homicidios	7af9e3d6-f7f7-4bee-b34c-cc2ee284afe7
34beefe7-0dcb-4ed0-88a3-578682215c7a	Reducción de conflictos	7af9e3d6-f7f7-4bee-b34c-cc2ee284afe7
93ee56df-cfcd-4adb-8452-e37a84d41b0c	Reducción de robos	7af9e3d6-f7f7-4bee-b34c-cc2ee284afe7
\.


--
-- Data for Name: decisiones_proyecto; Type: TABLE DATA; Schema: v1; Owner: postgres
--

COPY v1.decisiones_proyecto (desproid, proyid, desiid) FROM stdin;
b4728b46-ddd9-4ea2-8593-be734aad611c	4e904db9-8c09-4883-bfaa-0c768bb20d95	93ee56df-cfcd-4adb-8452-e37a84d41b0c
\.


--
-- Data for Name: equipos; Type: TABLE DATA; Schema: v1; Owner: postgres
--

COPY v1.equipos (equid, userid, proyid, miembroestado) FROM stdin;
\.


--
-- Data for Name: funciones_rol; Type: TABLE DATA; Schema: v1; Owner: postgres
--

COPY v1.funciones_rol (funcrolid, rolid, funcrolestado, funcrolpermiso, accionid) FROM stdin;
e8e22df8-75fd-4b07-9513-3651988fe30a	628acd70-f86f-4449-af06-ab36144d9d6a	1	1	0ff17033-7e9a-4f6d-a66b-b80b69860ec0
6c90663f-d762-40d2-b747-ff6cd246db5c	628acd70-f86f-4449-af06-ab36144d9d6a	1	1	1f471664-7209-4053-85f5-e49cd506e9d9
f35fd051-d1a6-400e-a37c-55a90d0128ba	628acd70-f86f-4449-af06-ab36144d9d6a	1	1	dd9a202b-3c2c-4a69-97b6-1c13b8f4792f
511b20ad-f22d-4e9c-be99-351c4a333163	628acd70-f86f-4449-af06-ab36144d9d6a	1	1	07225737-ca27-4f9a-bae9-1be6bfe8d15c
34b7a492-8683-4ccb-a193-b57f6fb3c401	628acd70-f86f-4449-af06-ab36144d9d6a	1	1	cf49d486-f6fe-4667-b155-51eda0fb7382
d9275258-2d50-466e-b29a-409f1496c5b6	628acd70-f86f-4449-af06-ab36144d9d6a	1	1	e0be3e0e-b127-4fe7-8478-b78a35faf845
ca7ee0a9-ec55-4f17-b5ae-ffd2a73207ec	628acd70-f86f-4449-af06-ab36144d9d6a	1	1	00add5dd-7d17-4c93-b3a7-22ac9a1f3c76
abb839a4-b904-4464-b5d2-3170620f75fc	0be58d4e-6735-481a-8740-739a73c3be86	1	1	cf49d486-f6fe-4667-b155-51eda0fb7382
\.


--
-- Data for Name: instrumentos; Type: TABLE DATA; Schema: v1; Owner: postgres
--

COPY v1.instrumentos (instrid, instridexterno, instrtipo, instrnombre, instrdescripcion) FROM stdin;
b374d83c-52bd-4099-8d82-5af753657a5e	aiBtimUN3BBR6iRVMpQidL	1	El Retiro	abc
033ffff4-1b91-4524-b2cd-bcdee903af76	aJypqscWMCu3J3URaN2JKf	1	La Luna	  test
a5819268-a084-4bd7-9239-bb5313a0b48c	a7YUdD8i9BQAKSrKhAPMEt	1	Siloe	desc
\.


--
-- Data for Name: parametros; Type: TABLE DATA; Schema: v1; Owner: postgres
--

COPY v1.parametros (paramid, paramvalor, paramdesc) FROM stdin;
\.


--
-- Data for Name: proyectos; Type: TABLE DATA; Schema: v1; Owner: postgres
--

COPY v1.proyectos (proyid, proynombre, proydescripcion, proyidexterno, proyfechacreacion, proyfechacierre, proyestado) FROM stdin;
0a98f186-cfa9-4e18-962b-418fe90cbd17	Alias reprehenderit	Est vitae et officia	12345	2019-09-10 21:13:44.47384	\N	0
4e904db9-8c09-4883-bfaa-0c768bb20d95	Consequat Laborum e	Et qui recusandae N	12345	2019-09-19 16:20:35.905628	\N	1
\.


--
-- Data for Name: roles; Type: TABLE DATA; Schema: v1; Owner: postgres
--

COPY v1.roles (rolid, rolname, roldescripcion, rolestado) FROM stdin;
0be58d4e-6735-481a-8740-739a73c3be86	Voluntario	abcc	0
628acd70-f86f-4449-af06-ab36144d9d6a	Proyectista	abc	1
e52ec910-0f33-4f94-879f-2e83258dde0b	Invitado	abcd	1
\.


--
-- Data for Name: tareas; Type: TABLE DATA; Schema: v1; Owner: postgres
--

COPY v1.tareas (tareid, tarenombre, taretipo, tarerestricgeo, tarerestriccant, tarerestrictime, instrid, proyid) FROM stdin;
058e25eb-f378-4045-97ba-dd438d6f6dde	Test	1	{}	75	{}	a5819268-a084-4bd7-9239-bb5313a0b48c	0a98f186-cfa9-4e18-962b-418fe90cbd17
\.


--
-- Data for Name: usuarios; Type: TABLE DATA; Schema: v1; Owner: postgres
--

COPY v1.usuarios (userid, useremail, password, usertoken, userfullname, rolid, userleveltype, userestado, last_login) FROM stdin;
7af9e3d6-f7f7-4bee-b34c-cc2ee284afe7	inge4neuromedia@gmail.com	$pbkdf2-sha256$30000$oJRSyrnXOodwTglBCGHsnQ$m8VgZmxv9Ms0caCSIMVh9e28m7B6tMepyvEgMkJpvQg	\N	Admin	628acd70-f86f-4449-af06-ab36144d9d6a	1	1	\N
ab9e679e-f691-48ed-91b9-4dd91601a077	inge3neuromedia@gmail.com	$pbkdf2-sha256$30000$3DvHWMsZYwxBiPGek/L.Pw$XpkvGOpDLn8oL6a76ish5dwTGfVQn8dJ3xaqArVVetM	\N	Volunatario	0be58d4e-6735-481a-8740-739a73c3be86	1	1	\N
9705e2f4-ab8c-4df0-8321-507b99ee37bd	inge2neuromedia@gmail.com	$pbkdf2-sha256$30000$MCZE6P1fi3GO0ToHYAyBkA$09ffHRkDaDK8greYmSN7v7cl6vqDJHR6RtfOX0lcsL4	\N	Invitado	e52ec910-0f33-4f94-879f-2e83258dde0b	1	1	\N
\.


--
-- Name: acciones acciones_pkey; Type: CONSTRAINT; Schema: v1; Owner: postgres
--

ALTER TABLE ONLY v1.acciones
    ADD CONSTRAINT acciones_pkey PRIMARY KEY (accionid);


--
-- Name: contextos_proyecto contexto_proyecto_pkey; Type: CONSTRAINT; Schema: v1; Owner: postgres
--

ALTER TABLE ONLY v1.contextos_proyecto
    ADD CONSTRAINT contexto_proyecto_pkey PRIMARY KEY (contproyid);


--
-- Name: contextos contextos_pkey; Type: CONSTRAINT; Schema: v1; Owner: postgres
--

ALTER TABLE ONLY v1.contextos
    ADD CONSTRAINT contextos_pkey PRIMARY KEY (contextoid);


--
-- Name: datos_contexto datos_contexto_pkey; Type: CONSTRAINT; Schema: v1; Owner: postgres
--

ALTER TABLE ONLY v1.datos_contexto
    ADD CONSTRAINT datos_contexto_pkey PRIMARY KEY (dataid);


--
-- Name: decisiones decisiones_pkey; Type: CONSTRAINT; Schema: v1; Owner: postgres
--

ALTER TABLE ONLY v1.decisiones
    ADD CONSTRAINT decisiones_pkey PRIMARY KEY (desiid);


--
-- Name: decisiones_proyecto decisiones_proyecto_pkey; Type: CONSTRAINT; Schema: v1; Owner: postgres
--

ALTER TABLE ONLY v1.decisiones_proyecto
    ADD CONSTRAINT decisiones_proyecto_pkey PRIMARY KEY (desproid);


--
-- Name: equipos equipos_pkey; Type: CONSTRAINT; Schema: v1; Owner: postgres
--

ALTER TABLE ONLY v1.equipos
    ADD CONSTRAINT equipos_pkey PRIMARY KEY (equid);


--
-- Name: funciones_rol funciones_rol_pkey; Type: CONSTRAINT; Schema: v1; Owner: postgres
--

ALTER TABLE ONLY v1.funciones_rol
    ADD CONSTRAINT funciones_rol_pkey PRIMARY KEY (funcrolid);


--
-- Name: instrumentos instrumentos_pkey; Type: CONSTRAINT; Schema: v1; Owner: postgres
--

ALTER TABLE ONLY v1.instrumentos
    ADD CONSTRAINT instrumentos_pkey PRIMARY KEY (instrid);


--
-- Name: proyectos proyectos_pkey; Type: CONSTRAINT; Schema: v1; Owner: postgres
--

ALTER TABLE ONLY v1.proyectos
    ADD CONSTRAINT proyectos_pkey PRIMARY KEY (proyid);


--
-- Name: roles roles_pkey; Type: CONSTRAINT; Schema: v1; Owner: postgres
--

ALTER TABLE ONLY v1.roles
    ADD CONSTRAINT roles_pkey PRIMARY KEY (rolid);


--
-- Name: tareas tareas_pkey; Type: CONSTRAINT; Schema: v1; Owner: postgres
--

ALTER TABLE ONLY v1.tareas
    ADD CONSTRAINT tareas_pkey PRIMARY KEY (tareid);


--
-- Name: usuarios usuarios_pkey; Type: CONSTRAINT; Schema: v1; Owner: postgres
--

ALTER TABLE ONLY v1.usuarios
    ADD CONSTRAINT usuarios_pkey PRIMARY KEY (userid);


--
-- Name: datos_contexto contextoid_fkey; Type: FK CONSTRAINT; Schema: v1; Owner: postgres
--

ALTER TABLE ONLY v1.datos_contexto
    ADD CONSTRAINT contextoid_fkey FOREIGN KEY (contextoid) REFERENCES v1.contextos(contextoid) ON DELETE CASCADE;


--
-- Name: contextos_proyecto contextoid_fkey; Type: FK CONSTRAINT; Schema: v1; Owner: postgres
--

ALTER TABLE ONLY v1.contextos_proyecto
    ADD CONSTRAINT contextoid_fkey FOREIGN KEY (contextoid) REFERENCES v1.contextos(contextoid) ON DELETE CASCADE;


--
-- Name: decisiones_proyecto decisiones_proyecto_desiid_fkey; Type: FK CONSTRAINT; Schema: v1; Owner: postgres
--

ALTER TABLE ONLY v1.decisiones_proyecto
    ADD CONSTRAINT decisiones_proyecto_desiid_fkey FOREIGN KEY (desiid) REFERENCES v1.decisiones(desiid) ON DELETE CASCADE;


--
-- Name: decisiones_proyecto decisiones_proyecto_proyid_fkey; Type: FK CONSTRAINT; Schema: v1; Owner: postgres
--

ALTER TABLE ONLY v1.decisiones_proyecto
    ADD CONSTRAINT decisiones_proyecto_proyid_fkey FOREIGN KEY (proyid) REFERENCES v1.proyectos(proyid) ON DELETE CASCADE;


--
-- Name: decisiones decisiones_userid_fkey; Type: FK CONSTRAINT; Schema: v1; Owner: postgres
--

ALTER TABLE ONLY v1.decisiones
    ADD CONSTRAINT decisiones_userid_fkey FOREIGN KEY (userid) REFERENCES v1.usuarios(userid) ON DELETE CASCADE;


--
-- Name: equipos equipos_proyid_fkey; Type: FK CONSTRAINT; Schema: v1; Owner: postgres
--

ALTER TABLE ONLY v1.equipos
    ADD CONSTRAINT equipos_proyid_fkey FOREIGN KEY (proyid) REFERENCES v1.proyectos(proyid) ON DELETE CASCADE;


--
-- Name: equipos equipos_userid_fkey; Type: FK CONSTRAINT; Schema: v1; Owner: postgres
--

ALTER TABLE ONLY v1.equipos
    ADD CONSTRAINT equipos_userid_fkey FOREIGN KEY (userid) REFERENCES v1.usuarios(userid);


--
-- Name: funciones_rol funciones_rol_accionid_fkey; Type: FK CONSTRAINT; Schema: v1; Owner: postgres
--

ALTER TABLE ONLY v1.funciones_rol
    ADD CONSTRAINT funciones_rol_accionid_fkey FOREIGN KEY (accionid) REFERENCES v1.acciones(accionid) ON DELETE CASCADE;


--
-- Name: funciones_rol funciones_rol_rolid_fkey; Type: FK CONSTRAINT; Schema: v1; Owner: postgres
--

ALTER TABLE ONLY v1.funciones_rol
    ADD CONSTRAINT funciones_rol_rolid_fkey FOREIGN KEY (rolid) REFERENCES v1.roles(rolid) ON DELETE CASCADE;


--
-- Name: contextos_proyecto proyid_fkey; Type: FK CONSTRAINT; Schema: v1; Owner: postgres
--

ALTER TABLE ONLY v1.contextos_proyecto
    ADD CONSTRAINT proyid_fkey FOREIGN KEY (proyid) REFERENCES v1.proyectos(proyid) ON DELETE CASCADE;


--
-- Name: tareas tareas_instrid_fkey; Type: FK CONSTRAINT; Schema: v1; Owner: postgres
--

ALTER TABLE ONLY v1.tareas
    ADD CONSTRAINT tareas_instrid_fkey FOREIGN KEY (instrid) REFERENCES v1.instrumentos(instrid) ON DELETE CASCADE;


--
-- Name: tareas tareas_proyid_fkey; Type: FK CONSTRAINT; Schema: v1; Owner: postgres
--

ALTER TABLE ONLY v1.tareas
    ADD CONSTRAINT tareas_proyid_fkey FOREIGN KEY (proyid) REFERENCES v1.proyectos(proyid) ON DELETE CASCADE;


--
-- Name: usuarios usuarios_rolid_fkey; Type: FK CONSTRAINT; Schema: v1; Owner: postgres
--

ALTER TABLE ONLY v1.usuarios
    ADD CONSTRAINT usuarios_rolid_fkey FOREIGN KEY (rolid) REFERENCES v1.roles(rolid) ON DELETE CASCADE;


--
-- Name: SCHEMA v1; Type: ACL; Schema: -; Owner: postgres
--

GRANT ALL ON SCHEMA v1 TO opc;


--
-- Name: TABLE acciones; Type: ACL; Schema: v1; Owner: postgres
--

GRANT ALL ON TABLE v1.acciones TO opc;


--
-- Name: TABLE contextos; Type: ACL; Schema: v1; Owner: postgres
--

GRANT ALL ON TABLE v1.contextos TO opc;


--
-- Name: TABLE contextos_proyecto; Type: ACL; Schema: v1; Owner: postgres
--

GRANT ALL ON TABLE v1.contextos_proyecto TO opc;


--
-- Name: TABLE datos_contexto; Type: ACL; Schema: v1; Owner: postgres
--

GRANT ALL ON TABLE v1.datos_contexto TO opc;


--
-- Name: TABLE decisiones; Type: ACL; Schema: v1; Owner: postgres
--

GRANT ALL ON TABLE v1.decisiones TO opc;


--
-- Name: TABLE decisiones_proyecto; Type: ACL; Schema: v1; Owner: postgres
--

GRANT ALL ON TABLE v1.decisiones_proyecto TO opc;


--
-- Name: TABLE equipos; Type: ACL; Schema: v1; Owner: postgres
--

GRANT ALL ON TABLE v1.equipos TO opc;


--
-- Name: TABLE funciones_rol; Type: ACL; Schema: v1; Owner: postgres
--

GRANT ALL ON TABLE v1.funciones_rol TO opc;


--
-- Name: TABLE instrumentos; Type: ACL; Schema: v1; Owner: postgres
--

GRANT ALL ON TABLE v1.instrumentos TO opc;


--
-- Name: TABLE parametros; Type: ACL; Schema: v1; Owner: postgres
--

GRANT ALL ON TABLE v1.parametros TO opc;


--
-- Name: TABLE proyectos; Type: ACL; Schema: v1; Owner: postgres
--

GRANT ALL ON TABLE v1.proyectos TO opc;


--
-- Name: TABLE roles; Type: ACL; Schema: v1; Owner: postgres
--

GRANT ALL ON TABLE v1.roles TO opc;


--
-- Name: TABLE tareas; Type: ACL; Schema: v1; Owner: postgres
--

GRANT ALL ON TABLE v1.tareas TO opc;


--
-- Name: TABLE usuarios; Type: ACL; Schema: v1; Owner: postgres
--

GRANT ALL ON TABLE v1.usuarios TO opc;


--
-- PostgreSQL database dump complete
--

