import matplotlib.animation as animation
import os.path

animated = False
    
def animate(fig, update_func, init_function=None):
    global animated
    anim = animation.FuncAnimation(fig, update_func, init_func=init_function, blit=False)
#    save_anim(anim, file_name)
    animated = True
    return anim
        
def isanimated():
    return animated

def save_anim(anim, file_name):
    anim.save(str(file_name) + '.mp4', fps=20)
    
    # produces gif of size ~500 KB:
    os.system('ffmpeg -i ' + str(file_name) + '.mp4 -vf scale=320:-1 -r 10 -f image2pipe -vcodec ' + 
                'ppm - | convert -delay 5 -loop 0 - ' + str(file_name) + '.gif') 
    
    # produces gif of size ~ 50MB:          
    #    os.system('ffmpeg -y -i ' + str(file_name) + '.mp4 -r 20 -pix_fmt rgb24 ' + str(file_name) + '.gif')