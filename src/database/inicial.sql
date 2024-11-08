-- Conectarse a la base de datos recién creada
--\c thesis

/*
TIPO_REGISTRO:
-> Persona / Entidad - Registros de personas / entidades (empresa)
-> Animal - Registros de animales individuales.
-> Parto - Registros de partos dentro de la ganadería.
-> Venta - Registros de ventas de animales.
-> Compra - Registros de compras de animales.
-> Vacunación - Registros de eventos de vacunación.
-> Alimentación - Registros de programas de alimentación o dietas.
-> Enfermedad - Registros de diagnósticos o tratamientos de enfermedades.
-> Producción - Registros de producción (leche, carne, etc.).

ESTADO_REGISTRO:
-> Activo - El registro está vigente y es relevante.
-> Inactivo - El registro no es relevante actualmente, pero se conserva.
-> Eliminado - El registro ha sido eliminado lógicamente del sistema.
-> Pendiente - El registro está en espera de una acción o verificación.
-> Finalizado - El registro corresponde a un evento o acción ya completada.
*/

-- Habilitar las extensiones necesarias
CREATE EXTENSION IF NOT EXISTS pgcrypto;
CREATE EXTENSION IF NOT EXISTS plpgsql;
CREATE EXTENSION IF NOT EXISTS pldbgapi;

CREATE TABLE IF NOT EXISTS public.fauditoria (
    id_auditoria SERIAL,
    parcial SERIAL,
    nombre_tabla VARCHAR(20) NOT NULL,
    tipo_tabla_tipo_operacion INTEGER NOT NULL,
    codigo_tabla_tipo_operacion INTEGER NOT NULL,
    id_registro INTEGER NOT NULL,
    descripcion VARCHAR(100) NOT NULL,
    fecha_operacion DATE NOT NULL,
    usuario_operacion VARCHAR(10) NOT NULL,
    CONSTRAINT fauditoria_pk PRIMARY KEY (id_auditoria, parcial)
);


CREATE TABLE IF NOT EXISTS public.fpermisos (
    id_permiso SERIAL,
    nombre_permiso VARCHAR(10) NOT NULL,
    descripcion VARCHAR(100) NOT NULL,
    CONSTRAINT fpermisos_pk PRIMARY KEY (id_permiso)
);


CREATE TABLE IF NOT EXISTS public.froles (
    id_rol SERIAL,
    nombre_rol VARCHAR(10) NOT NULL,
    descripcion VARCHAR(100) NOT NULL,
    CONSTRAINT froles_pk PRIMARY KEY (id_rol)
);


CREATE TABLE IF NOT EXISTS public.froles_permisos (
    id_rol_perm SERIAL,
    id_rol INTEGER NOT NULL,
    id_permiso INTEGER NOT NULL,
    CONSTRAINT froles_permisos_pk PRIMARY KEY (id_rol_perm)
);


CREATE TABLE IF NOT EXISTS public.fgeneral (
    id_persona SERIAL,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    telefono VARCHAR(50) NOT NULL,
    correo_electronico VARCHAR(100) NOT NULL,
    tipo_tabla_estado_civil INTEGER NOT NULL,
    codigo_tabla_estado_civil INTEGER NOT NULL,
    tipo_tabla_estado_registro INTEGER NOT NULL,
    codigo_tabla_estado_registro INTEGER NOT NULL,
    tipo_tabla_tipo_registro INTEGER NOT NULL,
    codigo_tabla_tipo_registro INTEGER NOT NULL,
    documento VARCHAR(15) NOT NULL,
    tipo_tabla_tipo_documento INTEGER NOT NULL,
    codigo_tabla_tipo_documento INTEGER NOT NULL,
    CONSTRAINT fgeneral_pk PRIMARY KEY (id_persona)
);


CREATE TABLE IF NOT EXISTS public.fusuarios (
    id_usuario SERIAL,
    id_persona INTEGER NOT NULL,
    operador VARCHAR(10) NOT NULL,
    contrasena VARCHAR(60) NOT NULL,
    tipo_tabla_estado_registro INTEGER NOT NULL,
    codigo_tabla_estado_registro INTEGER NOT NULL,
    tipo_tabla_tipo_registro INTEGER NOT NULL,
    codigo_tabla_tipo_registro INTEGER NOT NULL,
    CONSTRAINT fusuarios_pk PRIMARY KEY (id_usuario)
);


CREATE TABLE IF NOT EXISTS public.fusuarios_roles (
    id_usu_rol SERIAL,
    id_rol INTEGER NOT NULL,
    id_usuario INTEGER NOT NULL,
    CONSTRAINT fusuarios_roles_pk PRIMARY KEY (id_usu_rol)
);


