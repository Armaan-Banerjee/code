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

    err = pprof.StartCPUProfile(f)
    if err != nil {
        panic(err)
    }

    pprof.StopCPUProfile()
}
