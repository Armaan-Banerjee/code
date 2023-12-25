package main;

import "fmt"
import "time"

func pn(num string){
    fmt.Println(num)
}


func main_primitives(){
    go pn("1")
    go pn("2")
    go pn("3")

    time.Sleep(time.Second * 2)

    fmt.Println("hi")

}