CREATE TABLE IF NOT EXISTS public.fcapacitacion (
    id_capacitacion SERIAL,
    id_capacitor INTEGER NOT NULL,
    descripcion VARCHAR(100) NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    resultado VARCHAR(100) NOT NULL,
    CONSTRAINT fcapacitacion_pk PRIMARY KEY (id_capacitacion)
);


CREATE TABLE IF NOT EXISTS public.findicadores_rendimiento (
    id_indicador SERIAL,
    id_capacitacion INTEGER NOT NULL,
    tipo_tabla_tipo_indicador INTEGER NOT NULL,
    codigo_tabla_tipo_indicador INTEGER NOT NULL,
    valor INTEGER NOT NULL,
    fecha DATE NOT NULL,
    CONSTRAINT findicadores_rendimiento_pk PRIMARY KEY (id_indicador)
);


CREATE TABLE IF NOT EXISTS public.fempresa (
    id_empresa INTEGER NOT NULL,
    id_propietario INTEGER NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(150) NOT NULL,
    telefono VARCHAR(50) NOT NULL,
    correo_electronico VARCHAR(100) NOT NULL,
    tipo_tabla_tipo_ganaderia INTEGER NOT NULL,
    codigo_tabla_tipo_ganaderia INTEGER NOT NULL,
    total_animales INTEGER NOT NULL,
    CONSTRAINT fempresa_pk PRIMARY KEY (id_empresa)
);


CREATE TABLE IF NOT EXISTS public.fcontabilidad (
    id_contabilidad SERIAL,
    id_empresa INTEGER NOT NULL,
    tipo_tabla_tipo_transaccion INTEGER NOT NULL,
    codigo_tabla_tipo_transaccion INTEGER NOT NULL,
    monto NUMERIC(18,2) NOT NULL,
    fecha DATE NOT NULL,
    descripcion VARCHAR(100) NOT NULL,
    CONSTRAINT fcontabilidad_pk PRIMARY KEY (id_contabilidad)
);


CREATE TABLE IF NOT EXISTS public.fventas (
    id_venta SERIAL,
    id_cliente INTEGER NOT NULL,
    fecha_venta DATE NOT NULL,
    cantidad_vendida REAL NOT NULL,
    precio_total NUMERIC(18,2) NOT NULL,
    moneda INTEGER NOT NULL,
    CONSTRAINT fventas_pk PRIMARY KEY (id_venta)
);


CREATE TABLE IF NOT EXISTS public.fproducto_final (
    id_producto_final SERIAL,
    descripcion VARCHAR(100) NOT NULL,
    fecha_produccion DATE NOT NULL,
    cantidad_producida REAL NOT NULL,
    CONSTRAINT fproducto_final_pk PRIMARY KEY (id_producto_final)
);


CREATE TABLE IF NOT EXISTS public.fventa_detalle (
    id_detalle SERIAL,
    id_producto_final INTEGER NOT NULL,
    id_venta INTEGER NOT NULL,
    cantidad REAL NOT NULL,
    precio_unitario NUMERIC(18,2) NOT NULL,
    total_item NUMERIC(18,2) NOT NULL,
    CONSTRAINT fventa_detalle_pk PRIMARY KEY (id_detalle)
);


CREATE TABLE IF NOT EXISTS public.fanimal (
    id_animal SERIAL,
    id_empresa INTEGER NOT NULL,
    tipo_tabla_tipo_animal INTEGER NOT NULL,
    codigo_tabla_tipo_animal INTEGER NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    peso REAL NOT NULL,
    tipo_tabla_estado_registro INTEGER NOT NULL,
    codigo_tabla_estado_registro INTEGER NOT NULL,
    tipo_tabla_estado_salud INTEGER NOT NULL,
    codigo_tabla_estado_salud INTEGER NOT NULL,
    CONSTRAINT fanimal_pk PRIMARY KEY (id_animal)
);


CREATE TABLE IF NOT EXISTS public.fhistoriales_medicos (
    id_historial SERIAL,
    id_animal INTEGER NOT NULL,
    descripcion VARCHAR(100) NOT NULL,
    fecha DATE NOT NULL,
    CONSTRAINT fhistoriales_medicos_pk PRIMARY KEY (id_historial)
);


CREATE TABLE IF NOT EXISTS public.fresultados_examenes (
    id_historial_examen SERIAL,
    id_historial INTEGER NOT NULL,
    id_animal INTEGER NOT NULL,
    tipo_tabla_tipo_examen INTEGER NOT NULL,
    codigo_tabla_tipo_examen INTEGER NOT NULL,
    resultado VARCHAR(100) NOT NULL,
    fecha DATE NOT NULL,
    CONSTRAINT fresultados_examenes_pk PRIMARY KEY (id_historial_examen)
);


