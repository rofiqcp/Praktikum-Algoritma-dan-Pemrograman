#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
run_py(){ echo "== PY: $1 =="; (cd "$ROOT/$1" && python ${2}); }
if [[ "${1:-all}" == "python" || "${1:-all}" == "all" ]]; then
  run_py "Pertemuan-05-List-Data-Statistik/praktikum" "-m unittest discover -s tests -v"
  run_py "Pertemuan-06-Function-Debugging/praktikum" "-m unittest discover -s tests -v"
  run_py "Pertemuan-07-VSCode-Git-GitHub/praktikum/python-local" "-m unittest discover -s tests -v"
  run_py "Pertemuan-08-Project-Checkpoint-1/praktikum/starter-cli" "-m unittest discover -s tests -v"
  run_py "Pertemuan-09-Python-Web-Flask/praktikum/flask-web" "-m unittest -v test_app.py"
  run_py "Pertemuan-10-Python-API-REST/praktikum/rest-api" "-m unittest -v test_api.py"
  run_py "Pertemuan-11-Deployment/praktikum/deploy-flask" "-m unittest -v test_app.py"
  run_py "Pertemuan-12-Project-Checkpoint-2/praktikum/starter-web-api" "-m unittest -v test_app.py"
  run_py "Pertemuan-14-Node-Python-SQLite/praktikum/integrated-app/backend" "-m unittest -v test_app.py"
  run_py "Pertemuan-15-Fullstack-Structured-Backend/praktikum/structured-app/backend" "-m unittest -v test_backend.py"
  run_py "Pertemuan-16-Final-Project/praktikum/final-starter/backend" "-m unittest -v test_app.py"
  run_py "Pertemuan-16-Final-Project/praktikum/final-starter/backend" "test_api.py"
fi
if [[ "${1:-all}" == "node" || "${1:-all}" == "all" ]]; then
  echo "== NODE: Pertemuan 13 =="
  (cd "$ROOT/Pertemuan-13-NodeJS-Express/praktikum/node-express" && npm install --no-audit --no-fund && npm test)
  for dir in \
    "Pertemuan-14-Node-Python-SQLite/praktikum/integrated-app/frontend" \
    "Pertemuan-15-Fullstack-Structured-Backend/praktikum/structured-app/frontend" \
    "Pertemuan-16-Final-Project/praktikum/final-starter/frontend"; do
    echo "== NODE INSTALL: $dir =="
    (cd "$ROOT/$dir" && npm install --no-audit --no-fund && node --check server.js && node --check public/app.js)
  done
fi
