import tkinter as tk


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):



    
    draw_sky(canvas,0,0)
    draw_sun(canvas,300, 100)
    draw_mount(canvas,scene_left + 200, scene_top + 100, 200)
    draw_mount(canvas,scene_left + 600, scene_top + 100, 200)
    draw_grass(canvas,0,300)
    draw_pine_tree(canvas, scene_left + 300, scene_top + 250, 150)
    draw_pine_tree(canvas, scene_left + 200, scene_top + 250, 150)
    draw_pine_tree(canvas, scene_left + 100, scene_top + 250, 150)
    draw_pine_tree(canvas, scene_left + 400, scene_top + 250, 150)
    draw_pine_tree(canvas, scene_left + 500, scene_top + 250, 150)
    draw_pine_tree(canvas, scene_left + 600, scene_top + 250, 150)
    draw_pine_tree(canvas, scene_left + 700, scene_top + 250, 150)
    draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 100)
    

    #canvas.create_oval(100, 100, 200, 200, outline="#ebde34", fill="#ebde34")


   

def draw_mount(canvas, peak_x, peak_y, height):


    mount_width= height 
    mount_height= height
    mount_left= peak_x - mount_width 
    mount_right = peak_x + mount_width 
    mount_bottom= peak_y + mount_height


    canvas.create_polygon(peak_x, peak_y,mount_right, mount_bottom, mount_left, mount_bottom,
            outline="gray20", width=1, fill="#734608")



def draw_sky(canvas, sky_left, sky_top):

    sky_width= 800
    sky_height=700
    sky_right= sky_left + sky_width
    sky_bottom = sky_top + sky_height
    

    canvas.create_rectangle(sky_left, sky_top, sky_right, sky_bottom, fill="#34c0eb")

def draw_grass(canvas, grass_left, grass_top):

    grass_width= 800
    grass_height=700
    grass_right= grass_left + grass_width
    grass_bottom = grass_top + grass_height
    

    canvas.create_rectangle(grass_left, grass_top, grass_right, grass_bottom, fill="#44d406")    


  


def draw_sun(canvas, sun_left, sun_top):

    sun_width= 200
    sun_height=200
    sun_right= sun_left + sun_width
    sun_bottom = sun_top + sun_height
    



    canvas.create_oval(sun_left,sun_top, sun_right, sun_bottom, fill="#ebde34", width=0)
   

def draw_grid(canvas,left, top, right, bottom, grid_spacing):

        text_horizontal_margin = 20
        text_vertical_margin = 10

        #Draw horizontal lines
        for i in range(top, bottom, grid_spacing):
         canvas.create_line(left,i, right, i)
         canvas.create_text(left + text_horizontal_margin, i + text_vertical_margin, text=f"{i}")

         #vertical

        for i in range(left, right, grid_spacing):
         canvas.create_line(i,top,i,bottom)
         canvas.create_text(i, top + text_vertical_margin, text=f"{i}")


    
  


# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.


def draw_pine_tree(canvas, peak_x, peak_y, height):

    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")


# Call the main function so that
# this program will start executing.
main()