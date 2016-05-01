#-*- coding: utf-8 -*-
import os
import datetime
from openpyxl import Workbook,load_workbook

order_args = (
('NCL2014-500',5726495.73,5379220,46858,0,0,0,0,17752,71786,17037),
('NCL2015-0134',14434878,13424289,143680,0,133444,0,100000,54421,221149,23006),
('NCL2015-0378',2119393,1942948,35046,7001,0,0,0,23146,55337,4160),
('NCL2014-535',4715650.43,4322711,561230,0,0.01,0,0,22371,82380,15401),
('NCL2015-0085',6904273,6341879,64926,0,0,34521,0,27236,100500,22118),
('NCL2015-0376',1617429.06,1461407,32160,0,24816,0,0,10789,32617,1892),
('NCL2014-465',395935,352842,5492,7000,0,0,0,0,4730,0),
('NCL2015-0251',6961998.29,6304036,94514,13261.64,0,34809.99,0,56248,148672,0),
('NCL2015-0426',923693.16,826749,18743,0,15887,0,0,6670.58,23501,3780),
('NCL2015-0125',560230,493253,17649,0,0,2801,0,6419,4931,1958),
('NCL2015-0233',60769,54359,1022,0,0,0,0,607,1786,0),
('NCL2015-0024',707841,636934,7054,0,0,0,0,6164,15412,2259),
('NCL2014-476',766530,686322,6756,0,0,0,0,9454,23265,2450),
('NCL2015-0056',891571,789938,13582,0,0,0,0,8043,13874,3022),
('NCL2014-560',1189743,1046990,13617,7001,15449,0,0,11052,21304,3884),
('NCL2014-462',67721,59046,1394,0,1188,0,0,575,825,208),
('NCL2014-590',420000,369192,4882,0,0,0,3000,12569,7646,1254),
('NCL2014-485',2591946,2306880,1307,0,0,0,0,27264,42384,8223),
('NCL2015-0173',1839384,1584417,38533,0,0,0,0,0,63179,7766),
('NCL2014-493',1640865,1397699,243166,0,0,22134,0,15195,43069,5304),
('NCL2014-559',36653,31575,705,0,643,0,0,523,1468,135),
('NCL2014-578',6326444,5379524,174211,0,78215,63264,7403,79428,270692,12672),
('NCL2014-484-1',78153,60181,1316,7000,0,0,0,600,2343,285),
('NCL2014-540',48482,41538,705,0,850,0,0,598,1942,181),
('NCL2015-0404',84600,72377,1307,0,0,0,0,2831,3735,349),
('NCL2015-0081',232188,180841,12935,7002,0,1160,0,7727,14769,1042),
('NCL2015-0420',115905,100030,0,0,0,0,0,2865,1395,470),
('NCL2014-508',108335.23,90168,3051,0,1091,0,810.279999999999,1298,4257,421),
('NCL2014-489',369478,305834,11846,0,0,0,0,6039,18041,1498),
('NCL2014-513',290811,245098,4235,0,0,0,0,6409,7759,980),
('NCL2015-0333',62034.19,51992,1133,0,0,0,0,930,2042,238),
('NCL2014-455',152250,128246,1962,0,0,0,0,6503,3975,497),
('NCL2014-549',125071,104845,1351,0,2195,0,0,971,4552,455),
('NCL2014-541',105982,88621,1307,0,0,0,0,2951,3885,415),
('NCL2015-0357',457628,362570,24830,0,0,0,0,13744,33549,2083),
('NCL2014-473',133963,111798,1307,0,0,0,0,4300,3788,473),
('NCL2015-0088',331461,267678,12167,0,0,0,0,13433,23105,1439),
('NCL2014-406',17917292,14930913,163025,0,107671,0,123989,217395,507991,32410),
('NCL2015-0220',1693970.09,1384640,19420,15301.1400000001,0,0,0,39224,40603,3238),
('NCL2015-0022',2173130,1759640,45677,0,31968,0,0,15700,103754,9113),
('NCL2015-0406-1',75017,57887,4315,0,0,0,0,3497,6239,487),
('NCL2014-555',2841615.38,2292771,62625,0,40571,30000,83117.84,110703,144849,11713),
('NCL2015-0285',90000,73285,1133,0,0,0,0,801,3128,0),
('NCL2015-0361',6219555.33,4887380,94440,0,77215,0,0,181150,254071,26259),
('NCL2015-0180',83418.8,51970,4309,7964.22,0,0,0,4477,5940,413),
('NCL2014-495',174615,114903,5928,0,0,11160,0,7396,6963,983),
('NCL2015-0330',9871.79,5004,610,0,0,0,0,500,362,45.9),
('NCL2015-0287',476068,134782,7933,0,0,0,0,5189,42495,2765)
)

