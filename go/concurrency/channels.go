package main

import "fmt"

func main_channels() {
    channel := make(chan string)

    go func(){
        channel <- "data" //in the lambda function, data enters the channel that can be read from the main function
    }()

    msg := <-channel // the main function can rean the data from the channel which the lamda function entered
    // main function will wait for the data from the channel

    fmt.Println(msg)
    
}
