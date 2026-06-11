import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import sqlite3
import smtplib
from email.mime.text import MIMEText
import win32com.client as win32 # Outlook-hoz
from datetime import datetime, timedelta

DB = 'climate_data.db'
emails = []
email_config = {'mode': 'outlook', 'gmail_user': '', 'gmail_pass': ''}

class Dashboard:
    def __init__(self, root):
        self.root = root
        root.title("Industrial Climate Alert Dashboard v3.0 EXE")
        root.geometry("1400x700")
        root.configure(bg="#1e1e2f")

        self.unit = 'C'
        self.zones = 5
        self.hours = 24
        self.thresholds = {}
        self.today = datetime.now().strftime("%Y-%m-%d")

        self.init_db()
        self.load_thresholds()
        self.load_emails()

        self.create_ui()
        self.render_table()
        self.update_stats()

    def init_db(self):
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS data
                     (date TEXT, zone INTEGER, hour INTEGER, value REAL)''')
        c.execute('''CREATE TABLE IF NOT EXISTS thresholds
                     (zone INTEGER, min REAL, max REAL)''')
        c.execute('''CREATE TABLE IF NOT EXISTS emails (email TEXT)''')
        conn.commit()
        conn.close()

    def create_ui(self):
        # Felső gombok
        top = tk.Frame(self.root, bg="#1e1e2f")
        top.pack(pady=10)

        tk.Button(top, text="C/F", commandAha, most értem kincsem! 😄

Te nem weboldalt akarsz, hanem vissza a gyökerekhez: **EXE program** mint az eredeti Tkinter táblázatodnál. Ott volt Outlook/Gmail küldés beépítve, nem kellett EmailJS meg böngésző.

Igazad van, az sokkal stabilabb multi-userre. Mindenki letölti az EXE-t, elindítja, beírja a saját Gmail/Outlook adatát, és kész. Nincs szerver, nincs regisztráció.

**Csináljuk v3.2 DESKTOP PRO verziót:**

### **Mit tud az EXE:**
1. **Tkinter GUI** - ugyanaz a 5 zóna x 24 óra táblázat
2. **Min/Max küszöb** zónánként + kék/piros színezés
3. **Heti/Havi stat** SQLite-ba mentve, nem vész el
4. **Outlook vagy Gmail** küldés - ahogy az eredetinél volt
5. **Beállítások ablak** - SMTP szerver, port, jelszó mentve
6. **PyInstaller** - 1 db `Dashboard.exe` fájl lesz belőle

### **Kód - másold `dashboard_pro.py` néven:**

```python
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import sqlite3
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta
import win32com.client as win32 # Outlookhoz

DB = 'climate_data.db'
EMAIL_CONFIG = {}

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Industrial Climate Alert Dashboard v3.2 PRO - EXE")
        self.root.geometry("1400x800")
        self.unit = 'C'
        self.zones = 5
        self.hours = 24
        self.thresholds = {z: {'min': 10, 'max': 40} for z in range(1, 6)}
        self.init_db()
        self.load_thresholds()
        self.load_emails()
        self.create_gui()
        self.check_alerts_job()

    def init_db(self):
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS data
                     (date TEXT, zone INTEGER, hour INTEGER, value REAL)''')
        c.execute('''CREATE TABLE IF NOT EXISTS thresholds
                     (zone INTEGER PRIMARY KEY, min REAL, max REAL)''')
        c.execute('''CREATE TABLE IF NOT EXISTS emails
                     (email TEXT PRIMARY KEY)''')
        c.execute('''CREATE TABLE IF NOT EXISTS email_config
                     (id INTEGER PRIMARY KEY, type TEXT, email TEXT, pass TEXT, smtp TEXT, port INTEGER)''')
        conn.commit()
        conn.close()

    def load_thresholds(self):
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("SELECT zone, min, max FROM thresholds")
        for z, mn, mx in c.fetchall():
            self.thresholds[z] = {'min': mn, 'max': mx}
        conn.close()

    def save_thresholds(self):
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        for z, t in self.thresholds.items():
            c.execute("REPLACE INTO thresholds VALUES (?,?,?)", (z, t['min'], t['max']))
        conn.commit()
        conn.close()

    def load_emails(self):
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("SELECT email FROM emails")
        self.emails = [r[0] for r in c.fetchall()]
        c.execute("SELECT type, email, pass, smtp, port FROM email_config WHERE id=1")
        row = c.fetchone()
        if row:
            EMAIL_CONFIG.update({'type': row[0], 'email': row[1], 'pass': row[2], 'smtp': row[3], 'port': row[4]})
        conn.close()

    def create_gui(self):
        # Felső menü
        top = tk.Frame(self.root, bg='#1e1e2
