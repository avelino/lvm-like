import os

class lvm():
	def create(self,size,name,sg):
		os.system("lvcreate -L %s -n %s %s" % (size,name,sg))
		
	def remove(self,sg,name):
		os.system("lvremove -f /dev/%s/%s" % (sg,name))
		
	def lvscan(self):
		os.system("lvscan")
