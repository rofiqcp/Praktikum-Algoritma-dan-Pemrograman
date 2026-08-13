const express=require('express');
const path=require('path');
const app=express();
const PORT=process.env.PORT||3000;
app.use(express.json());
app.use(express.static(path.join(__dirname,'public')));
app.get('/api/hello',(req,res)=>res.json({message:'Halo dari Node.js + Express',runtime:process.version}));
app.get('/health',(req,res)=>res.json({status:'ok'}));
app.listen(PORT,()=>console.log(`Server: http://localhost:${PORT}`));