CREATE TABLE IF NOT EXISTS public.fdietas (
    id_dieta SERIAL,
    id_animal INTEGER NOT NULL,
    tipo_tabla_tipo_dieta INTEGER NOT NULL,
    codigo_tabla_tipo_dieta INTEGER NOT NULL,
    descripcion VARCHAR(100) NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    CONSTRAINT fdietas_pk PRIMARY KEY (id_dieta)
);


CREATE TABLE IF NOT EXISTS public.falimentacion (
    id_alimentacion SERIAL,
    id_dieta INTEGER NOT NULL,
    tipo_tabla_tipo_alimento INTEGER NOT NULL,
    codigo_tabla_tipo_alimento INTEGER NOT NULL,
    cantidad REAL NOT NULL,
    fecha DATE NOT NULL,
    CONSTRAINT falimentacion_pk PRIMARY KEY (id_alimentacion, id_dieta)
);


CREATE TABLE IF NOT EXISTS public.ftratamientos (
    id_tratamiento SERIAL,
    descripcion VARCHAR(100) NOT NULL,
    duracion INTEGER NOT NULL,
    CONSTRAINT ftratamientos_pk PRIMARY KEY (id_tratamiento)
);


CREATE TABLE IF NOT EXISTS public.ftratamientos_aplicados (
    id_tratamiento_apli SERIAL,
    id_tratamiento INTEGER NOT NULL,
    id_animal INTEGER NOT NULL,
    descripcion VARCHAR(100) NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    resultado VARCHAR(100) NOT NULL,
    CONSTRAINT ftratamientos_aplicados_pk PRIMARY KEY (id_tratamiento_apli)
);


CREATE TABLE IF NOT EXISTS public.fmedidas_preventivas (
    id_medida SERIAL,
    id_animal INTEGER NOT NULL,
    tipo_tabla_tipo_medida INTEGER NOT NULL,
    codigo_tabla_tipo_medida INTEGER NOT NULL,
    descripcion VARCHAR(100) NOT NULL,
    fecha DATE NOT NULL,
    CONSTRAINT fmedidas_preventivas_pk PRIMARY KEY (id_medida)
);


CREATE TABLE IF NOT EXISTS public.fmateria_prima (
    id_prima SERIAL,
    id_animal INTEGER NOT NULL,
    descripcion VARCHAR(100) NOT NULL,
    fecha_obtencion DATE NOT NULL,
    cantidad REAL NOT NULL,
    CONSTRAINT fmateria_prima_pk PRIMARY KEY (id_prima, id_animal)
);


CREATE TABLE IF NOT EXISTS public.fproduccion (
    id_produccion SERIAL,
    id_prima INTEGER NOT NULL,
    id_producto_final INTEGER NOT NULL,
    id_animal INTEGER NOT NULL,
    cantidad_usada REAL NOT NULL,
    CONSTRAINT fproduccion_pk PRIMARY KEY (id_produccion, id_prima, id_producto_final, id_animal)
);


CREATE TABLE IF NOT EXISTS public.ftablacod (
    id_tabla SERIAL,
    descripcion VARCHAR(100) NOT NULL,
    CONSTRAINT ftablacod_pk PRIMARY KEY (id_tabla)
);


CREATE TABLE IF NOT EXISTS public.ftabla (
    id_tabla INTEGER NOT NULL,
    id_valor SERIAL,
    descripcion VARCHAR(100) NOT NULL,
    CONSTRAINT ftabla_pk PRIMARY KEY (id_tabla, id_valor)
);


CREATE TABLE IF NOT EXISTS public.fmoneda (
    id_moneda SERIAL,
    nombre VARCHAR(100) NOT NULL,
    tipo_tabla_tipo_moneda INTEGER NOT NULL,
    codigo_tabla_tipo_moneda INTEGER NOT NULL,
    CONSTRAINT fmoneda_pk PRIMARY KEY (id_moneda)
);


CREATE TABLE IF NOT EXISTS public.fcambio (
    id_cambio SERIAL,
    moneda INTEGER,
    importe FLOAT NOT NULL,
    fecha DATE NOT NULL,
    confirmado VARCHAR(1) NOT NULL,
    CONSTRAINT fcambio_pk PRIMARY KEY (id_cambio)
);

-------------------------------FK-------------------------------
DO $$
BEGIN
    ALTER TABLE public.froles_permisos
    ADD CONSTRAINT fpermisos_froles_permisos_fk
    FOREIGN KEY (id_permiso)
    REFERENCES public.fpermisos (id_permiso)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN
    -- No hacer nada si la restricción ya existe.
