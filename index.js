const hostname = '127.0.0.1'
const port = 3000
let express=require('express');
let app=express();
let server=require('http').createServer(app);
app.use(express.static('public'));

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`)
   })

app.get('/', function(request, respons){
    respons.sendFile(__dirname + '/index.html');
});

