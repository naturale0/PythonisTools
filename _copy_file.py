#!python3
'''Coded to be used inside Pythonista app.
Add this script to the action menu of the editor to use. Run the script while 
the file to copy is currently opened in the editor.'''

import console
import editor
import os
import shutil

def numbered_filename(filename):
    if os.path.exists(filename):
        i = 2
        numbered_name = ('(' + str(i) + ')').join(os.path.splitext(filename))
        while os.path.exists(numbered_name):
            i += 1
            numbered_name = ('(' + str(i) + ')').join(os.path.splitext(filename))
    return numbered_name

def main():
    file_path = editor.get_path()
    write_path = numbered_filename(os.path.split(file_path)[-1])
    shutil.copy(file_path, write_path)
    console.hud_alert('Copied as: {}'.format(write_path), duration=.75)

if __name__ == '__main__':
    main()