END $$;

DO $$
BEGIN
    ALTER TABLE public.fusuarios_roles ADD CONSTRAINT froles_fusuarios_roles_fk
    FOREIGN KEY (id_rol)
    REFERENCES public.froles (id_rol)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN
    -- No hacer nada si la restricción ya existe.
END $$;

DO $$
BEGIN
    ALTER TABLE public.froles_permisos ADD CONSTRAINT froles_froles_permisos_fk
    FOREIGN KEY (id_rol)
    REFERENCES public.froles (id_rol)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN
    -- No hacer nada si la restricción ya existe.
END $$;

DO $$
BEGIN
    ALTER TABLE public.fventas ADD CONSTRAINT fgeneral_fventas_fk
    FOREIGN KEY (id_cliente)
    REFERENCES public.fgeneral (id_persona)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN
    -- No hacer nada si la restricción ya existe.
END $$;

DO $$
BEGIN
    ALTER TABLE public.fempresa ADD CONSTRAINT fgeneral_fempresa_fk
    FOREIGN KEY (id_propietario)
    REFERENCES public.fgeneral (id_persona)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN
    -- No hacer nada si la restricción ya existe.
END $$;

DO $$
BEGIN
    ALTER TABLE public.fcapacitacion ADD CONSTRAINT fgeneral_fcapacitacion_fk
    FOREIGN KEY (id_capacitor)
    REFERENCES public.fgeneral (id_persona)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN
    -- No hacer nada si la restricción ya existe.
END $$;

DO $$
BEGIN
    ALTER TABLE public.fusuarios ADD CONSTRAINT fgeneral_fusuarios_fk
    FOREIGN KEY (id_persona)
    REFERENCES public.fgeneral (id_persona)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN
    -- No hacer nada si la restricción ya existe.
END $$;

DO $$
BEGIN
    ALTER TABLE public.fusuarios_roles ADD CONSTRAINT fusuarios_fusuarios_roles_fk
    FOREIGN KEY (id_usuario)
    REFERENCES public.fusuarios (id_usuario)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN
    -- No hacer nada si la restricción ya existe.
END $$;

DO $$
BEGIN
    ALTER TABLE public.findicadores_rendimiento ADD CONSTRAINT fcapacitacion_findicadores_rendimiento_fk
    FOREIGN KEY (id_capacitacion)
    REFERENCES public.fcapacitacion (id_capacitacion)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN
    -- No hacer nada si la restricción ya existe.
END $$;

DO $$
BEGIN
    ALTER TABLE public.fanimal ADD CONSTRAINT fempresa_fanimal_fk
    FOREIGN KEY (id_empresa)
    REFERENCES public.fempresa (id_empresa)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN
    -- No hacer nada si la restricción ya existe.
END $$;

DO $$
BEGIN
    ALTER TABLE public.fcontabilidad ADD CONSTRAINT fempresa_fcontabilidad_fk
    FOREIGN KEY (id_empresa)
    REFERENCES public.fempresa (id_empresa)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN
    -- No hacer nada si la restricción ya existe.
END $$;

DO $$
BEGIN
    ALTER TABLE public.fventa_detalle ADD CONSTRAINT fventas_fventa_detalle_fk
    FOREIGN KEY (id_venta)
    REFERENCES public.fventas (id_venta)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN
    -- No hacer nada si la restricción ya existe.
END $$;

DO $$
BEGIN
    ALTER TABLE public.fproduccion ADD CONSTRAINT fproducto_final_fproduccion_fk
    FOREIGN KEY (id_producto_final)
    REFERENCES public.fproducto_final (id_producto_final)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN
    -- No hacer nada si la restricción ya existe.
END $$;

DO $$
BEGIN
    ALTER TABLE public.fventa_detalle ADD CONSTRAINT fproducto_final_fventa_detalle_fk
    FOREIGN KEY (id_producto_final)
    REFERENCES public.fproducto_final (id_producto_final)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN
    -- No hacer nada si la restricción ya existe.
END $$;

DO $$
BEGIN
    ALTER TABLE public.fmateria_prima ADD CONSTRAINT fanimal_fmateria_prima_fk
    FOREIGN KEY (id_animal)
    REFERENCES public.fanimal (id_animal)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN
    -- No hacer nada si la restricción ya existe.
END $$;

DO $$
BEGIN
    ALTER TABLE public.fmedidas_preventivas ADD CONSTRAINT fanimal_fmedidas_preventivas_fk
    FOREIGN KEY (id_animal)
    REFERENCES public.fanimal (id_animal)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN
    -- No hacer nada si la restricción ya existe.
