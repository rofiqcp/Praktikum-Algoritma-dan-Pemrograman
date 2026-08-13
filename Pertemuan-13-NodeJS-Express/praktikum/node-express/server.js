const app=require('./app');
const port=Number(process.env.PORT||3000);
app.listen(port,()=>console.log(`Node server: http://127.0.0.1:${port}`));
