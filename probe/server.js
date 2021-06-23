const port = 4000;
const express = require("express");
const app = express();
const fs = require("fs")

app.use(express.static("public"))
app.use(express.urlencoded({ extended: false }))

app.get("/receive", (req, res) => {
    fs.readFile("./data.csv", "utf-8", (err, data) => {
        if (err) throw err;
        res.send(data)
    })
})
app.post("/send", (req, res) => {

    fs.appendFile("./data.csv", '[' + JSON.stringify(req.body) + ']', (err) => {
        if (err) throw err;
    })
    res.send("hi")
})
app.listen(port, () => {
    console.log("port " + port)
})