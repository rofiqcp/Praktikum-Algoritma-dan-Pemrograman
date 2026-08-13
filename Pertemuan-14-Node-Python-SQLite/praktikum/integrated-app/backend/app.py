import sqlite3
from pathlib import Path
from flask import Flask,jsonify,request
DB_PATH=Path(__file__).with_name('app.db'); app=Flask(__name__)
@app.after_request
def cors(r):
    r.headers['Access-Control-Allow-Origin']='http://localhost:3000'; r.headers['Access-Control-Allow-Headers']='Content-Type'; r.headers['Access-Control-Allow-Methods']='GET,POST,PATCH,DELETE,OPTIONS'; return r
def db():
    c=sqlite3.connect(DB_PATH); c.row_factory=sqlite3.Row; return c
def init_db():
    with db() as c: c.execute('CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT NOT NULL,done INTEGER NOT NULL DEFAULT 0 CHECK(done IN(0,1)))'); c.commit()
@app.get('/api/tasks')
def list_tasks():
    with db() as c: rows=c.execute('SELECT id,title,done FROM tasks ORDER BY id').fetchall()
    return jsonify({'data':[dict(x) for x in rows]})
@app.post('/api/tasks')
def create():
    b=request.get_json(silent=True) or {}; title=str(b.get('title','')).strip()
    if not title: return jsonify({'error':'title wajib'}),400
    with db() as c: cur=c.execute('INSERT INTO tasks(title) VALUES(?)',(title,)); c.commit(); i=cur.lastrowid
    return jsonify({'id':i,'title':title,'done':0}),201
@app.patch('/api/tasks/<int:i>')
def patch(i):
    b=request.get_json(silent=True) or {}
    if not isinstance(b.get('done'),bool): return jsonify({'error':'done harus boolean'}),400
    with db() as c: cur=c.execute('UPDATE tasks SET done=? WHERE id=?',(int(b['done']),i)); c.commit()
    return (jsonify({'id':i,'done':int(b['done'])}),200) if cur.rowcount else (jsonify({'error':'not_found'}),404)
@app.delete('/api/tasks/<int:i>')
def delete(i):
    with db() as c: cur=c.execute('DELETE FROM tasks WHERE id=?',(i,)); c.commit()
    return ('',204) if cur.rowcount else (jsonify({'error':'not_found'}),404)
if __name__=='__main__': init_db(); app.run(port=5000,debug=True)
