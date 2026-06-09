# -*- coding: utf-8 -*-
"""
Project: Industrial Climate Alert Dashboard v1
Author: Norbi (Cs-Aion Labor)
// Evolúció - Excel cellákból egy önálló, golyóálló ipari szoftverarchitektúra.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import datetime

class IndustrialClimateDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Industrial Heat & Cold Alert Dashboard v1 // Evolúció")
        self.root.geometry("1200x850")
        self.root.configure(bg="#1e1e1e") # Modern sötét ipari háttér

        # Stílusok beállítása a modern kinézhez
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TLabel", background="#1e1e1e", foreground="#ffffff", font=("Arial", 10))
        self.style.configure("TLabelframe", background="#1e1e1e", foreground="#00adb5", bordercolor="#393e46")
        self.style.configure("TLabelframe.Label", background="#1e1e1e", foreground="#00adb5", font=("Arial", 10, "bold"))
        self.style.configure("TButton", font=("Arial", 10, "bold"), background="#00adb5", foreground="#ffffff")
        
        self.zones = ["Zóna 1", "Zóna 2", "Zóna 3", "Zóna 4", "Zóna 5"]
        self.hours = [f"{i:02d}:00" for i in range(24)]
        
        self.create_ui()

    def c_to_f(self, c_val):
        """Tűpontos Celsius -> Fahrenheit konverzió"""
        try:
            return round((float(c_val) * 1.8) + 32, 1)
        except (ValueError, TypeError):
            return ""

    def update_min_f(self, *args):
        val = self.min_c_entry.get()
        f_val = self.c_to_f(val)
        self.min_f_label.config(text=f"{f_val} °F" if f_val != "" else "")

    def update_max_f(self, *args):
        val = self.max_c_entry.get()
        f_val = self.c_to_f(val)
        self.max_f_label.config(text=f"{f_val} °F" if f_val != "" else "")

    def create_ui(self):
        # 1. FELSŐ PANEL: VÉGTELENÍTETT E-MAIL CÍMEK (Outlook & Gmail kompatibilis)
        mail_frame = ttk.LabelFrame(self.root, text=" 📩 E-mail címek / Email addresses / E-Mail-Adressen (Outlook & Gmail) ")
        mail_frame.pack(fill="x", padx=15, pady=10)

        self.email_entry = tk.Entry(mail_frame, bg="#2d2d2d", fg="#ffffff", insertbackground="white", font=("Arial", 10), bd=1, relief="solid")
        self.email_entry.pack(fill="x", padx=15, pady=10)
        self.email_entry.insert(0, "manager@company.com; supervisor@gmail.com; director@corporate.de")

        # 2. HATÁRÉRTÉKEK ÉS KETTŐS VIZUÁLIS RIASZTÓ LÁMPA
        limits_frame = ttk.LabelFrame(self.root, text=" ⚙️ Határértékek & Vizuális Riasztó / Limits & Alarm Indicators ")
        limits_frame.pack(fill="x", padx=15, pady=5)

        # Minimum beállítási blokk (3 nyelven fixen kiírva)
        min_label_text = "Minimum: Riasztási Beírt érték\nMinimum: Alarm Entered Value\nMinimalwert: Alarmwert"
        tk.Label(limits_frame, text=min_label_text, justify="left", bg="#1e1e1e", fg="#ffffff", font=("Arial", 9)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        self.min_c_var = tk.StringVar()
        self.min_c_var.trace_add("write", self.update_min_f)
        self.min_c_entry = tk.Entry(limits_frame, textvariable=self.min_c_var, width=8, bg="#2d2d2d", fg="#00adb5", font=("Arial", 12, "bold"), bd=1, relief="solid", justify="center")
        self.min_c_entry.grid(row=0, column=1, padx=5, pady=10)
        self.min_c_entry.insert(0, "15.0")
        
        tk.Label(limits_frame, text="°C  =", bg="#1e1e1e", fg="#ffffff").grid(row=0, column=2, padx=2)
        self.min_f_label = tk.Label(limits_frame, text="59.0 °F", bg="#1e1e1e", fg="#00adb5", font=("Arial", 11, "bold"))
        self.min_f_label.grid(row=0, column=3, padx=5, sticky="w")

        # Maximum beállítási blokk (3 nyelven fixen kiírva)
        max_label_text = "Maximum: Riasztási Beírt érték\nMaximum: Alarm Entered value\nMaximalwert: Alarmwert eingegeben"
        tk.Label(limits_frame, text=max_label_text, justify="left", bg="#1e1e1e", fg="#ffffff", font=("Arial", 9)).grid(row=0, column=4, padx=20, pady=10, sticky="w")
        
        self.max_c_var = tk.StringVar()
        self.max_c_var.trace_add("write", self.update_max_f)
        self.max_c_entry = tk.Entry(limits_frame, textvariable=self.max_c_var, width=8, bg="#2d2d2d", fg="#ff2e63", font=("Arial", 12, "bold"), bd=1, relief="solid", justify="center")
        self.max_c_entry.grid(row=0, column=5, padx=5, pady=10)
        self.max_c_entry.insert(0, "29.3")
        
        tk.Label(limits_frame, text="°C  =", bg="#1e1e1e", fg="#ffffff").grid(row=0, column=6, padx=2)
        self.max_f_label = tk.Label(limits_frame, text="84.7 °F", bg="#1e1e1e", fg="#ff2e63", font=("Arial", 11, "bold"))
        self.max_f_label.grid(row=0, column=7, padx=5, sticky="w")

        # Állapotjelző lámpa (Minden OK / Riasztás)
        self.status_lamp = tk.Label(limits_frame, text="🟢 MINDEN OKÉ / STATUS OK / ALLES REGLER", bg="#21bf73", fg="#ffffff", font=("Arial", 10, "bold"), width=38, height=2, bd=1, relief="solid")
        self.status_lamp.grid(row=0, column=8, padx=25, pady=10, sticky="e")

        # 3. KÖZÉPSŐ PANEL: 24 ÓRÁS MÁTRIX ADATBEVITEL
        matrix_frame = ttk.LabelFrame(self.root, text=" 📊 24 órás Mátrix / 24-hour Data Entry ")
        matrix_frame.pack(fill="both", expand=True, padx=15, pady=5)

        # Dátumválasztó sor
        date_row_frame = tk.Frame(matrix_frame, bg="#1e1e1e")
        date_row_frame.pack(fill="x", padx=10, pady=5)
        tk.Label(date_row_frame, text="Dátum / Date / Datum:", bg="#1e1e1e", fg="#ffffff", font=("Arial", 10, "bold")).pack(side="left", padx=5)
        
        self.date_combo = ttk.Combobox(date_row_frame, values=[datetime.date.today().strftime("%d.%m.%Y")], width=15)
        self.date_combo.pack(side="left", padx=5)
        self.date_combo.current(0)

        # Gördíthető táblázat konténer a 24 órának
        canvas_frame = tk.Frame(matrix_frame, bg="#1e1e1e")
        canvas_frame.pack(fill="both", expand=True, padx=10, pady=5)

        canvas = tk.Canvas(canvas_frame, bg="#1e1e1e", highlightthickness=0)
        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        self.scrollable_table = tk.Frame(canvas, bg="#1e1e1e")

        self.scrollable_table.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.scrollable_table, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Táblázat Fejléc
        tk.Label(self.scrollable_table, text="Időpont óra/perc\nTime hour/minute\nUhrzeit", bg="#252a34", fg="#00adb5", font=("Arial", 9, "bold"), width=18, bd=1, relief="solid", height=3).grid(row=0, column=0, sticky="nsew")
        for col_idx, zone in enumerate(self.zones, start=1):
            tk.Label(self.scrollable_table, text=f"{zone}\nMért érték / Messwert\n(°C)", bg="#252a34", fg="#ffffff", font=("Arial", 9, "bold"), width=18, bd=1, relief="solid", height=3).grid(row=0, column=col_idx, sticky="nsew")

        # Cellák generálása a 24 órára
        self.matrix_cells = {}
        for row_idx, hour in enumerate(self.hours, start=1):
            bg_color = "#2d2d2d" if row_idx % 2 == 0 else "#252a34"
            tk.Label(self.scrollable_table, text=hour, bg=bg_color, fg="#ffffff", font=("Arial", 10, "bold"), bd=1, relief="solid").grid(row=row_idx, column=0, sticky="nsew", ipady=4)
            
            self.matrix_cells[hour] = {}
            for col_idx, zone in enumerate(self.zones, start=1):
                entry = tk.Entry(self.scrollable_table, bg="#393e46", fg="#ffffff", insertbackground="white", bd=1, relief="solid", justify="center", font=("Arial", 10))
                entry.grid(row=row_idx, column=col_idx, sticky="nsew", padx=1, pady=1)
                self.matrix_cells[hour][zone] = entry

        # 4. ALSÓ PANEL: LINKEDIN-STYLE ÉVES ÖSSZESÍTŐ ANALITIKA
        analytics_frame = ttk.LabelFrame(self.root, text=" 📈 LinkedIn-Style Analytics Dashboard (Annual Data Breakdown) ")
        analytics_frame.pack(fill="x", padx=15, pady=10)

        top_an_frame = tk.Frame(analytics_frame, bg="#1e1e1e")
        top_an_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Label(top_an_frame, text="Havi átlaghőmérséklet legördülő szövegdoboz / Monthly Selection:", bg="#1e1e1e", fg="#00adb5", font=("Arial", 9, "bold")).pack(side="left", padx=5)
        self.view_combo = ttk.Combobox(top_an_frame, values=["Havi nézet / Monthly View / Monatsansicht", "Heti nézet / Weekly View / Wochenansicht"], width=40)
        self.view_combo.pack(side="left", padx=5)
        self.view_combo.current(0)

        # Éves táblázat rács konténer (12 Hónap x 5 Zóna kettős kijelzéssel °C / °F)
        months_frame = tk.Frame(analytics_frame, bg="#1e1e1e")
        months_frame.pack(fill="x", padx=10, pady=5)

        # Hónap fejléc sor
        tk.Label(months_frame, text="Zóna / Month", bg="#252a34", fg="#00adb5", font=("Arial", 8, "bold"), width=10, bd=1, relief="solid").grid(row=0, column=0, sticky="nsew")
        for m in range(1, 13):
            tk.Label(months_frame, text=f"{m:02d}", bg="#252a34", fg="#ffffff", font=("Arial", 8, "bold"), width=8, bd=1, relief="solid").grid(row=0, column=m, sticky="nsew")

        # Éves adatok feltöltése a terved alapján (°C / °F párok)
        for z_idx, zone in enumerate(self.zones, start=1):
            bg_c = "#2d2d2d" if z_idx % 2 == 0 else "#252a34"
            tk.Label(months_frame, text=zone, bg=bg_c, fg="#ffffff", font=("Arial", 8, "bold"), bd=1, relief="solid", anchor="w", padx=4).grid(row=z_idx, column=0, sticky="nsew", ipady=3)
            
            for m in range(1, 13):
                demo_c = 22.4 if m in [6,7,8] else 18.5
                demo_f = self.c_to_f(demo_c)
                cell_text = f"{demo_c}°C\n{demo_f}°F"
                tk.Label(months_frame, text=cell_text, bg=bg_c, fg="#aaaaaa", font=("Arial", 7), bd=1, relief="solid").grid(row=z_idx, column=m, sticky="nsew")

        # 5. AKCIÓ GOMB: ELLENŐRZÉS FUTTATÁSA
        self.btn_check = tk.Button(self.root, text="💾  ADATOK MENTÉSE ÉS ELLENŐRZÉS / SAVE & CHECK DATA / SPEICHERN & PRÜFEN", 
                                   bg="#00adb5", fg="#ffffff", activebackground="#007a82", activeforeground="#ffffff",
                                   font=("Arial", 11, "bold"), bd=0, relief="flat", height=2, command=self.run_logic_check)
        self.btn_check.pack(fill="x", padx=15, pady=10)

    def run_logic_check(self):
        """A háttérben futó automata döntési motor kódja"""
        try:
            min_limit = float(self.min_c_entry.get())
            max_limit = float(self.max_c_entry.get())
        except ValueError:
            messagebox.showerror("Hiba / Error", "A megadott határértékek formátuma hibás!\nInvalid threshold limit format!")
            return

        alert_triggered = False
        triggered_type = ""
        triggered_val = 0.0
        triggered_zone = ""

        # Végigmegyünk az összes beírt cellán, üres értékeket kihagyva (nincs cellahiba!)
        for hour in self.hours:
            for zone in self.zones:
                raw_val = self.matrix_cells[hour][zone].get()
                if raw_val.strip() != "":
                    try:
                        val = float(raw_val)
                        if val > max_limit:
                            alert_triggered = True
                            triggered_type = "MAX"
                            triggered_val = val
                            triggered_zone = zone
                        elif val < min_limit:
                            alert_triggered = True
                            triggered_type = "MIN"
                            triggered_val = val
                            triggered_zone = zone
                    except ValueError:
                        pass 

        # Állapotjelző lámpa frissítése és szimulált 3 nyelvű e-mail sablon indítása
        if alert_triggered:
            self.status_lamp.config(text="🔴 RIASZTÁS AKTÍV / ALERT ACTIVE / ALARM AKTIV", bg="#ff2e63")
            
            raw_emails = self.email_entry.get().replace(",", ";")
            email_list = [e.strip() for e in raw_emails.split(";") if e.strip()]
            
            if triggered_type == "MAX":
                subject = "🚨 INDUSTRIAL HEAT ALERT / HŐSÉGRIADÓ"
                msg = (
                    f"Riasztási esemény történt a következő helyen: {triggered_zone}!\n"
                    f"Mért érték: {triggered_val}°C ({self.c_to_f(triggered_val)}°F) [Limit: {max_limit}°C]\n\n"
                    "HU: Figyelem! A hőfok elérte a riasztási maximum értéket, a riasztás visszavonásig érvényes.\n"
                    "EN: Warning: the temperature has reached the alarm maximum value, the alarm is valid until canceled.\n"
                    "DE: Warnung: Die Temperatur hat den maximalen Alarmwert erreicht. Der Alarm bleibt bis zur Deaktivierung aktiv."
                )
            else:
                subject = "❄️ INDUSTRIAL COLD ALERT / MINIMUM RIASZTÁS"
                msg = (
                    f"Riasztási esemény történt a következő helyen: {triggered_zone}!\n"
                    f"Mért érték: {triggered_val}°C ({self.c_to_f(triggered_val)}°F) [Limit: {min_limit}°C]\n\n"
                    "HU: Figyelem! A hőfok elérte a riasztási minimum értéket, a riasztás visszavonásig érvényes.\n"
                    "EN: Warning: the temperature has reached the alarm minimum value, the alarm is valid until cancelled.\n"
                    "DE: Warnung: Die Temperatur hat den Alarmminimumwert erreicht. Der Alarm bleibt bis zur Deaktivierung aktiv."
                )
                
            messagebox.showwarning(subject, f"Szimulált SMTP küldés indítása a következő címekre:\n{email_list}\n\nLevéltörzs:\n{msg}")
        else:
            self.status_lamp.config(text="🟢 MINDEN OKÉ / STATUS OK / ALLES REGLER", bg="#21bf73")
            messagebox.showinfo("Mentés / Safe OK", "Adatok rögzítve. Minden zóna az előírt klímatartományon belül van.\nData logged. Status: OK.")

if __name__ == "__main__":
    root = tk.Tk()
    app = IndustrialClimateDashboard(root)
    root.mainloop()
