package main

import (
  "net/http"
  "net/http/httptest"
  "os"
  "testing"

  "github.com/gin-gonic/gin"
)

var tmpArticleList []article

func testmain(m *testing.M) {
    
    gin.SetMode(gin.TestMode)

    os.Exit(m.Run())


}

func getRouter(withTemplates bool) *gin.Engine {
  r := gin.Default()
  if withTemplates {
    r.LoadHTMLGlob("templates/*")
  }
  return r
}


func testHTTPResponse(t *testing.T, r *gin.Engine, req *http.Request, f func(w *httptest.ResponseRecorder) bool) {

  // Create a response recorder
  w := httptest.NewRecorder()

  // Create the service and process the above request.
  r.ServeHTTP(w, req)

  if !f(w) {
    t.Fail()
  }
}

func saveLists() {
  tmpArticleList = articleList
}

func restoreLists() {
  articleList = tmpArticleList
}
