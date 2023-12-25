package main

import "fmt"

func main_selects() {
    channel := make(chan string)
    anotherchannel := make(chan string)

    go func(){
        channel <- "data" 
    }()

    go func(){
        anotherchannel <- "vodka"
    }()

    select { // will block untill it receives a message from a channel, only one message will be outputted. If multiple channels are ready at the same time, it will pick at random
        case MsgFromChannel := <- channel:
            fmt.Println(MsgFromChannel)

        case MsgFromAnotherchannel := <- anotherchannel:
            fmt.Println(MsgFromAnotherchannel)
    }
    
}
