from flask import Flask, jsonify, render_template, request
from external_client import fetch_external

app = Flask(__name__)

INITIAL_PLANS = [{"id": 1, "title": "Belajar API", "status": "todo"}]
plans = [item.copy() for item in INITIAL_PLANS]


def reset_plans():
    plans.clear()
    plans.extend(item.copy() for item in INITIAL_PLANS)


def api_error(code, message, status):
    return jsonify({"error": {"code": code, "message": message}}), status


def find_plan(plan_id):
    return next((item for item in plans if item["id"] == plan_id), None)


@app.get("/")
def home():
    return render_template("home.html")


@app.get("/plans")
def plans_page():
    return render_template("plans.html", plans=plans)


@app.get("/external")
def external_page():
    mode = request.args.get("mode", "success")
    result = fetch_external(mode)
    return render_template("external.html", result=result, mode=mode, data=result["data"])


@app.get("/api/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/api/plans")
def list_plans():
    return jsonify({"data": plans, "count": len(plans)})


@app.get("/api/plans/<int:plan_id>")
def get_plan(plan_id):
    item = find_plan(plan_id)
    return jsonify(item) if item else api_error("NOT_FOUND", "Plan tidak ditemukan", 404)


@app.post("/api/plans")
def create_plan():
    payload = request.get_json(silent=True) or {}
    title = str(payload.get("title", "")).strip()
    if not title:
        return api_error("VALIDATION_ERROR", "title wajib diisi", 400)
    item = {"id": max((x["id"] for x in plans), default=0) + 1, "title": title, "status": "todo"}
    plans.append(item)
    return jsonify(item), 201


@app.patch("/api/plans/<int:plan_id>")
def update_plan(plan_id):
    item = find_plan(plan_id)
    if item is None:
        return api_error("NOT_FOUND", "Plan tidak ditemukan", 404)
    payload = request.get_json(silent=True) or {}
    if "status" not in payload:
        return api_error("VALIDATION_ERROR", "status wajib dikirim", 400)
    if payload["status"] not in {"todo", "doing", "done"}:
        return api_error("VALIDATION_ERROR", "status tidak dikenal", 400)
    item["status"] = payload["status"]
    return jsonify(item)


@app.delete("/api/plans/<int:plan_id>")
def delete_plan(plan_id):
    item = find_plan(plan_id)
    if item is None:
        return api_error("NOT_FOUND", "Plan tidak ditemukan", 404)
    plans.remove(item)
    return "", 204


@app.get("/api/external-preview")
def external_preview():
    mode = request.args.get("mode", "success")
    result = fetch_external(mode)
    status = 200 if result["state"] in {"success", "empty"} else 503
    return jsonify(result), status


if __name__ == "__main__":
    app.run(debug=True)
