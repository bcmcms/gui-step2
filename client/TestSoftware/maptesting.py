from uHTR import uHTR
import Hardware as hw
from client import webBus
import DChains
import DaisyChain
import QIE


active_slots=[2]
bus=webBus()

for i in active_slots:
	dc=hw.getDChains(i, bus)
	hw.openChannel(i, bus)
	dc.read()
	for j in xrange(12):
		qie=dc[j]
		qie.ChargeInjectDAC(8640)
		dc.write()
		info=get_mapping_histo()
		print "Slot: {4} Qie: {3}, slot: {0}, link: {1}: channel: {2}".format(info[0], info[1], info[2], j, i)