END $$;

DO $$
BEGIN
    ALTER TABLE public.ftratamientos ADD CONSTRAINT fanimal_ftratamientos_fk
    FOREIGN KEY (id_animal)
    REFERENCES public.fanimal (id_animal)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN
    -- No hacer nada si la restricción ya existe.
END $$;

DO $$
BEGIN
    ALTER TABLE public.fdietas ADD CONSTRAINT fanimal_fdietas_fk
    FOREIGN KEY (id_animal)
    REFERENCES public.fanimal (id_animal)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN
    -- No hacer nada si la restricción ya existe.
END $$;

DO $$
BEGIN
    ALTER TABLE public.fhistoriales_medicos ADD CONSTRAINT fanimal_fhistoriales_medicos_fk
    FOREIGN KEY (id_animal)
    REFERENCES public.fanimal (id_animal)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN
    -- No hacer nada si la restricción ya existe.
END $$;

DO $$
BEGIN
    ALTER TABLE public.ftratamientos_aplicados ADD CONSTRAINT fanimal_ftratamientos_aplicados_fk
    FOREIGN KEY (id_animal)
    REFERENCES public.fanimal (id_animal)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN
    -- No hacer nada si la restricción ya existe.
END $$;

DO $$
BEGIN
    ALTER TABLE public.fresultados_examenes ADD CONSTRAINT fanimal_fresultados_examenes_fk
    FOREIGN KEY (id_animal)
    REFERENCES public.fanimal (id_animal)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN
    -- No hacer nada si la restricción ya existe.
END $$;

DO $$
BEGIN
    ALTER TABLE public.fresultados_examenes ADD CONSTRAINT fhistoriales_medicos_fresultados_examenes_fk
    FOREIGN KEY (id_historial)
    REFERENCES public.fhistoriales_medicos (id_historial)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN
    -- No hacer nada si la restricción ya existe.
END $$;

DO $$
BEGIN
    ALTER TABLE public.falimentacion ADD CONSTRAINT fdietas_falimentacion_fk
    FOREIGN KEY (id_dieta)
    REFERENCES public.fdietas (id_dieta)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN
    -- No hacer nada si la restricción ya existe.
END $$;

DO $$
BEGIN
    ALTER TABLE public.ftratamientos_aplicados ADD CONSTRAINT ftratamientos_ftratamientos_aplicados_fk
    FOREIGN KEY (id_tratamiento)
    REFERENCES public.ftratamientos (id_tratamiento)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN
    -- No hacer nada si la restricción ya existe.
END $$;

DO $$
BEGIN
    ALTER TABLE public.fproduccion ADD CONSTRAINT fmateria_prima_fproduccion_fk
    FOREIGN KEY (id_prima, id_animal)
    REFERENCES public.fmateria_prima (id_prima, id_animal)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN
    -- No hacer nada si la restricción ya existe.
END $$;


DO $$
BEGIN
    ALTER TABLE public.ftabla
    ADD CONSTRAINT ftabla_ftablacod_fk
    FOREIGN KEY (id_tabla)
    REFERENCES public.ftablacod (id_tabla)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN
    -- No hacer nada si la restricción ya existe.
END $$;


DO $$
BEGIN
    ALTER TABLE public.fgeneral
    ADD CONSTRAINT fgeneral_fk_estado_civil
    FOREIGN KEY (tipo_tabla_estado_civil, codigo_tabla_estado_civil)
    REFERENCES public.ftabla (id_tabla, id_valor)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN NULL;
    -- No hacer nada si la restricción ya existe.
END $$;


DO $$
BEGIN
    ALTER TABLE public.fgeneral
    ADD CONSTRAINT fgeneral_fk_estado_registro
    FOREIGN KEY (tipo_tabla_estado_registro, codigo_tabla_estado_registro)
    REFERENCES public.ftabla (id_tabla, id_valor)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN NULL;
    -- No hacer nada si la restricción ya existe.
END $$;


DO $$
BEGIN
    ALTER TABLE public.fgeneral
    ADD CONSTRAINT fgeneral_fk_tipo_registro
    FOREIGN KEY (tipo_tabla_tipo_registro, codigo_tabla_tipo_registro)
    REFERENCES public.ftabla (id_tabla, id_valor)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN NULL;
    -- No hacer nada si la restricción ya existe.
END $$;


DO $$
BEGIN
    ALTER TABLE public.fgeneral
    ADD CONSTRAINT fgeneral_fk_tipo_documento
    FOREIGN KEY (tipo_tabla_tipo_documento, codigo_tabla_tipo_documento)
    REFERENCES public.ftabla (id_tabla, id_valor)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN NULL;
    -- No hacer nada si la restricción ya existe.
