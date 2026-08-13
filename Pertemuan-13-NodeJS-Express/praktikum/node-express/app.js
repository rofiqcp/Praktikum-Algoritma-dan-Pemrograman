const express = require('express');
const path = require('path');

const app = express();
const INITIAL_ITEMS = [
  { id: 1, name: 'Keyboard' },
  { id: 2, name: 'Mouse' },
];
let items = INITIAL_ITEMS.map(item => ({ ...item }));

function resetItems() {
  items = INITIAL_ITEMS.map(item => ({ ...item }));
}

app.use(express.json());
app.use((req, res, next) => {
  console.log(`${new Date().toISOString()} ${req.method} ${req.path}`);
  next();
});
app.use(express.static(path.join(__dirname, 'public')));

app.get('/api/status', (req, res) => {
  res.json({ status: 'ok', runtime: 'node' });
});

app.get('/api/items', (req, res) => {
  res.json({ data: items, count: items.length });
});

app.post('/api/items', (req, res) => {
  if (!req.body || typeof req.body !== 'object' || Array.isArray(req.body)) {
    return res.status(400).json({ error: { code: 'VALIDATION_ERROR', message: 'Body harus JSON object' } });
  }
  const name = String(req.body.name ?? '').trim();
  if (!name) {
    return res.status(400).json({ error: { code: 'VALIDATION_ERROR', message: 'name wajib diisi' } });
  }
  const item = { id: Math.max(0, ...items.map(x => x.id)) + 1, name };
  items.push(item);
  return res.status(201).json(item);
});

app.use('/api', (req, res) => {
  res.status(404).json({ error: { code: 'NOT_FOUND', message: 'endpoint tidak ditemukan' } });
});

app.resetItems = resetItems;
module.exports = app;
