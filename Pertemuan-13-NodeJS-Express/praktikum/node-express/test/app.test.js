const test=require('node:test');const assert=require('node:assert/strict');const request=require('supertest');const app=require('../app');
test('status 200',async()=>{const r=await request(app).get('/api/status');assert.equal(r.status,200);assert.equal(r.body.status,'ok');});
test('items',async()=>{const r=await request(app).get('/api/items');assert.equal(r.status,200);assert.ok(Array.isArray(r.body.data));});
test('invalid post',async()=>{const r=await request(app).post('/api/items').send({name:''});assert.equal(r.status,400);});
test('valid post',async()=>{const r=await request(app).post('/api/items').send({name:'Monitor'});assert.equal(r.status,201);});
