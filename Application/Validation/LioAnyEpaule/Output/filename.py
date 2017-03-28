import os

def name(context, Basename, ext):
    i = 0
    f = str(Basename[0]) + "." + str(ext[0])
    
    while os.path.exists(os.path.join( f)):
        i += 1
        f =str(Basename[0]) + "_" + str(i) + "." + str(ext[0])


    return f