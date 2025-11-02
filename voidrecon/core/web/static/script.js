const API_BASE = "/api";

const workspaceSelect = document.getElementById("workspace-select");
const tablesList = document.getElementById("tables");
const tableWrapper = document.getElementById("table-wrapper");
const loader = document.getElementById("loader");
const exportBtn = document.getElementById("export-csv");
const refreshBtn = document.getElementById("refresh-workspaces");
const mainTitle = document.getElementById("main-title");


let currentWorkspace = null;
let currentTable = null;
let currentTableData = [];

// Loader
function showLoader(yes) {
  loader.classList.toggle("hidden", !yes);
  tableWrapper.classList.toggle("hidden", yes);
}

// Load workspaces
async function loadWorkspaces() {
  try {
    const res = await fetch(`${API_BASE}/workspaces`);
    const workspaces = await res.json();

    workspaceSelect.innerHTML = "";
    workspaces.forEach(ws => {
      const opt = document.createElement("option");
      opt.value = ws;
      opt.textContent = ws;
      workspaceSelect.appendChild(opt);
    });

    if (workspaces.length > 0) {
      currentWorkspace = workspaces[0];
      workspaceSelect.value = currentWorkspace;
      mainTitle.textContent = `${currentWorkspace}`;
      tableWrapper.innerHTML = "<p>Select a table to view data</p>";
      loadTables(currentWorkspace);
    }
  } catch (err) {
    console.error(err);
  }
}

// Load tables
async function loadTables(workspace) {
  if (!workspace) return;

  showLoader(true);
  tablesList.innerHTML = "";
  tableWrapper.innerHTML = "<p>Select a table to view data</p>";
  mainTitle.textContent = `${workspace}`;

  try {
    const res = await fetch(`${API_BASE}/workspace/${workspace}/tables`);
    const tables = await res.json();

    tables.forEach(t => {
      const li = document.createElement("li");
      li.textContent = t;
      li.addEventListener("click", () => {
        [...tablesList.children].forEach(c => c.classList.remove("active"));
        li.classList.add("active");
        loadTableData(workspace, t);
      });
      tablesList.appendChild(li);
    });
  } catch (err) {
    console.error(err);
  } finally {
    showLoader(false);
  }
}


// Load table data
async function loadTableData(workspace, table) {
  if (!workspace || !table) return;

  currentWorkspace = workspace;
  currentTable = table;
  mainTitle.textContent = `${workspace} — ${table}`;

  showLoader(true);
  try {
    const res = await fetch(`${API_BASE}/workspace/${workspace}/table/${table}`);
    const data = await res.json();
    currentTableData = data;
    renderTable(data);
    exportBtn.disabled = false;
  } catch (err) {
    console.error(err);
    tableWrapper.innerHTML = "<p>Error loading table data</p>";
    exportBtn.disabled = true;
  } finally {
    showLoader(false);
  }
}

// Render table
function renderTable(rows) {
  if (!rows || rows.length === 0) {
    tableWrapper.innerHTML = "<p>No data available</p>";
    return;
  }

  const table = document.createElement("table");
  table.classList.add("table");

  // Use field names from first row as headers
  const cols = Object.keys(rows[0]);
  const thead = document.createElement("thead");
  const trHead = document.createElement("tr");
  cols.forEach(colName => {
    const th = document.createElement("th");
    th.textContent = colName;  // FIELD NAME, not index
    trHead.appendChild(th);
  });
  thead.appendChild(trHead);
  table.appendChild(thead);

  // Table body
  const tbody = document.createElement("tbody");
  rows.forEach(r => {
    const tr = document.createElement("tr");
    cols.forEach(c => {
      const td = document.createElement("td");
      let v = r[c];
      if (Array.isArray(v)) {
        td.textContent = v.join(", ");
      } else if (typeof v === "object" && v !== null) {
        td.textContent = JSON.stringify(v);
      } else {
        td.textContent = v ?? "";
      }
      tr.appendChild(td);
    });
    tbody.appendChild(tr);
  });
  table.appendChild(tbody);

  tableWrapper.innerHTML = "";
  tableWrapper.appendChild(table);
}


// Export CSV
exportBtn.addEventListener("click", () => {
  if (!currentTableData || currentTableData.length === 0) return;

  const cols = Object.keys(currentTableData[0]);
  const lines = [cols.join(",")];

  currentTableData.forEach(r => {
    const row = cols.map(c => `"${String(r[c] ?? "").replace(/"/g, '""')}"`);
    lines.push(row.join(","));
  });

  const blob = new Blob([lines.join("\n")], { type: "text/csv" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `${currentWorkspace}_${currentTable}.csv`;
  a.click();
  URL.revokeObjectURL(url);
});

// Fix: handle workspace change event
workspaceSelect.addEventListener("change", (e) => {
  currentWorkspace = e.target.value;
  mainTitle.textContent = `${currentWorkspace}`;
  tablesList.innerHTML = "";
  tableWrapper.innerHTML = "<p>Select a table to view data</p>";
  loadTables(currentWorkspace);
});

// Refresh workspaces
refreshBtn.addEventListener("click", loadWorkspaces);

// Initialize
loadWorkspaces();
