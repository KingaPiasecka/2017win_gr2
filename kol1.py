###Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
##The program should:
# - print out current orientation
# - applied tilt correction
# - run in infinite loop
# - until user breaks the loop
#Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations"). 
#With every simulation step the orentation should be corrected, applied and printed out.
#If you can thing of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#If you have spare time you can implement: Command Line Interface, generators, or even multiprocessing.
#Do your best, show off with good, clean, well structured code - this is more important than number of features.
#After you finish, be sure to UPLOAD this (add, commit, push) to the remote repository.
#Good Luck

import random, time, math

mean_and_standard_dev = (10, 10/3);

def turbulations():
	new_orientation = random.gauss(mean_and_standard_dev[0], mean_and_standard_dev[1])
	return new_orientation;

def tilt_correction(desired_orientation, curent_orientation):
	if desired_orientation < curent_orientation:
		curent_orientation -= math.fabs(desired_orientation - curent_orientation)
	else:
		curent_orientation += math.fabs(desired_orientation - curent_orientation)
	
	return curent_orientation
	

try:
	desired_orientation = random.gauss(mean_and_standard_dev[0], mean_and_standard_dev[1])
	print "plane orientation: ",   desired_orientation
	while True:
		curent_orientation = turbulations()
		print 'turbulations!\ncurent_orientation:: {orientation}'.format(orientation=turbulations())
		time.sleep(0.5)
		print "tilt correction applying"
		time.sleep(1)
		curent_orientation = tilt_correction(desired_orientation, curent_orientation)
		print 'curent_orientation: {orientation}'.format(orientation=curent_orientation)
		time.sleep(3)
except KeyboardInterrupt:
	exit()
