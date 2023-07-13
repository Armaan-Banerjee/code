package main

import (

  "github.com/gin-gonic/gin"
)


var router *gin.Engine

func main() {
    
    router := gin.Default()

    router.LoadHTMLGlob("templates/*")

    router.GET("/", showIndexPage)
    
    router.GET("/article/view/:article_id", getArticle )

    router.Run(":8432")
}
