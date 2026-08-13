const test = require('node:test');
const assert = require('node:assert/strict');
const request = require('supertest');
const app = require('../app');

test.beforeEach(() => app.resetItems());

test('status endpoint', async () => {
  const r = await request(app).get('/api/status');
  assert.equal(r.status, 200);
  assert.equal(r.body.status, 'ok');
  assert.equal(r.body.runtime, 'node');
});

test('initial collection', async () => {
  const r = await request(app).get('/api/items');
  assert.equal(r.status, 200);
  assert.equal(r.body.count, 2);
  assert.ok(Array.isArray(r.body.data));
});

test('invalid empty name', async () => {
  const r = await request(app).post('/api/items').send({ name: '' });
  assert.equal(r.status, 400);
  assert.equal(r.body.error.code, 'VALIDATION_ERROR');
});

test('whitespace name is invalid', async () => {
  const r = await request(app).post('/api/items').send({ name: '   ' });
  assert.equal(r.status, 400);
});

test('valid post creates item', async () => {
  const r = await request(app).post('/api/items').send({ name: 'Monitor' });
  assert.equal(r.status, 201);
  assert.equal(r.body.name, 'Monitor');
  const list = await request(app).get('/api/items');
  assert.equal(list.body.count, 3);
});

test('static index is served', async () => {
  const r = await request(app).get('/');
  assert.equal(r.status, 200);
  assert.match(r.headers['content-type'], /text\/html/);
});

test('unknown api endpoint returns JSON 404', async () => {
  const r = await request(app).get('/api/unknown');
  assert.equal(r.status, 404);
  assert.equal(r.body.error.code, 'NOT_FOUND');
});
