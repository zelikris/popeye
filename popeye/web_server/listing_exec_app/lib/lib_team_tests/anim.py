import matplotlib.animation as animation
import os.path

plotted = False 
   
def plot_anim(fig, update_func, file_name):
    global plotted
    anim = animation.FuncAnimation(fig, update_func, 25, interval=50, blit=True)
    save_anim(anim, str(file_name))
    plotted = True
    
def mesh_anim(fig, update_func, file_name):
    global plotted    
    anim = animation.FuncAnimation(fig, update_func, 25, interval=50, blit=True)
    save_anim(anim, str(file_name))
    plotted = True
        
def isanimated():
    return plotted              

def save_anim(anim, file_name):
    anim.save(str(file_name) + '.mp4', fps=20)
    os.system('ffmpeg -y -i ' + str(file_name) + '.mp4 -r 20 -pix_fmt rgb24 ' + str(file_name) + '.gif')              