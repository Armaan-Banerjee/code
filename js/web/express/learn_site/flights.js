const express = require('express')
const router = express.Router()

router.get("/:from-:to", (req, res) => {
    res.send(req.params)
})

module.exports = router