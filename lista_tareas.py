#!/usr/bin/env python3
"""
Aplicación Simple de Lista de Tareas
Una herramienta de línea de comandos para gestionar tareas con almacenamiento persistente.
"""

import json
import os
from datetime import datetime
from typing import List, Dict

class AppTareas:
    def __init__(self, archivo: str = "tareas.json"):
        self.archivo = archivo
        self.tareas: List[Dict] = []
        self.cargar_tareas()
    
    def cargar_tareas(self) -> None:
        """Cargar tareas desde el archivo JSON."""
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r', encoding='utf-8') as f:
                    self.tareas = json.load(f)
            except json.JSONDecodeError:
                print("⚠️  Error al cargar tareas. Comenzando de nuevo.")
                self.tareas = []
        else:
            self.tareas = []
    
    def guardar_tareas(self) -> None:
        """Guardar tareas en el archivo JSON."""
        with open(self.archivo, 'w', encoding='utf-8') as f:
            json.dump(self.tareas, f, indent=2, ensure_ascii=False)
    
    def agregar_tarea(self, descripcion: str, prioridad: str = "media") -> None:
        """Agregar una nueva tarea."""
        tarea = {
            "id": len(self.tareas) + 1,
            "descripcion": descripcion,
            "prioridad": prioridad.lower(),
            "completada": False,
            "creada_en": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tareas.append(tarea)
        self.guardar_tareas()
        print(f"✅ Tarea agregada: {descripcion}")
    
    def listar_tareas(self, mostrar_completadas: bool = True) -> None:
        """Mostrar todas las tareas."""
        if not self.tareas:
            print("📝 No hay tareas. ¡Agrega una para comenzar!")
            return
        
        print("\n" + "="*60)
        print("TU LISTA DE TAREAS".center(60))
        print("="*60 + "\n")
        
        for tarea in self.tareas:
            if not mostrar_completadas and tarea["completada"]:
                continue
            
            estado = "✓" if tarea["completada"] else " "
            icono_prioridad = {"alta": "🔴", "media": "🟡", "baja": "🟢"}.get(tarea["prioridad"], "⚪")
            
            print(f"[{estado}] {tarea['id']}. {icono_prioridad} {tarea['descripcion']}")
            print(f"    Prioridad: {tarea['prioridad'].upper()} | Creada: {tarea['creada_en']}")
            print()
    
    def completar_tarea(self, id_tarea: int) -> None:
        """Marcar una tarea como completada."""
        for tarea in self.tareas:
            if tarea["id"] == id_tarea:
                tarea["completada"] = True
                self.guardar_tareas()
                print(f"🎉 ¡Tarea {id_tarea} completada!")
                return
        print(f"❌ Tarea {id_tarea} no encontrada.")
    
    def eliminar_tarea(self, id_tarea: int) -> None:
        """Eliminar una tarea."""
        self.tareas = [tarea for tarea in self.tareas if tarea["id"] != id_tarea]
        self.guardar_tareas()
        print(f"🗑️  Tarea {id_tarea} eliminada.")
    
    def limpiar_completadas(self) -> None:
        """Eliminar todas las tareas completadas."""
        cantidad_inicial = len(self.tareas)
        self.tareas = [tarea for tarea in self.tareas if not tarea["completada"]]
        eliminadas = cantidad_inicial - len(self.tareas)
        self.guardar_tareas()
        print(f"🧹 Se limpiaron {eliminadas} tarea(s) completada(s).")

def main():
    app = AppTareas()
    
    print("\n🎯 ¡Bienvenido a tu Lista de Tareas!")
    
    while True:
        print("\n" + "-"*40)
        print("Comandos:")
        print("  agregar <tarea> [prioridad]  - Agregar nueva tarea")
        print("  listar                       - Mostrar todas las tareas")
        print("  listar pendientes            - Mostrar tareas pendientes")
        print("  completar <id>               - Marcar tarea como hecha")
        print("  eliminar <id>                - Eliminar una tarea")
        print("  limpiar                      - Borrar tareas completadas")
        print("  salir                        - Salir de la aplicación")
        print("-"*40)
        
        comando = input("\n> ").strip().lower()
        
        if comando.startswith("agregar "):
            partes = comando[8:].split()
            if len(partes) >= 1:
                descripcion = " ".join(partes[:-1] if partes[-1] in ["alta", "media", "baja"] else partes)
                prioridad = partes[-1] if partes[-1] in ["alta", "media", "baja"] else "media"
                app.agregar_tarea(descripcion, prioridad)
            else:
                print("❌ Por favor proporciona una descripción de la tarea.")
        
        elif comando == "listar":
            app.listar_tareas()
        
        elif comando == "listar pendientes":
            app.listar_tareas(mostrar_completadas=False)
        
        elif comando.startswith("completar "):
            try:
                id_tarea = int(comando.split()[1])
                app.completar_tarea(id_tarea)
            except (ValueError, IndexError):
                print("❌ Por favor proporciona un ID de tarea válido.")
        
        elif comando.startswith("eliminar "):
            try:
                id_tarea = int(comando.split()[1])
                app.eliminar_tarea(id_tarea)
            except (ValueError, IndexError):
                print("❌ Por favor proporciona un ID de tarea válido.")
        
        elif comando == "limpiar":
            app.limpiar_completadas()
        
        elif comando == "salir":
            print("\n👋 ¡Adiós! ¡Mantente productivo!")
            break
        
        else:
            print("❌ Comando desconocido. Intenta de nuevo.")

if __name__ == "__main__":
    main()