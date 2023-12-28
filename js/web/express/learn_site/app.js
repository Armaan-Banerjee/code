const express = require('express')
const app = express()
const port = 3002
const flights = require("./flights")
const logger = require("./logger")

app.use("/flights", flights)
app.use(logger)

app.get('/', (req, res) => {
  res.send('Hello World!')
})


app.listen(port, () => {
  console.log(`Started on  127.0.0.1:${port}`)
})