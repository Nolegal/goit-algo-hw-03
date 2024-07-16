import turtle


def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            # Рекурсія
            koch_snowflake(t, order-1, size / 3)
            t.left(angle)
           






def main():
    screen = turtle.Screen()
    screen.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)

    #order = 3
    size = 300

    # Створення сніжинки Коха
    print("1 side:")
    order1=int(input())
    koch_snowflake(t, order1, size/2)
    t.right(120)
    print("2 side:")
    order2=int(input())
    koch_snowflake(t, order2, size/2)
    t.right(120)
    print("3 side:")
    order3=int(input())
    koch_snowflake(t, order3, size/2)
    t.right(120)
   
   
    screen.mainloop()


if __name__ == "__main__":
    main()

