const port = 3000;
const express = require("express");
const app = express();
const fs = require("fs")
let newData;
let arr = new Array()
app.use(express.static("public"))
app.use(express.urlencoded({ extended: false }))

app.get("/receive", (req, res) => {
    newData = arr[arr.length - 1]
    res.send(JSON.stringify(newData))
})
app.post("/send", (req, res) => {

    arr.push(req.body)

    res.send(req.body)
})
app.listen(port, () => {
    console.log("port " + port)
})