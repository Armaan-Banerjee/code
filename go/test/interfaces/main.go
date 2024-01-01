package main

import (
    "fmt"

    "math"
)

type Shape interface{
    area() float32;
    perimeter() float32;
}

type Rectangle struct{
    length, breadth float32
}

type EquilateralTriangle struct{
    length float32
}

func (t EquilateralTriangle) perimeter() float32{
    return 3 * t.length
}

func (t EquilateralTriangle) area() float32 {
    var s float32 = t.perimeter() / 2
    return float32(math.Sqrt(float64(s*3*(s - t.length))))
}

func (r Rectangle) area() float32 {
    return r.length * r.breadth
}

func (r Rectangle) perimeter() float32 {
    return 2 * r.length + 2 * r.breadth
}

func CalcArea(s Shape) float32 {
    fmt.Println("Area: ", s.area())
    return 0
}

func main(){
    
    rect := Rectangle{1.0, 3.0}
    triang := EquilateralTriangle{5.0}
    CalcArea(rect);
    CalcArea(triang);
}
