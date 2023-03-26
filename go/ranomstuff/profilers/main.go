package main

import (
    "os"
    "runtime/pprof"
)

func main() {
    f, err := os.Create("cpu.profile")
    if err != nil {
        panic(err)
    }
}
