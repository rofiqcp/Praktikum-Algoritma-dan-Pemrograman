> Diadaptasi langsung dari lampiran/panduan pada buku sumber Edisi Agustus 2026.

# Lampiran F — Node.js/Express Cheat Sheet

```bash
npm init -y
npm install express
node server.js
```

```javascript
const express=require('express');
const app=express();
app.use(express.json());
app.use(express.static('public'));
app.get('/api/health',(req,res)=>res.json({status:'ok'}));
app.listen(process.env.PORT||3000);
```
