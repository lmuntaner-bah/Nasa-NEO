--For Microsoft SQL Server
USE master;

CREATE TABLE near_earth_objects (
    id INT PRIMARY KEY,
    neo_reference_id INT,
    official_name NVARCHAR(MAX),
    short_name NVARCHAR(MAX),
    designation NVARCHAR(MAX),
    absolute_magnitude_h FLOAT,
    is_potentially_hazardous_asteroid BIT,
    is_sentry_object BIT,
    kilometers_estimated_diameter_min FLOAT,
    kilometers_estimated_diameter_max FLOAT,
    orbit_id NVARCHAR(MAX),
    orbit_class_type NVARCHAR(MAX),
    perihelion_distance FLOAT,
    aphelion_distance FLOAT,
    first_date_detected NVARCHAR(MAX),
    last_date_detected NVARCHAR(MAX),
    orbit_class_description NVARCHAR(MAX)
);

CREATE TABLE NEO_BI_Dashboard (
    id INT PRIMARY KEY,
    official_name NVARCHAR(MAX),
    short_name NVARCHAR(MAX),
    absolute_magnitude_h FLOAT,
    is_potentially_hazardous_asteroid BIT,
    is_sentry_object BIT,
    kilometers_estimated_diameter_min FLOAT,
    kilometers_estimated_diameter_max FLOAT,
    perihelion_distance FLOAT,
    aphelion_distance FLOAT,
    first_date_detected NVARCHAR(MAX),
    last_date_detected NVARCHAR(MAX),
    orbit_class_description NVARCHAR(MAX)
);