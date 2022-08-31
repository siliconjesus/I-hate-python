## Initial by @TokyoEdTech
import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("4,4,4")
wn.setup(width=800, height=600)
wn.tracer(0)

# main loop
while True:
    wn.update()