import arcade

file1 = open("nationsPop.txt", "r")

some_lines = file1.readlines()

for lines in some_lines:
    lines = lines.split(",")
#make sure to change up values and adjust values to actually be readable
my_window = arcade.open_window(400,400, "Populations of largest Nations on Earth")
arcade.set_background_color(arcade.color.EGGSHELL)
arcade.start_render()
arcade.draw_line(80, 400, 80, 80, arcade.color.BLACK)
arcade.draw_line(400, 80, 80, 80, arcade.color.BLACK)


scale = (400 - 80) / len(range(100, 1500, 100))
currentY = 80

#draw y axis legend
for i in range(100, 1500, 100):
    currentLabel = arcade.Text(f"{i}M", 5, currentY, arcade.color.BLACK)
    currentLabel.draw()
    currentY += scale

arcade.finish_render()

arcade.run()