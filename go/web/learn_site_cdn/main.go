package main

import (
    "net/http"

    "github.com/gin-gonic/gin"

    "fmt"

    "strings"

    "github.com/google/uuid"

    "os"

    "path/filepath"
)

var router *gin.Engine


func ApiIndex(c *gin.Context){
    c.JSON(http.StatusOK, gin.H{
        "message" : "welcome",
    })
}


func FileUploadView(c * gin.Context){
    form, _ := c.MultipartForm()
    files := form.File["upload[]"]
   
    currentDir, err := os.Getwd()
	if err != nil {
		fmt.Println("Error getting directory:", err)
		return
	}

    dst := currentDir + "/uploads"
    // fmt.Println(dst)

    for _, file := range files {
        prev_name := file.Filename
        
        uuid := (uuid.New()).String()
        extensionParts := strings.Split(prev_name, ".")
        if len(extensionParts) < 2 {
            fmt.Println("File has no extension:", prev_name)
            return
        }
        extension := extensionParts[len(extensionParts) - 1]

        final_name := uuid + "." + string(extension)
        file.Filename = final_name

        dst := dst + "/" + file.Filename

        err := c.SaveUploadedFile(file, dst)
        if err != nil {
            fmt.Println("Error uploading file", err)
        }

        //fmt.Printf("Uploading file: %s, with name:  %s", prev_name, final_name)
        
        c.JSON(http.StatusOK, gin.H{
            "image": final_name, 
        })
    }

}

func search_files(file_id string) (bool, string){
    pattern := filepath.Join("./uploads", file_id+".*")

    matches, err := filepath.Glob(pattern)
	if err != nil {
		fmt.Println("Error:", err)
		return false, ""
	}

	if len(matches) > 0 {
		return true, matches[0] // Return the full path of the first matching file
	}

	return false, ""

}

func RetreiveFileView(c *gin.Context){
    //fileID := c.Param("fileid")
    fileID := c.Query("fileid")
    
    fmt.Println(fileID)
    exists, file := search_files(fileID)
    
    if exists {
        fmt.Println(file)
        c.File(file)
        return 
    }
    
    c.JSON(http.StatusBadRequest, gin.H{"error": "file not found"})
    

}

func main() {
    router = gin.Default()
    
    router.ForwardedByClientIP = true
    router.SetTrustedProxies([]string{"127.0.0.1"})

    router.MaxMultipartMemory = 8 << 20
    
    router.GET("/", ApiIndex)
    router.POST("/upload", FileUploadView)
    router.GET("/download", RetreiveFileView)

    router.Run("0.0.0.0:1155")
}

