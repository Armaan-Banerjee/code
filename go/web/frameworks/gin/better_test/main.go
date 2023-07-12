package main

import (
  "net/http"

  "github.com/gin-gonic/gin"
)


var router *gin.Engine

func main() {
    
    router := gin.Default()

    router.LoadHTMLGlob("templates/*")

    router.GET("/", showIndexPage)

    router.Run(":8432")
}
