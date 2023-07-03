package main

import(
    "github.com/gofiber/fiber/v2"
)

func main(){
    app := fiber.New()

    app.Get("/", func(c *fiber.Ctx) error {
      err := c.SendString("And the API is UP!")
      :return err
    })

    app.Get("/hello", func (c *fiber.Ctx) error {
      err := c.SendString("hi")
      return err
      
    })
    
    app.Listen(":3004")
}

