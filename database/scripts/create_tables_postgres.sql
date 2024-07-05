--For PostgreSQL
CREATE TABLE IF NOT EXISTS public.neo_dashboard
(
    id integer NOT NULL,
    official_name character varying COLLATE pg_catalog."default",
    short_name character varying COLLATE pg_catalog."default",
    absolute_magnitude_h numeric,
    is_potentially_hazardous_asteroid boolean,
    is_sentry_object boolean,
    kilometers_estimated_diameter_min numeric,
    kilometers_estimated_diameter_max numeric,
    perihelion_distance numeric,
    aphelion_distance numeric,
    first_date_detected timestamp without time zone,
    last_date_detected timestamp without time zone,
    orbit_class_description character varying COLLATE pg_catalog."default",
    CONSTRAINT neo_dashboard_pkey PRIMARY KEY (id)
)