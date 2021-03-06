import wget
from PIL import Image
import os
import tarfile
import shutil
import pymp
cwd = os.getcwd()

handbag_url = 'https://people.eecs.berkeley.edu/~tinghuiz/projects/pix2pix/datasets/edges2handbags.tar.gz'
shoes_url = 'https://people.eecs.berkeley.edu/~tinghuiz/projects/pix2pix/datasets/edges2shoes.tar.gz'

#wget.download(handbag_url)
#wget.download(shoes_url)

with pymp.Parallel(2) as p:
    for index in p.range(0, 2):
		if index == 0:
			print "wget.download(handbag_url)" + handbag_url
			wget.download(handbag_url)
		if index == 1:
			print "wget.download(shoes_url)" + shoes_url
			wget.download(shoes_url)

with pymp.Parallel(2) as p:
    for index in p.range(0, 2):
		if index == 0:
			print "with tarfile.open('./edges2handbags.tar.gz') as tar:"
			with tarfile.open('./edges2handbags.tar.gz') as tar:
				tar.extractall()
				tar.close()
		if index == 1:
			print "with tarfile.open('./edges2shoes.tar.gz') as tar:"
			with tarfile.open('./edges2shoes.tar.gz') as tar:
				tar.extractall()
				tar.close()

bag_dir = "/edges2handbags/train/"
shoe_dir = "/edges2shoes/train/"

bag_list = os.listdir("."+bag_dir)
shoe_list = os.listdir("."+shoe_dir)

os.mkdir("./bags")
os.mkdir("./shoes")
os.mkdir("./result")

for i in bag_list:
	image = Image.open(cwd+bag_dir+i)
	image = image.resize([128,64])
	image = image.crop([64,0,128,64])
	image.save("./bags/"+i)

for i in shoe_list:
	image = Image.open(cwd+shoe_dir+i)
	image = image.resize([128,64])
	image = image.crop([64,0,128,64])
	image.save("./shoes/"+i)

#shutil.rmtree("./edges2handbags")
#shutil.rmtree("./edges2shoes")

os.remove('./edges2handbags.tar.gz')
os.remove('./edges2shoes.tar.gz')
