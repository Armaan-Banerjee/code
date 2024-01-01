package main

import (
    "net/http"

    "github.com/gin-gonic/gin"

    "fmt"

    "strings"

    "errors"

    "github.com/google/uuid"

    "os"

    "path/filepath"

    "mime/multipart"
)

var router *gin.Engine


func ApiIndex(c *gin.Context){
    c.JSON(http.StatusOK, gin.H{
        "message" : "welcome",
    })
}

func CheckImage(image *string) (bool, error) {
    extension := strings.Split(*image, ".")
    if len(extension) < 2 {
        return false, errors.New("file has no extension")
    }

    ext := extension[len(extension) - 1]
    allowed_images := []string{"png", "jpg", "jpeg", "webp"}

    return Contains(allowed_images, ext), nil
}

func Contains(slics []string, val string) bool {

    for _ , ch := range slics {
        if ch == val {
            return true
        }
    } 

    return false
}

func uploadFile(c *gin.Context, file multipart.FileHeader, image bool) (*string, error){
    filename := file.Filename
    if image{
        res, err := CheckImage(&filename)
        if err != nil {
            return nil, err
        }
        if !res {
            return nil, errors.New("not valid file extension")
        }
    }

    uuid := (uuid.New()).String()

    fileparts := strings.Split(filename, ".")
    if len(fileparts) < 2 {
        return nil, errors.New("file has no extension")
    }

    extension := fileparts[len(fileparts) - 1]

    uploadname := uuid + "." + string(extension)
    file.Filename = uploadname

    currentDir, err := os.Getwd()
    if err != nil {
        return nil, errors.New("could not determine upload path")
    }

    dst := currentDir + "/uploads" + "/" + file.Filename

    errfile := c.SaveUploadedFile(&file, dst)
    if errfile != nil {
        return nil, errors.New("could not upload file")
    }

    return &uploadname, nil

}

func FileUploadView(c *gin.Context){
    form, _ := c.MultipartForm()
    files := form.File["upload[]"]
   
    // currentDir, err := os.Getwd()
	// if err != nil {
	// 	fmt.Println("Error getting directory:", err)
	// 	return
	// }

    //dst := currentDir + "/uploads"
    // fmt.Println(dst)

    var filenames = make([]string, 0, len(files))

    for _, file := range files {

        res, errf := uploadFile(c, *file, false)

        if errf != nil{
            fmt.Println("There was an error", errf)
        }
        // prev_name := file.Filename
        
        // uuid := (uuid.New()).String()
        // extensionParts := strings.Split(prev_name, ".")
        // if len(extensionParts) < 2 {
        //     fmt.Println("File has no extension:", prev_name)
        //     return
        // }
        // extension := extensionParts[len(extensionParts) - 1]

        // final_name := uuid + "." + string(extension)
        // file.Filename = final_name

        // dst := dst + "/" + file.Filename

        // errfile := c.SaveUploadedFile(file, dst)
        // if errfile != nil {
        //     fmt.Println("Error uploading file", errfile)
        // }

        filenames = append(filenames, *res)

        //fmt.Printf("Uploading file: %s, with name:  %s", prev_name, final_name)
        
     }

     c.JSON(http.StatusOK, gin.H{
         "images": filenames,
    })

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

