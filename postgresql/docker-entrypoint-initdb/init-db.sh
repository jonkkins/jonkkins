#!/bin/bash
set -e

JONKKINS_PASSWD=`cat /run/secrets/jonkkins-passwd`
POSTGRES_PASSWD=`cat /run/secrets/postgres-passwd`

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    -- Initialize root database
    CREATE USER root WITH PASSWORD '${POSTGRES_PASSWD}';
    CREATE DATABASE root;
    GRANT ALL PRIVILEGES ON DATABASE root TO root;

    -- User creations
    CREATE USER login_usr WITH PASSWORD '${JONKKINS_PASSWD}';
EOSQL

psql -v ON_ERROR_STOP=1 --username="root" --dbname="root" <<-EOSQL
    -- Create Schema
    CREATE SCHEMA login_sc;

    -- Grant basic CRUD to user(s)
    GRANT SELECT, UPDATE, DELETE, INSERT ON ALL TABLES IN SCHEMA login_sc TO login_usr;

    -- Schema stuff
    CREATE TABLE login_tbl(
        id SERIAL PRIMARY KEY,
        username VARCHAR(32) UNIQUE NOT NULL,
        password VARCHAR(61) NOT NULL
    );
EOSQL