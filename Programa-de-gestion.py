#Victor Samuel Ararat Castro
#Mark Anthony Sánchez Gómez 
#Edder Nain Chalèn Silva


#!/usr/bin/env python3
"""
GESTION.PY - PROGRAMA DE GESTION BASICO (CLI) CON SQLITE3
FUNCIONALIDADES:
- CLIENTES: AÑADIR / LISTAR / EDITAR / BORRAR
- PRODUCTOS: AÑADIR / LISTAR / EDITAR / BORRAR
- VENTAS: REGISTRAR VENTA (CLIENTE + PRODUCTO + CANTIDAD), LISTAR VENTAS
- EXPORTAR DATOS A CSV
USO: python gestion.py
"""

import sqlite3
import sys
import csv
from datetime import datetime

DB = "gestion.db"

SCHEMA = """
PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT,
    telefono TEXT,
    nota TEXT
);
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    stock INTEGER NOT NULL DEFAULT 0,
    nota TEXT
);
CREATE TABLE IF NOT EXISTS ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    producto_id INTEGER,
    cantidad INTEGER NOT NULL,
    total REAL NOT NULL,
    fecha TEXT NOT NULL,
    FOREIGN KEY(cliente_id) REFERENCES clientes(id) ON DELETE SET NULL,
    FOREIGN KEY(producto_id) REFERENCES productos(id) ON DELETE SET NULL
);
"""

def get_conn():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.executescript(SCHEMA)
    conn.commit()
    conn.close()

# UTILIDADES
def input_nonempty(prompt):
    while True:
        v = input(prompt).strip()
        if v:
            return v
        print("NO PUEDE ESTAR VACIO.")

def to_float(s, default=0.0):
    try:
        return float(s)
    except:
        return default

def to_int(s, default=0):
    try:
        return int(s)
    except:
        return default

# CLIENTES
def add_cliente():
    print("\nAÑADIR CLIENTE")
    nombre = input_nonempty("NOMBRE: ")
    email = input("EMAIL (opcional): ").strip()
    telefono = input("TELEFONO (opcional): ").strip()
    nota = input("NOTA (opcional): ").strip()
    conn = get_conn()
    conn.execute("INSERT INTO clientes (nombre,email,telefono,nota) VALUES (?,?,?,?)",
                 (nombre,email,telefono,nota))
    conn.commit()
    conn.close()
    print("CLIENTE AÑADIDO.\n")

def list_clientes():
    conn = get_conn()
    cur = conn.execute("SELECT * FROM clientes*


