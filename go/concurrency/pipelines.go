package main

import "fmt"

func slicetoChannel(nums []int) <- chan int { // this stage is for converting the slice to a channel
    out := make(chan int) // creates a chennel to store data

    go func(){
        for _, n := range nums { // loops over input array and in each element adds it to the channel
            out <- n
        }

        close(out) 
    }()

    return out
}

func sq(in <- chan int) <- chan int{ // method for squaring numbers in channel
    out := make(chan int)

    go func() { // this function reads the data from the channel outputted from slicetoChannel and blocks the process until it is done 
        for n := range in { // loops over each entry in the channel and squares it
            out <- n*n
        }

        close(out)
    }()

    return out 
}


func main_pipelines(){
    //input

    nums := []int{1, 4, 5, 3, 2} // creats an input slice

    //stage 1
    dataChannel := slicetoChannel(nums) // channel to store the channel that is retruned by slicetoChannel after converting it from a slice

    //stage 2
    finalChannel := sq(dataChannel) // channel to store the channel that is returned by sq after squarign all numbers in an input channel

    //stage 3
    for n := range finalChannel {
        fmt.Println(n)
    }
}
