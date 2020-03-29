import re

date=17

inpath='/Users/mahannan/Audia/Pictia/Mar'+str(date)+'.txt'
outpath='/Users/mahannan/Audia/Pictia/Mar'+str(date)+'.csv'

print inpath
print outpath

f=open(inpath, "r")
f2=open(outpath, "w")

f2.write("city, confirmed cases, heat label\n")

fcontent=f.read().splitlines()

for line in fcontent:
	#line.rstrip('\n')
	print 'before              ',line
	line.replace("//"," ")
	heat = re.search(r' (\d+)', line)
	if(heat):
		print 'heat found ', heat.group()
		heat=int(heat.group())
		print 'old heat ', heat
		if(heat<5):
			heat=1
		elif(5<= heat<10):
			heat=2
		elif(10<=heat<20):
			heat=3
		elif(20<=heat<30):
			heat=4
		elif(30<=heat<40):
			heat=5
		else:
			heat=6
		print 'new heat ', heat
	#line = re.sub(" (\d+)", r" county of Los Angles state of California, \1", line)
	line = re.sub(" (\d+)", r", \1", line)
	if(heat):
		#line.replace('\n', ',')
		print 'after               ', line+", "+str(heat)
		#f2.write("city of "+line+", "+str(heat)+"\n")
		f2.write(line+", "+str(heat)+"\n")
	else:
		print 'after               ', line
		#f2.write("city of "+line+"\n")
		f2.write(line+"\n")

f.close()
f2.close()
