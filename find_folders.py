import os
print("it works")
for e,i in enumerate(set(folder for folder, subfolders, files in os.walk('/media/jaime/Almeidata/Dropbox/Torrents/buntu16') for file_ in files if os.path.splitext(file_)[1] == '.mp4')):
	print("{}. {}".format(e, i.replace('/media/jaime/Almeidata/Dropbox/Torrents/buntu16/','')))

# I need ot remove the path from each of the results 