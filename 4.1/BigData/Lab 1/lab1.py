import json
import matplotlib.pyplot as plt
from matplotlib import animation


FPS = 20
filename = 'file5_1160_786.json'

with open(filename, "r") as jfile:
    df = json.load(jfile)
    data, frames, width, height = df['data'], df['frames'], df['width'], df['height']

    fig = plt.figure() 

    def animate(num):
        frame = data[num]
        dat = [frame[i:i+width] for i in range(len(frame) // height)] 
        image = plt.imshow(dat)
        return [image]
    
    anime = animation.FuncAnimation(fig, animate, frames=frames, interval=FPS, blit = True)
    gifname = filename.split('.')[0] + '.gif'
    anime.save(gifname, fps=FPS)
    plt.show()