END $$;


DO $$
BEGIN
    ALTER TABLE public.fempresa
    ADD CONSTRAINT fempresa_fk_tipo_ganaderia
    FOREIGN KEY (tipo_tabla_tipo_ganaderia, codigo_tabla_tipo_ganaderia)
    REFERENCES public.ftabla (id_tabla, id_valor)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN NULL;
    -- No hacer nada si la restricción ya existe.
END $$;


DO $$
BEGIN
    ALTER TABLE public.findicadores_rendimiento
    ADD CONSTRAINT findicadores_rendimiento_fk_tipo_indicador
    FOREIGN KEY (tipo_tabla_tipo_indicador, codigo_tabla_tipo_indicador)
    REFERENCES public.ftabla (id_tabla, id_valor)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN NULL;
    -- No hacer nada si la restricción ya existe.
END $$;


DO $$
BEGIN
    ALTER TABLE public.fcontabilidad
    ADD CONSTRAINT fcontabilidad_fk_tipo_transaccion
    FOREIGN KEY (tipo_tabla_tipo_transaccion, codigo_tabla_tipo_transaccion)
    REFERENCES public.ftabla (id_tabla, id_valor)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN NULL;
    -- No hacer nada si la restricción ya existe.
END $$;


DO $$
BEGIN
    ALTER TABLE public.fanimal
    ADD CONSTRAINT fanimal_fk_tipo_animal
    FOREIGN KEY (tipo_tabla_tipo_animal, codigo_tabla_tipo_animal)
    REFERENCES public.ftabla (id_tabla, id_valor)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN NULL;
    -- No hacer nada si la restricción ya existe.
END $$;


DO $$
BEGIN
    ALTER TABLE public.fresultados_examenes
    ADD CONSTRAINT fresultados_examenes_fk_tipo_examen
    FOREIGN KEY (tipo_tabla_tipo_examen, codigo_tabla_tipo_examen)
    REFERENCES public.ftabla (id_tabla, id_valor)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN NULL;
    -- No hacer nada si la restricción ya existe.
END $$;


DO $$
BEGIN
    ALTER TABLE public.fdietas
    ADD CONSTRAINT fdietas_fk_tipo_dieta
    FOREIGN KEY (tipo_tabla_tipo_dieta, codigo_tabla_tipo_dieta)
    REFERENCES public.ftabla (id_tabla, id_valor)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN NULL;
    -- No hacer nada si la restricción ya existe.
END $$;


DO $$
BEGIN
    ALTER TABLE public.falimentacion
    ADD CONSTRAINT falimentacion_fk_tipo_alimento
    FOREIGN KEY (tipo_tabla_tipo_alimento, codigo_tabla_tipo_alimento)
    REFERENCES public.ftabla (id_tabla, id_valor)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN NULL;
    -- No hacer nada si la restricción ya existe.
END $$;


DO $$
BEGIN
    ALTER TABLE public.fmedidas_preventivas
    ADD CONSTRAINT fmedidas_preventivas_fk_tipo_medida
    FOREIGN KEY (tipo_tabla_tipo_medida, codigo_tabla_tipo_medida)
    REFERENCES public.ftabla (id_tabla, id_valor)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN NULL;
    -- No hacer nada si la restricción ya existe.
END $$;


DO $$
BEGIN
    ALTER TABLE public.fventas
    ADD CONSTRAINT fventas_fk_moneda
    FOREIGN KEY (moneda)
    REFERENCES public.fmoneda (id_moneda)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN NULL;
    -- No hacer nada si la restricción ya existe.
END $$;


DO $$
BEGIN
    ALTER TABLE public.fcambio
    ADD CONSTRAINT fcambio_fk_moneda
    FOREIGN KEY (moneda)
    REFERENCES public.fmoneda (id_moneda)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN NULL;
    -- No hacer nada si la restricción ya existe.
END $$;


DO $$
BEGIN
    ALTER TABLE public.fmoneda
    ADD CONSTRAINT fmoneda_fk_tipo_moneda
    FOREIGN KEY (tipo_tabla_tipo_moneda, codigo_tabla_tipo_moneda)
    REFERENCES public.ftabla (id_tabla, id_valor)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    NOT DEFERRABLE;
EXCEPTION
    WHEN duplicate_object THEN NULL;
    -- No hacer nada si la restricción ya existe.
END $$;


