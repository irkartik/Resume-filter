import os
import textract
import shutil

def findWord(text, word):
    if text.lower().count(word.lower()):
        return True
    else:
        return False

curr_dir = os.path.dirname(os.path.realpath(__file__))

# root directory with folders files = curr_dir + data

root_dir = os.path.join(curr_dir, 'data')

for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        fname = os.path.join(subdir, file)
        try:
            text = textract.process(fname)
        except Exception as e:
            print(e)
            pass
        if findWord(text, "personal") or findWord(text, "achievement") or findWord(text, "institute") or findWord(text, "college") or findWord(text, "hobbies") or findWord(text, "hobby") or findWord(text, "education") or findWord(text, "vitae"):
            source = os.path.join(subdir, file)
            # dest_abs = "~/Desktop/work/data/"
            dest = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'data'))
            try:
                shutil.move(source, dest)
                print('moved '+ file)
            except:
                print("Error")
                pass


print("**********COMPLETED***********")