class Order:
	def __init__(self,contract,mp,bom,drum,other1,tender_fee,tpc,other2,transport,variable,travel):
		self.contract = contract
		self.mp = float(mp)
		self.bom = float(bom)
		self.drum = float(drum)
		self.other1 = float(other1)
		self.tpc = float(tpc)
		self.other2 = float(other2)
		self.transport = float(transport) 
		self.variable = float(variable)
		self.travel = float(travel)
		self.tender_fee = float(tender_fee)
		self.renew_gm()
		# #对gm1落在正确范围内的点进行计数
		# self.cnt_between_gm1 = 0
		# #对新方案奖金>=2014方案范围内的点进行计数
		# self.cnt_new_win = 0
		# self.cnt_2016_win = 0


	def renew_gm(self):
		self.gm1 = self.mp-self.bom-self.drum-self.other1
		self.gm1_per = self.gm1/self.mp
		self.gm2 = self.gm1 - self.tender_fee -self.tpc - self.other2
		self.gm2_per = self.gm2/self.mp
		self.gm3 = self.gm2 - self.transport -self.variable -self.travel
		self.gm3_per = self.gm3/self.mp


	def get_bonus2014(self):
		cm2 = self.gm3
		cm2_per = cm2/self.mp
		if cm2_per>=0.2:
			per = 0.3
			base = cm2
		elif cm2_per >=0.1:
			per = 0.25
			base = cm2
		elif cm2_per >0.03:
			per = 0.2
			base = cm2
		else:
			if self.mp >= 10*1000000:
				per = 0.3/100
				base = self.mp - self.tpc
			elif self.mp >= 5*1000000:
				per = 0.4/100
				base = self.mp - self.tpc
			elif self.mp >= 0.5*1000000:
				per = 0.5/100
				base = self.mp - self.tpc
			else:
				per = 0
				base = 0
		return base*per

	def get_bonus2016(self):
		base = self.mp-self.tpc

		if self.gm1_per >= 0.3:
			per = 0.05 
		elif self.gm1_per >= 0.2:
			per = 0.04
		elif self.gm1_per >= 0.15:
			per = 0.025
		elif self.gm1_per >= 0.1:
			per = 0.015
		elif self.gm1_per >= 0.08:
			per = 0.01
		elif self.gm1_per < 0.08:
			per = 0.005
		return base*per

	def get_bonus_new(self,p1=0.05,p2=0.04,p3=0.025,p4=0.015,p5=0.01,p6=0.005):
		base = self.mp-self.tpc

		if self.gm1_per >= 0.3:
			per = p1
		elif self.gm1_per >= 0.2:
			per = p2
		elif self.gm1_per >= 0.15:
			per = p3
		elif self.gm1_per >= 0.1:
			per = p4
		elif self.gm1_per >= 0.08:
			per = p5
		elif self.gm1_per < 0.08:
			per = p6
		return base*per

	def set_mp(self,mp):
		self.mp = mp
		self.renew_gm()
