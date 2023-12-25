package main

import "fmt"
import "time"

func dowork(done <- chan bool){
    for {
        select{
        case <- done:
            return 
        default: 
            fmt.Println("hi")
        }
    }
}

func main_another_for_solect(){

    done := make(chan bool)

    go dowork(done)


    time.Sleep(time.Second * 3)

    close(done)
}
