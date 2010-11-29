from lvm import *

test = lvm()
#test.create('2G','testtttt','vg-xen-01')
#test.remove('vg-xen-01','test')
test.lvscan()