-------------------------------Inserciones-------------------------------
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM public.ftablacod WHERE id_tabla = 1) THEN
        INSERT INTO public.ftablacod (id_tabla, descripcion) VALUES
            (1, 'ESTADO CIVIL');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftablacod WHERE id_tabla = 2) THEN
        INSERT INTO public.ftablacod (id_tabla, descripcion) VALUES
            (2, 'TIPO REGISTRO');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftablacod WHERE id_tabla = 3) THEN
        INSERT INTO public.ftablacod (id_tabla, descripcion) VALUES
            (3, 'TIPO OPERACION');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftablacod WHERE id_tabla = 4) THEN
        INSERT INTO public.ftablacod (id_tabla, descripcion) VALUES
            (4, 'TIPO INDICADOR');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftablacod WHERE id_tabla = 5) THEN
        INSERT INTO public.ftablacod (id_tabla, descripcion) VALUES
            (5, 'ESTADO SALUD');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftablacod WHERE id_tabla = 6) THEN
        INSERT INTO public.ftablacod (id_tabla, descripcion) VALUES
            (6, 'TIPO TRANSACCION');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftablacod WHERE id_tabla = 7) THEN
        INSERT INTO public.ftablacod (id_tabla, descripcion) VALUES
            (7, 'TIPO EXAMEN');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftablacod WHERE id_tabla = 8) THEN
        INSERT INTO public.ftablacod (id_tabla, descripcion) VALUES
            (8, 'TIPO DIETA');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftablacod WHERE id_tabla = 9) THEN
        INSERT INTO public.ftablacod (id_tabla, descripcion) VALUES
            (9, 'TIPO ALIMENTO');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftablacod WHERE id_tabla = 10) THEN
        INSERT INTO public.ftablacod (id_tabla, descripcion) VALUES
            (10, 'TIPO MEDIDA');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftablacod WHERE id_tabla = 11) THEN
        INSERT INTO public.ftablacod (id_tabla, descripcion) VALUES
            (11, 'TIPO DOCUMENTO');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftablacod WHERE id_tabla = 12) THEN
        INSERT INTO public.ftablacod (id_tabla, descripcion) VALUES
            (12, 'TIPO ANIMAL');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftablacod WHERE id_tabla = 13) THEN
        INSERT INTO public.ftablacod (id_tabla, descripcion) VALUES
            (13, 'ESTADO REGISTRO');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftablacod WHERE id_tabla = 14) THEN
        INSERT INTO public.ftablacod (id_tabla, descripcion) VALUES
            (14, 'TIPO GANADERIA');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftablacod WHERE id_tabla = 15) THEN
        INSERT INTO public.ftablacod (id_tabla, descripcion) VALUES
            (15, 'TIPO MONEDA');
    END IF;
END $$;


DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 1 AND id_valor = 1) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (1, 1, 'SOLTERO');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 1 AND id_valor = 2) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (1, 2, 'CASADO');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 1 AND id_valor = 3) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (1, 3, 'DIVORCIADO');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 1 AND id_valor = 4) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (1, 4, 'VIUDO');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 2 AND id_valor = 1) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (2, 1, 'PERSONA');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 2 AND id_valor = 2) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (2, 2, 'ENTIDAD');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 2 AND id_valor = 3) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (2, 3, 'ANIMAL');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 2 AND id_valor = 4) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (2, 4, 'PARTO');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 2 AND id_valor = 5) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (2, 5, 'USUARIO');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 3 AND id_valor = 1) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (3, 1, 'INSERTAR');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 3 AND id_valor = 2) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (3, 2, 'ACTUALIZAR');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 3 AND id_valor = 3) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (3, 3, 'ELIMINAR');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 4 AND id_valor = 1) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (4, 1, 'PRODUCTIVIDAD');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 4 AND id_valor = 2) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (4, 2, 'CALIDAD');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 5 AND id_valor = 1) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (5, 1, 'BUENO');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 5 AND id_valor = 2) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (5, 2, 'REGULAR');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 5 AND id_valor = 3) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (5, 3, 'MALO');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 6 AND id_valor = 1) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (6, 1, 'DÉBITO');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 6 AND id_valor = 2) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (6, 2, 'CRÉDITO');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 7 AND id_valor = 1) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (7, 1, 'SANGRE');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 7 AND id_valor = 2) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (7, 2, 'ORINA');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 8 AND id_valor = 1) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (8, 1, 'HERBÍVORO');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 8 AND id_valor = 2) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (8, 2, 'OMNÍVORO');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 9 AND id_valor = 1) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (9, 1, 'PASTO');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 9 AND id_valor = 2) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (9, 2, 'CONCENTRADO');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 10 AND id_valor = 1) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (10, 1, 'VACUNACIÓN');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 10 AND id_valor = 2) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (10, 2, 'DESPARASITACIÓN');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 11 AND id_valor = 1) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (11, 1, 'CEDULA DE IDENTIDAD');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 11 AND id_valor = 2) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (11, 2, 'RUC');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 12 AND id_valor = 1) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (12, 1, 'VACA');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 12 AND id_valor = 2) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (12, 2, 'TORO');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 12 AND id_valor = 3) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (12, 3, 'CABALLO');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 12 AND id_valor = 4) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (12, 4, 'YEGUA');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 13 AND id_valor = 1) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (13, 1, 'ACTIVO');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 13 AND id_valor = 2) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (13, 2, 'INACTIVO');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 14 AND id_valor = 1) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (14, 1, 'GANADERIA');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 15 AND id_valor = 1) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (15, 1, 'LOCAL');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.ftabla WHERE id_tabla = 15 AND id_valor = 2) THEN
        INSERT INTO public.ftabla (id_tabla, id_valor, descripcion) VALUES
            (15, 2, 'EXTRANJERA');
    END IF;
