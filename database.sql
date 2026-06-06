-- MS-AUTH
CREATE TABLE usuarios (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(150) NOT NULL UNIQUE,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    rol ENUM('administrador', 'gestion_humana', 'empleado') NOT NULL,
    token VARCHAR(255) NULL,
    sesion_activa BOOLEAN DEFAULT FALSE,
    estado ENUM('activo', 'inactivo') DEFAULT 'activo',
    created_at TIMESTAMP NULL DEFAULT NULL,
    updated_at TIMESTAMP NULL DEFAULT NULL
);

-- MS-EMPLEADOS
CREATE TABLE empleados (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombres VARCHAR(100) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    documento VARCHAR(30) NOT NULL UNIQUE,
    correo VARCHAR(150) NOT NULL UNIQUE,
    telefono VARCHAR(30) NOT NULL,
    cargo VARCHAR(100) NOT NULL,
    area VARCHAR(100) NOT NULL,
    fecha_ingreso DATE NOT NULL,
    estado ENUM('activo', 'inactivo') DEFAULT 'activo',
    created_at TIMESTAMP NULL DEFAULT NULL,
    updated_at TIMESTAMP NULL DEFAULT NULL
);

-- MS-INCAPACIDADES
CREATE TABLE incapacidades (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    empleado_id BIGINT UNSIGNED NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    tipo ENUM('enfermedad_general','accidente_laboral','licencia_medica','incapacidad_temporal') NOT NULL,
    diagnostico_general TEXT NOT NULL,
    entidad_medica VARCHAR(150) NOT NULL,
    observaciones TEXT NULL,
    dias_incapacidad INT NOT NULL,
    estado ENUM('registrada','en_revision','aprobada','rechazada','finalizada') DEFAULT 'registrada',
    created_at TIMESTAMP NULL DEFAULT NULL,
    updated_at TIMESTAMP NULL DEFAULT NULL
);

-- MS-SEGUIMIENTO
CREATE TABLE seguimientos (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    incapacidad_id BIGINT UNSIGNED NOT NULL,
    fecha DATE NOT NULL,
    comentario TEXT NOT NULL,
    estado ENUM('registrada','en_revision','aprobada','rechazada','finalizada') NOT NULL,
    usuario_responsable VARCHAR(100) NOT NULL,
    created_at TIMESTAMP NULL DEFAULT NULL,
    updated_at TIMESTAMP NULL DEFAULT NULL
);