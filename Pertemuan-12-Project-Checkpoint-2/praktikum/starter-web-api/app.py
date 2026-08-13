from flask import Flask,jsonify,render_template,request
import json
from pathlib import Path

app=Flask(__name__)
plans=[{"id":1,"title":"Belajar API","status":"todo"}]

def err(code,msg,status): return jsonify({"error":{"code":code,"message":msg}}),status

def mock_external():
    path=Path(__file__).parent/"mock_external.json"
    return json.loads(path.read_text(encoding="utf-8"))

@app.get("/")
def home(): return render_template("home.html")
@app.get("/plans")
def plans_page(): return render_template("plans.html",plans=plans)
@app.get("/external")
def external_page(): return render_template("external.html",data=mock_external())
@app.get("/api/health")
def health(): return jsonify({"status":"ok"})
@app.get("/api/plans")
def list_plans(): return jsonify({"data":plans})
@app.post("/api/plans")
def create_plan():
    p=request.get_json(silent=True) or {}; title=str(p.get("title","")).strip()
    if not title: return err("VALIDATION_ERROR","title wajib diisi",400)
    item={"id":max((x["id"] for x in plans),default=0)+1,"title":title,"status":"todo"}; plans.append(item); return jsonify(item),201
@app.delete("/api/plans/<int:pid>")
def delete_plan(pid):
    item=next((x for x in plans if x["id"]==pid),None)
    if not item: return err("NOT_FOUND","plan tidak ditemukan",404)
    plans.remove(item); return "",204

if __name__=="__main__": app.run(debug=True)
