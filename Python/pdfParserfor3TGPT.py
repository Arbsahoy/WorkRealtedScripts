#Import required modules to test if they are installed
import importlib.util as iutil
import os

modules = ['selenium']

print('Checking for required modules...')

for mods in modules:
    if iutil.find_spec(mods) is None:
        print('Installing ' + mods + '.')
        os.system('! pip install ' + mods)
    else:
        print(mods + ' is installed.')

#https://harishgarg.com/writing/build-a-chatgpt-for-your-pdf-documents/#:~:text=Easiest%20Guide%20to%20build%20a%20chatGPT%20for%20your,...%207%20Create%20embeddings%20...%208%20Conclusion%20