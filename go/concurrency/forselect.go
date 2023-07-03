package main

import "fmt"

func main(){
    charChannel := make(chan string, 3) //makes a buffered channel which allows for asynchronous operation nad go rountine can continue without being blocked

    chars := []string{"a", "b", "c"}

    for _, s := range chars {
        select{
        case charChannel <- s:

        }
    }
    
    close(charChannel)

    for result := range charChannel{
        fmt.Println(result)
    }
}