END $$;


-------------------------------Procedimientos-------------------------------
drop function if exists authenticate_user(text, text);

CREATE OR REPLACE FUNCTION authenticate_user(username TEXT, pass TEXT)
    RETURNS TABLE (
                      id_usuario INTEGER,
                      id_persona INTEGER,
                      operador VARCHAR(10),
                      tipo_tabla_estado_registro INTEGER,
                      codigo_tabla_estado_registro INTEGER,
                      tipo_tabla_tipo_registro INTEGER,
                      codigo_tabla_tipo_registro INTEGER
                  ) AS $$
BEGIN
    RETURN QUERY
        SELECT f.id_usuario, f.id_persona, f.operador, f.tipo_tabla_estado_registro,
               f.codigo_tabla_estado_registro, f.tipo_tabla_tipo_registro, f.codigo_tabla_tipo_registro
        FROM fusuarios f
        WHERE f.operador = username
          AND f.contrasena = crypt(pass, f.contrasena);
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION TO_SENTENCE(
    TEXTO TEXT,
    SEPARADOR VARCHAR(1) DEFAULT '',
    TIPO INTEGER DEFAULT 1
)
    RETURNS TEXT AS $$
DECLARE
    V_TEXTO TEXT := '';
    V_PARTES TEXT[];
    I INTEGER;
    V_PALABRAS TEXT[];
    J INTEGER;
BEGIN
    IF TIPO = 0 THEN
        V_PARTES := STRING_TO_ARRAY(TEXTO, ',');

        FOR I IN ARRAY_LOWER(V_PARTES, 1)..ARRAY_UPPER(V_PARTES, 1) LOOP
                V_PALABRAS := STRING_TO_ARRAY(V_PARTES[I], ' ');

                FOR J IN ARRAY_LOWER(V_PALABRAS, 1)..ARRAY_UPPER(V_PALABRAS, 1) LOOP
                        V_PALABRAS[J] := UPPER(SUBSTRING(V_PALABRAS[J] FROM 1 FOR 1)) || LOWER(SUBSTRING(V_PALABRAS[J] FROM 2));
                    END LOOP;

                V_PARTES[I] := ARRAY_TO_STRING(V_PALABRAS, ' ');
            END LOOP;

        V_TEXTO := ARRAY_TO_STRING(V_PARTES, ', ');
    ELSE
        IF SEPARADOR = '' THEN
            V_TEXTO := UPPER(SUBSTRING(TEXTO FROM 1 FOR 1)) || LOWER(SUBSTRING(TEXTO FROM 2));
        ELSE
            V_PARTES := STRING_TO_ARRAY(TEXTO, SEPARADOR);

            FOR I IN ARRAY_LOWER(V_PARTES, 1)..ARRAY_UPPER(V_PARTES, 1) LOOP

                    V_PALABRAS := STRING_TO_ARRAY(V_PARTES[I], ' ');

                    FOR J IN ARRAY_LOWER(V_PALABRAS, 1)..ARRAY_UPPER(V_PALABRAS, 1) LOOP
                            V_PALABRAS[J] := UPPER(SUBSTRING(V_PALABRAS[J] FROM 1 FOR 1)) || LOWER(SUBSTRING(V_PALABRAS[J] FROM 2));
                        END LOOP;

                    V_PARTES[I] := ARRAY_TO_STRING(V_PALABRAS, ' ');
                END LOOP;

            V_TEXTO := ARRAY_TO_STRING(V_PARTES, SEPARADOR);
        END IF;
    END IF;

    RETURN V_TEXTO;
END;
$$ LANGUAGE plpgsql;
