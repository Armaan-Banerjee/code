package main

import (
    "net/http"

    "github.com/gin-gonic/gin"

    "fmt"
)

var router *gin.Engine

func ApiIndex(c *gin.Context){
    c.JSON(http.StatusOK, gin.H{
        "message" : "welcome",
    })
}

func main() {
    router = gin.Default()
    router.GET("/", ApiIndex)

    fmt.Println("Starting server on 0.0.0.0:1155")
    router.Run("0.0.0.0:1155")
}

