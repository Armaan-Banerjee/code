const logger = function (req, res, next) {
    const d = new Date()
    const time = d.getTime()
    console.log('logging')
    next()
}

module.exports = logger