'''
	def show(self):
		arr_bonus = []
		arr_bonus.append(self.get_bonus2014())
		arr_bonus.append(self.get_bonus2016())
		increment = 0.005
		#增加0.5%,0.6%,0.7%...1.2%
		for i in range(5,13):
			increment = i*0.001
		arr_bonus.append(get_bonus_new(self,increment+0.05,increment+0.04,increment+0.025,increment+0.015,increment+0.01,increment+0.005))
		str_show = "%s,%.2f," %(self.contract,self.gm1_per*100)
		for b in arr_bonus:
			str_show += "%.2f," %(b)
		return str_show
		

	def show_between_gm1(self,gm1_start,gm1_end):
		if self.gm1_per >= gm1_start and self.gm1_per <= gm1_end:
			str_show = self.show()
			return str_show
		else:
			return None
'''
o1 = Order('NCL2015-0220',1693970.09,1384640,19420,15301.14,0,0,0,39224,40603,3238)
o2 = Order("NCL2015-0134",14434878,13424289,143680,0,133444,0,100000,54421,221149,3006)


#detail 是输出每条模拟数据的结果，每个合同可能有几百条
#summary 是输出整个合同的模拟结果，每个合同只有一条
def iter_an_order(order,origin_mp,gm1_start,gm1_end,detail=True,summary = True):
	class Sample:
		pass

	samples = []
	for i in range(100,3000):
		order.set_mp(origin_mp*i/1000)
		if order.gm1_per >= gm1_start and order.gm1_per <= gm1_end:
			arr = []
			for j in range(0,13):
				incre = j*0.001
				arr.append(order.get_bonus_new(incre+0.05,incre+0.04,incre+0.025,incre+0.015,incre+0.01,incre+0.005))
			
			sample = Sample()
			sample.contract = order.contract
			sample.mp = order.mp
			sample.b14 = order.get_bonus2014()
			sample.gm1_per = order.gm1_per
			sample.bonus_arr = arr

			samples.append(sample)


	#函数输出用的字符串
	str_all_details = 'contract,mp,gm1_per,b14,other_bonus\n'
	str_summary = "contract,all,b0_win_rate,b1_win_rate...bn_win_rate\n"
	str_all =''
	#对win进行计数的数组，0位置是总数，后面是每个方案的win counter
	cnt_arr = []
	for i in range(0,30):
		cnt_arr.append(0)

	for s in samples:
		cnt_arr[0] +=1	
		s.str = "%s,%.2f,%.2f,%.2f," %(s.contract,s.mp,s.gm1_per*100,s.b14)
		
		num_bonus = len(s.bonus_arr)
		for i in range(num_bonus):
			s.str += "%.2f," %(s.bonus_arr[i])
			if s.bonus_arr[i] >= s.b14:
				cnt_arr[i+1] +=1
		s.str +='\n'
		str_all_details += s.str
	
	if summary:
		str = "%s," %(order.contract)
		for item in cnt_arr:
			str += "%.2f," %(float(item)/float(cnt_arr[0])*100)
		str_summary += str +'\n'
		str_all +=str_summary
	if detail:
		str_all +=str_all_details

	return str_all

#写入当前文件夹下以时间命名的函数
def save_to_file(common_name,content):
	str_now = datetime.datetime.now().strftime('%y%m%d %H-%M-%S')
	result_file_name = os.path.dirname(os.path.abspath(__file__)) +'\\'+common_name +str_now+'.txt'
	with open(result_file_name,"w") as result_file:
		result_file.write(content.encode('utf-8'))
	print "saved to file: " + result_file_name
def save_detal_to_excel(filename):
	pass

def save_as_xlsx(workbook,name,save_dir):
	# str_now = datetime.datetime.now().strftime('-%y%m%d-%H-%M-%S')
	# new_filename = os.path.dirname(os.path.abspath(__file__))+'\\test'+str_now+'.xlsx'
	new_filename = save_dir+"\\"+ name +'.xlsx'
	print new_filename
	workbook.save(new_filename)



orders = []
for arg in order_args:
	orders.append(Order(arg[0],arg[1],arg[2],arg[3],arg[4],arg[5],arg[6],arg[7],arg[8],arg[9],arg[10]))
buffer_str = ''
order_cnt = 0

for o in orders:
	buffer_str += iter_an_order(o,o.mp,0.05,0.20,detail = True,summary=False)
	order_cnt += 1

save_to_file('sis_test',buffer_str)
input('press anykey')


