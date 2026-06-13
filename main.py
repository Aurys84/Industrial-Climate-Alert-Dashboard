<!DOCTYPE html>
<html lang="hu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Klíma Dashboard</title>
    <style>
        body { background: #121212; color: #e0e0e0; font-family: Arial, sans-serif; padding: 15px; margin: 0; font-size: 16px; }
        h1 { color: #00e5ff; text-align: center; margin-bottom: 15px; }
        .controls { display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 15px; background: #1e1e1e; padding: 12px; border-radius: 8px; }
        .control-group { display: flex; align-items: center; gap: 8px; flex: 1; min-width: 120px; }
        select, button, input { padding: 10px; border-radius: 6px; border: 1px solid #444; background: #2c2c2c; color: #fff; font-size: 15px; }
        button { background: #00e5ff; color: #000; font-weight: bold; cursor: pointer; border: none; }
        button:hover { background: #00b8cc; }
        .btn-danger { background: #ff4081; color: white; }
        .btn-warning { background: #ffab40; color: #000; }
        .btn-save { background: #69f0ae; color: #000; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; background: #1e1e1e; border-radius: 8px; overflow: hidden; }
        th, td { border: 1px solid #333; padding: 12px; text-align: center; }
        th { background: #00e5ff; color: #000; font-weight: bold; }
        input[type="number"] { width: 70px; padding: 6px; text-align: center; background: #2c2c2c; color: #fff; border: 1px solid #555; border-radius: 4px; }
        .status { font-weight: bold; }
        .ok { color: #00e5ff; }
        .warn { color: #ff4081; animation: pulse 1.5s infinite; }
        @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.5; } }
        .panel { background: #1e1e1e; padding: 15px; border-radius: 8px; margin-top: 20px; }
        .panel h3 { color: #00e5ff; margin-top: 0; }
        .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 10px; margin-top: 10px; }
        .stat-box { background: #2c2c2c; padding: 10px; border-radius: 6px; text-align: center; }
        .stat-val { font-size: 1.4em; font-weight: bold; color: #00e5ff; }
        .stat-label { font-size: 0.8em; color: #aaa; }
        .msg { margin-top: 15px; text-align: center; font-weight: bold; min-height: 24px; padding: 10px; border-radius: 4px; display: none; }
        .msg.success { background: rgba(0, 229, 255, 0.1); color: #69f0ae; border: 1px solid #69f0ae; }
        .msg.error { background: rgba(255, 64, 129, 0.1); color: #ff4081; border: 1px solid #ff4081; }
    </style>
</head>
<body>

    <h1 id="title">Klíma Dashboard</h1>

    <div class="controls">
        <div class="control-group">
            <label id="lblLang">Nyelv:</label>
            <select id="lang" onchange="changeLang()">
                <option value="HU">Magyar</option>
                <option value="EN">English</option>
                <option value="DE">Deutsch</option>
            </select>
        </div>
        <div class="control-group">
            <label id="lblHour">Óra:</label>
            <select id="hour" onchange="changeHour()"></select>
        </div>
        <button onclick="saveAll()" class="btn-save" id="btnSave">💾 MENTÉS</button>
        <button onclick="deleteHour()" class="btn-danger" id="btnDel">🗑️ Törlés</button>
        <button onclick="sendEmail()" class="btn-warning" id="btnEmail">📧 KÜLDÉS</button>
    </div>

    <table>
        <thead>
            <tr>
                <th id="thZone">Zóna</th>
                <th id="thC">°C</th>
                <th id="thF">°F</th>
                <th id="thMin">Min</th>
                <th id="thMax">Max</th>
                <th id="thStatus">Állapot</th>
            </tr>
        </thead>
        <tbody id="tableBody"></tbody>
    </table>

    <div class="panel">
        <h3 id="stTitle">Statisztika</h3>
        <div class="stats-grid">
            <div class="stat-box"><div class="stat-val" id="stAvg">--</div><div class="stat-label" id="stAvgLbl">Átlag</div></div>
            <div class="stat-box"><div class="stat-val" id="stMax">--</div><div class="stat-label" id="stMaxLbl">Max</div></div>
            <div class="stat-box"><div class="stat-val" id="stMin">--</div><div class="stat-label" id="stMinLbl">Min</div></div>
        </div>
    </div>

    <div class="panel">
        <h3 id="thTitle">Küszöbértékek</h3>
        <div id="threshList"></div>
    </div>

    <div class="panel">
        <h3 id="emTitle">E-mail Címek</h3>
        <input type="text" id="emailInput" placeholder="pelda@pelda.hu, pelda2@pelda.hu" onchange="saveEmailList()">
        <div id="emailTags" style="margin-top: 10px;"></div>
    </div>

    <div id="msgBox" class="msg"></div>

    <script>
        // --- ÁLLANDÓ ADATOK ---
        const zones = ["Z1", "Z2", "Z3", "Z4", "Z5"];
        const hours = Array.from({length: 24}, (_, i) => `${i.toString().padStart(2, '0')}:00`);
        
        const dict = {
            "HU": { title: "Klíma Dashboard", lblLang: "Nyelv:", lblHour: "Óra:", btnSave: "💾 MENTÉS", btnDel: "🗑️ Törlés", btnEmail: "📧 KÜLDÉS", thZone: "Zóna", thC: "°C", thF: "°F", thMin: "Min", thMax: "Max", thStatus: "Állapot", stOk: "OK", stWarn: "RIASZTÁS!", stTitle: "Statisztika", stAvg: "Átlag", stMax: "Max", stMin: "Min", thTitle: "Küszöbértékek", emTitle: "E-mail Címek", msgSaved: "✓ Mentve!", msgSent: "✓ E-mail megnyitva!", msgDelOk: "✓ Törölve!", msgErr: "Hiba!" },
            "EN": { title: "Climate Dashboard", lblLang: "Language:", lblHour: "Hour:", btnSave: "💾 SAVE", btnDel: "🗑️ Delete", btnEmail: "📧 SEND", thZone: "Zone", thC: "°C", thF: "°F", thMin: "Min", thMax: "Max", thStatus: "Status", stOk: "OK", stWarn: "ALARM!", stTitle: "Statistics", stAvg: "Avg", stMax: "Max", stMin: "Min", thTitle: "Thresholds", emTitle: "Email Addresses", msgSaved: "✓ Saved!", msgSent: "✓ Email opened!", msgDelOk: "✓ Deleted!", msgErr: "Error!" },
            "DE": { title: "Klima Dashboard", lblLang: "Sprache:", lblHour: "Stunde:", btnSave: "💾 SPEICHERN", btnDel: "🗑️ Löschen", btnEmail: "📧 SENDEN", thZone: "Zone", thC: "°C", thF: "°F", thMin: "Min", thMax: "Max", thStatus: "Status", stOk: "OK", stWarn: "ALARMM!", stTitle: "Statistik", stAvg: "Durchschn.", stMax: "Max", stMin: "Min", thTitle: "Grenzwerte", emTitle: "E-Mail-Adressen", msgSaved: "✓ Gespeichert!", msgSent: "✓ E-Mail geöffnet!", msgDelOk: "✓ Gelöscht!", msgErr: "Fehler!" }
        };

        let lang = "HU";
        let currentHour = "00:00";
        let data = {};
        let thresh = {};
        let emailList = [];

        // --- INICIALIZÁLÁS ---
        function init() {
            // Adatok inicializálása
            hours.forEach(h => {
                data[h] = {};
                zones.forEach(z => { data[h] [z] = { c: "", f: "" }; });
            });
            zones.forEach(z => {
                thresh[z] = { min: 18, max: 28 };
            });

            // Selectek feltöltése
            const hSel = document.getElementById('hour');
            hours.forEach(h => {
                const opt = document.createElement('option');
                opt.value = h;
                opt.innerText = h;
                hSel.appendChild(opt);
            });

            // Első renderelés
            changeLang();
        }

        // --- NYELVVÁLTÁS ---
        function changeLang() {
            lang = document.getElementById('lang').value;
            const t = dict[lang];

            // Szövegek frissítése
            document.getElementById('title').innerText = t.title;
            document.getElementById('lblLang').innerText = t.lblLang;
            document.getElementById('lblHour').innerText = t.lblHour;
            document.getElementById('btnSave').innerText = t.btnSave;
            document.getElementById('btnDel').innerText = t.btnDel;
            document.getElementById('btnEmail').innerText = t.btnEmail;
            document.getElementById('thZone').innerText = t.thZone;
            document.getElementById('thC').innerText = t.thC;
            document.getElementById('thF').innerText = t.thF;
            document.getElementById('thMin').innerText = t.thMin;
            document.getElementById('thMax').innerText = t.thMax;
            document.getElementById('thStatus').innerText = t.thStatus;
            document.getElementById('stTitle').innerText = t.stTitle;
            document.getElementById('stAvgLbl').innerText = t.stAvg;
            document.getElementById('stMaxLbl').innerText = t.stMax;
            document.getElementById('stMinLbl').innerText = t.stMin;
            document.getElementById('thTitle').innerText = t.thTitle;
            document.getElementById('emTitle').innerText = t.emTitle;

            // Táblázat frissítése
            renderTable();
            updateStats();
        }

        // --- ÓRA VÁLTÁS ---
        function changeHour() {
            currentHour = document.getElementById('hour').value;
            renderTable();
            updateStats();
        }

        // --- TÁBLÁZAT MEGJELENÍTÉS ---
        function renderTable() {
            const tbody = document.getElementById('tableBody');
            tbody.innerHTML = "";
            const t = dict[lang];

            zones.forEach(z => {
                const val = data[currentHour] [z];
                const th = thresh[z];
                const cVal = val.c || "";
                const fVal = val.f || "";

                let status = t.stOk;
                let cls = "ok";
                if (cVal !== "") {
                    const num = parseFloat(cVal);
                    if (!isNaN(num) && (num < th.min || num > th.max)) { 
                        status = t.stWarn; 
                        cls = "warn"; 
                    }
                }

                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${z}</td>
                    <td><input type="number" value="${cVal}" oninput="updateVal('${z}', 'c', this.value)"></td>
                    <td><input type="number" value="${fVal}" oninput="updateVal('${z}', 'f', this.value)"></td>
                    <td><input type="number" value="${th.min}" onchange="updateThresh('${z}', 'min', this.value)"></td>
                    <td><input type="number" value="${th.max}" onchange="updateThresh('${z}', 'max', this.value)"></td>
                    <td class="status ${cls}">${status}</td>
                `;
                tbody.appendChild(row);
            });
        }

        // --- ÉRTÉK FRISSÍTÉS ---
        function updateVal(z, type, val) {
            data[currentHour] [z] [type] = val;
            
            // °C -> °F vagy °F -> °C konverzió
            if (type === 'c' && val !== "") {
                const c = parseFloat(val);
                if (!isNaN(c)) {
                    data[currentHour] [z].f = (c * 9/5 + 32).toFixed(1);
                }
            } else if (type === 'f' && val !== "") {
                const f = parseFloat(val);
                if (!isNaN(f)) {
                    data[currentHour] [z].c = ((f - 32) * 5/9).toFixed(1);
                }
            }

            renderTable();
            updateStats();
        }

        // --- KÜSZÖBÉRTÉK FRISSÍTÉS ---
        function updateThresh(z, type, val) {
            thresh[z] [type] = parseFloat(val) || 0;
            renderTable();
            updateStats();
        }

        // --- STATISZTIKA ---
        function updateStats() {
            let sum = 0, count = 0, maxV = -999, minV = 999;

            zones.forEach(z => {
                const cVal = data[currentHour] [z].c;
                if (cVal !== "") {
                    const num = parseFloat(cVal);
                    if (!isNaN(num)) {
                        sum += num;
                        count++;
                        if (num > maxV) maxV = num;
                        if (num < minV) minV = num;
                    }
                }
            });

            const t = dict[lang];
            if (count > 0) {
                document.getElementById('stAvg').
