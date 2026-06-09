# 📊 Industrial Climate Alert Dashboard v1 (HU / EN / DE)

An autonomous, multi-language, 5-zone climate monitoring and automated notification software designed for industrial and corporate enterprise environments. 

### 🧬 // Evolúció (Evolution)
This project represents the digital evolution of traditional, cell-restricted, error-prone spreadsheet templates. By replacing legacy Excel sheets and hard-coded macros, this standalone system eliminates data calculation errors, bypasses local application dependencies, and introduces a modern, centralized data architecture.

---

## 🌍 Product Descriptions / Termékleírások / Produktbeschreibungen

### 🇭🇺 Kisvállalkozásoknak (HU)
Szabaduljon meg a kaotikus és instabil táblázatoktól! Ez a könnyű, önálló asztali alkalmazás automatikus e-mail riasztást küld, ha a raktár, műhely vagy hűtőkamra hőmérséklete kritikus (minimum vagy maximum) szintet ér el. Megbízható védelmet nyújt az árunak, az eszközöknek és a munkatársaknak, felesleges szoftveres előfizetések és bonyolult IT-infrastruktúra nélkül.

### 🇬🇧 For Enterprises & Corporations (EN)
A robust, 3-language, 5-zone industrial monitoring dashboard tailored for enterprise networks. Built to bridge the gap between shop-floor operations and upper management, the system features seamless Outlook (internal corporate network) and Gmail (external/private) server integration. It automates Celsius-to-Fahrenheit conversions and provides clean, LinkedIn-style monthly and weekly analytics for executive oversight.

### 🇩🇪 Für Unternehmen & Großbetriebe (DE)
Verabschieden Sie sich von unübersichtlichen Tabellenkalkulationen. Dieses eigenständige, dreisprachige Industrie-Dashboard überwacht bis zu 5 separate Zonen parallel. Das System integriert sich vollautomatisch in Outlook- und Gmail-Netzwerke, um das Management in Echtzeit über Grenzwertüberschreitungen zu informieren. Es bietet präzise Celsius-Fahrenheit-Doppelanalysen und übersichtliche monatliche Berichte im LinkedIn-Stil für die Geschäftsführung.

---

## 🎨 Core Features & Logic / Főbb Funkciók

### 1. Unified Multi-Language UI (HU/EN/DE)
To ensure absolute compliance in multinational corporate environments, the user interface displays all operational metadata in three languages simultaneously (Hungarian, English, and German), requiring zero external API dependencies or language switching.

### 2. Dual-Threshold Alarm System & Virtual Indicators
*   **Minimum Limit Control:** Monitors freezing or low-temperature thresholds to protect temperature-sensitive assets.
*   **Maximum Limit Control:** Configured for high-temperature/heat-wave protocols (optimized for industrial standard threshold configurations).
*   **Dynamic Conversion:** Real-time conversion between Celsius and Fahrenheit using the exact thermodynamic conversion formula on the interface.

### 3. Infinite Email Matrix (Hibrid SMTP Engine)
The interface features an unrestrictive, infinite multi-recipient entry field. It parses token-separated email addresses (supporting both `;` and `,`) to stream automated multi-language emergency notifications to:
*   **Internal Corporate Networks:** Via secure enterprise Microsoft Outlook / Exchange SMTP relays.
*   **External Encrypted Networks:** Via secure TLS/SSL SMTP pathways to private Gmail accounts for off-site executive monitoring.

### 4. LinkedIn-Style Executive Analytics Dashboard
*   **24-Hour Operational Matrix:** A clean, 5-zone matrix accepting hourly climate inputs without displaying calculation errors for missing data.
*   **Executive Toggle:** Dropdown selection for real-time Weekly and Monthly structural analytics.
*   **Annual Data Breakdown:** A continuous, 12-month aggregated dashboard tracking dual-unit (°C / °F) monthly averages per zone.

---

## 💻 Tech Stack & Deployment
*   **Core Architecture:** Python 3 / Standalone Executable (`.exe`) for local machine independence.
*   **UI Framework:** CustomTkinter / Modern GUI with high-contrast active alarm states.
*   **Data Structure:** Lightweight JSON-based local caching (`locales.json`, `mail_templates.json`).
*   **Mobile Synchronization:** Deployable as a dedicated Android `.apk` package, designed to poll live status and configuration arrays directly from this GitHub repository.

---
*Developed under the Cs-Aion Laboratory Framework.*ó
