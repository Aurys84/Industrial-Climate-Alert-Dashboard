let unit = 'C';
let matrix = {};
const zones = 5;
const hours = 24;

function init() {
  load();
  render();
}

function render() {
  const tbody = document.getElementById('tbody');
  tbody.innerHTML = '';
  for (let z = 1; z <= zones; z++) {
    let row = `<tr><td class="zone-label">Zóna ${z}</td>`;
    for (let h = 0; h < hours; h++) {
      let val = matrix[z]?.[h] ?? '';
      let cls = (parseFloat(val) > 40 && unit==='C') || (parseFloat(val) > 104 && unit==='F') ? 'hot' : '';
      row += `<td><input type="number" step="0.1" value="${val}" onchange="saveCell(${z},${h},this.value)" class="${cls}"></td>`;
    }
    row += '</tr>';
    tbody.innerHTML += row;
  }
  updateStats();
}

function saveCell(z, h, val) {
  if (!matrix[z]) matrix[z] = {};
  matrix[z][h] = val;
  localStorage.setItem('matrix', JSON.stringify(matrix));
  render();
}

function switchUnit() {
  unit = unit==='C' ? 'F' : 'C';
  document.getElementById('unitBtn').innerText = unit;
  document.querySelectorAll('th').forEach((th,i)=>{ if(i>0) th.innerText = i-1 + ':00 ' + unit; });
  render();
}

function updateStats() {
  let html = '<h3>Statisztika</h3>';
  for (let z = 1; z <= zones; z++) {
    let vals = Object.values(matrix[z]||{}).map(Number).filter(v=>!isNaN(v));
    if (vals.length) {
      let max = Math.max(...vals).toFixed(1);
      let min = Math.min(...vals).toFixed(1);
      let avg = (vals.reduce((a,b)=>a+b,0)/vals.length).toFixed(1);
      html += `<p><b>Zóna ${z}:</b> Max ${max}°${unit} | Min ${min}°${unit} | Átlag ${avg}°${unit}</p>`;
    }
  }
  document.getElementById('stats').innerHTML = html;
}

function deleteDay() {
  if (confirm('Biztos törlöd a teljes napot?')) {
    matrix = {};
    localStorage.removeItem('matrix');
    render();
  }
}

function load() {
  matrix = JSON.parse(localStorage.getItem('matrix') || '{}');
}

init();
