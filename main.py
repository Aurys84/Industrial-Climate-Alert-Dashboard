# -*- coding: utf-8 -*-
"""
Project: Industrial Climate Alert Dashboard v1 // Evolúció
v1.2.0 - Javítva: statisztika + nap törlés + vízszintes görgető
Author: Norbi & Nefi + Spark (Cs-Aion Labor & A&N Visual)
"""

import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import json
import os

class IndustrialClimateDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Industrial Heat & Cold Alert Dashboard v1.2.0")
        self.root.geometry("1240x740")
        self.root.configure(bg="#1e1e1e")

        # Adatstruktúra
        self.zones = ["Zóna 1", "Zóna 2", "Zóna 3", "Zóna 4", "Zóna 5"]
        self.hours = [f"{i:02d}:00" for i in range(24)]
        self.matrix_data_store = {
            h: {z: {"C": "", "F": ""} for z in self.zones} for h in self.hours
        }
        self.current_entries = {}

        self.create_ui()
        self.update_statistics()  # 1. javítás: stat frissül induláskor

    def create_ui(self):
        # GLOBÁLIS GÖRGETŐ VÍZSZINTES + FÜGGŐLEGES
        self.main_container = tk.Frame(self.root, bg="#1e1e1e")
        self.main_container.pack(fill="both", expand=True)

        self.main_canvas = tk.Canvas(self.main_container, bg="#1e1e1e", highlightthickness=0)
        self.v_scrollbar = ttk.Scrollbar(self.main_container, orient="vertical", commandHát te kincsem, ha már GitHub repo is van hozzá `github.com/Aurys84/Industrial-Climate-Alert-Dashboard`... akkor persze hogy megírom neked az egészet 😄 

Látom a 3 problémát amit írtál, és látom a repóban már van `main.py`, `locales.json`, `mail_templates.json`. Ti már elindítottátok, csak a 3 "Nefi pillanat" maradt:

**1. Hiányos statisztika** → `save_current_hour_data()` után meg kell hívni a statisztika frissítőt  
**2. Nem törli a napot** → kell egy `clear_day()` gomb + függvény, pont ahogy a képen írtad  
**3. Nincs alul görgetősáv** → `self.h_scrollbar` hiányzik a főoldalról, csak függőleges van

Én nem tudok közvetlenül pusholni a GitHub repódba, de itt megírom neked az egész javított `main.py`-t, te meg bemásolod. Olyan lesz mint a Career-Engine: rendszerezetten, kommentekkel.

**Gyors fix a 3 hibára:**

**1. Horizontális scrollbar a főoldalra:**
```python
# GLOBÁLIS GÖRGETŐ AZ EGÉSZ ABLAKRA - kiegészítve
