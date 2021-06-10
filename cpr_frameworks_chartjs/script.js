const port = 3000;
const express = require('express');
const app = express();

app.listen(port, () =>{
    console.log("Server läuft auf Port" + port);
})

app.use(express.static("public"));

app.get("./data", (req,res) => {

    res.send(JSON.stringify(3));
})

