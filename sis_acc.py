#-*- coding: utf-8 -*-
import os
import datetime

order_args = (
("NCL2015-0075",5828205.13,4486018.03,662107.7,0,0,40000,0,0,68612.82),
("NCL2016-047",1307692.31,1066666.67,4615.38,20830,61538.46,8000,0,0,16961.54),
("NCL2015-0361",6219555.33,4887380,94441.86,77215.04,0,181150,0,280331.03,179853.16),
("NCL2015-0317",145393.16,106004.27,4163.04,2551.65,0,500,0,0,2397.9),
("NCL2015-0041",58405.13,42487.18,769.23,1025.01,0,800,0,0,256.13),
("NCL2015-0022",574040.38,411536.46,7511.85,10074.41,0,2000,0,0,2430.5),
("NCL2015-0008",97077.44,68848.03,1483.24,1703.71,0,300,0,0,379.28),
("NCL2015-0075-1",58974.36,33666.9,9000,0,0,1000,0,0,258.97),
("NCL2016-137",330662.62,233003.42,4976.93,5803.13,19929.74,2500,0,0,1264.98),
("NCL2015-0059",1161831.62,688131.82,137712,18952.77,0,5000,0,0,7271.12),
("NCL2015-0371",68726.5,38898.46,9923.08,0,0,0,0,0,0),
("NCL2015-0218",25726.5,18199.4,0,0,0,1500,0,0,771.79),
("NCL2014-367",193076.92,131066.67,2307.69,0,0,3000,0,0,3400),
("NCL2015-0178",932341.88,557868.24,82051.29,0,0,17500,0,0,12350.87),
("NCL2016-122",323076.92,217846.15,3600,0,21600,6000,0,0,1292),
("NCL2015-0222",200000,131035.9,3076.92,0,0,5000,0,0,856.41),
("NCL2014-746",1010256.41,663723.08,0,17002,0,11820,0,2000,6730.77),
("NCL2015-0344",19509.98,12735.04,0,342.4,0,300,0,0,58.53),
("NCL2015-0216",38136.75,16818.17,8000,0,0,600,0,0,3988.89),
("NCL2015-0094",27179.49,17337.54,0.01,0,0,300,0,0,0),
("NCL2014-724",410940.17,220811.97,41025.64,0,28205.12821,8800,0,0,3526.92),
("NCL2015-0208",47564.1,30240.74,0,0,0,300,0,0,2378.21),
("NCL2015-0004",555555.56,351713.36,0,0,76923.08,12500,0,0,35470.09),
("NCL2015-0283",138639,87462.28,0,0,0,0,10000,0,7242.43),
("NCL2015-0198",1880606.84,1094581.96,88888.89,31023.75,0,40000,0,125000,29975.15),
("NCL2014-760",1836345.3,965989.74,164102.57,0,0,30000,0,0,15375.41),
("NCL2014-399",364102.56,189443.59,30000,0,74358.97436,11000,0,0,11200),
("NCL2015-0069",23846.13,14357.75,0,0,0,300,0,0,0),
("NCL2015-0020",1938461.54,926644.92,217200,29027,535384.62,5150,0,0,4307.69),
("NCL2015-0019",2261538.46,1074306.46,250800,29027,624615.38,5150,0,0,5025.64),
("NCL2016-019",2261538.46,1074306.46,250800,29027,624615.38,5150,0,0,5025.64),
("NCL2015-0284",28641.37,16273.5,0.01,502.66,0,300,0,0,85.92),
("NCL2015-0239",132051.28,72230.77,0,0,0,3000,0,0,16602.56),
("NCL2015-0057",484615.38,202000,53907.69,0,133846.15,4600,0,0,1076.92),
("NCL2014-750",1173316.24,518735.79,97851.29,27455.6,0,8000,0,85000,13177.44),
("NCL2014-707",713675.21,317615.38,41025.64,0,90084.61538,10000,0,0,13905.95),
("NCL2015-0388",29487.18,14360.86,0,0,0,0,0,0,0),
("NCL2015-0399",38461.54,18252.23,0.01,0,0,2000,0,0,8151.78),
("NCL2014-727",1216500,471822.54,97200,0,0,9000,0,20000,37951.41),
("NCL2015-0051",61538.46,28317.95,0,0,0,1200,0,0,12307.69),
("NCL2015-0117",256410.26,117991.45,0.01,0,0,5000,0,0,51282.05),
("NCL2016-093",18405.98,8232.05,100,0,0,500,0,0,4365.15),
("NCL2014-394",1683589.74,521152.56,126000,0,606666.6667,10000,0,0,13569.23),
("NCL2014-482",2512820.51,757774.36,82051.28,0,1405128.205,20000,0,0,28574.36),
("NCL2015-0087",56538.46,12447.26,5928.2,0,0,2000,0,0,0),
("NCL2015-0065",799743.59,205069.23,0,0,367622.95,3000,0,0,2230.77)
)


class Order:
	def __init__(self,contract,mp,bom,install,tender_fee,tpc,ship,ship_oversea,others,bonus):
		self.contract = contract  
		self.mp = float(mp)
		self.bom = float(bom)
		self.install = float(install)
		self.tender_fee = float(tender_fee)
		self.tpc = float(tpc)
		self.ship = float(ship) 
		self.ship_oversea = float(ship_oversea) 
		self.others = float(others) 
		self.bonus = float(bonus) 
		self.renew_gm()


	def renew_gm(self):
		self.gm1 = self.mp-self.bom-self.install
		self.gm1_per = self.gm1/self.mp
		self.gm2 = self.gm1 - self.tender_fee -self.tpc
		self.gm2_per = float(self.gm2/self.mp)
		self.gm3 = self.gm2 - self.ship -self.ship_oversea
		self.gm3_per = self.gm3/self.mp
		self.cm1 = self.gm3 -self.bonus
		self.cm1_per = self.cm1/self.mp


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
	def get_bonus_gm2(self,p1 =0.25,p2=0.2,p3=0.15,p4=0.1,p5=0.075,p6=0.05):
		base = self.gm2
		if self.gm2_per >= 0.3:
			per = p1
		elif self.gm2_per >= 0.2:
			per = p2
		elif self.gm2_per >= 0.15:
			per = p3
		elif self.gm2_per >= 0.1:
			per = p4
		elif self.gm2_per >= 0.08:
			per = p5
		elif self.gm2_per < 0.08:
			per = p6
		return base*per

	def set_mp(self,mp):
		self.mp = mp
		self.renew_gm()
	
# --------------------------------------------------------------------------------------------------------------


#写入当前文件夹下以时间命名的函数
def save_to_file(common_name,content):
	str_now = datetime.datetime.now().strftime('%y%m%d %H-%M-%S')
	result_file_name = os.path.dirname(os.path.abspath(__file__)) +'\\'+common_name +str_now+'.txt'
	with open(result_file_name,"w") as result_file:
		result_file.write(content.encode('utf-8'))
	print "saved to file: " + result_file_name



orders = []
for arg in order_args:
	orders.append(Order(arg[0],arg[1],arg[2],arg[3],arg[4],arg[5],arg[6],arg[7],arg[8],arg[9]))
# --------------------------------------------------------------------------------------------------------------


results = ['']
for o in orders:
	results[0] = 'contract,MP,GM1%,GM2%,origin_bonus,SPC_A,SPC_B,SPC_C,SPC_D'
	result = "%s,%.2f,%.4f,%.4f,%.2f," %(o.contract,o.mp,o.gm1_per,o.gm2_per,o.bonus)
	result += "%.2f," %(o.get_bonus_gm2(p1 =0.25,p2=0.2,p3=0.15,p4=0.13,p5=0.11,p6=0.095))
	result += "%.2f," %(o.get_bonus_gm2(p1 =0.25,p2=0.2,p3=0.165,p4=0.14,p5=0.115,p6=0.10))
	result += "%.2f," %(o.get_bonus_gm2(p1 =0.25,p2=0.2,p3=0.15,p4=0.12,p5=0.105,p6=0.09))
	result += "%.2f," %(o.get_bonus_gm2(p1 =0.25,p2=0.2,p3=0.15,p4=0.13,p5=0.115,p6=0.1))
	results.append(result)

buffer_str=""
for r in results:
	buffer_str +=r+'\n'
save_to_file('acc_summary',buffer_str)

# --------------------------------------------------------------------------------------------------------------
samples = ['contract,MP,GM1,GM2,GM1%,GM2%,SPC_A,SPC_B,SPC_C,SPC_D,']
for o in orders:
	origin_mp = o.mp
	for mp_key in range(100,2000):
		o.set_mp(origin_mp*mp_key/1000)
		if o.gm2_per >= 0.05 and o.gm2_per <=0.3:
			sample = '%s,%.2f,%.2f,%.2f,%.4f,%.4f,' %(o.contract,o.mp,o.gm1,o.gm2,o.gm1_per,o.gm2_per)
			sample += "%.2f," %(o.get_bonus_gm2(p1 =0.25,p2=0.2,p3=0.15,p4=0.13,p5=0.11,p6=0.095))
			sample += "%.2f," %(o.get_bonus_gm2(p1 =0.25,p2=0.2,p3=0.165,p4=0.14,p5=0.115,p6=0.10))
			sample += "%.2f," %(o.get_bonus_gm2(p1 =0.25,p2=0.2,p3=0.15,p4=0.12,p5=0.105,p6=0.09))
			sample += "%.2f," %(o.get_bonus_gm2(p1 =0.25,p2=0.2,p3=0.15,p4=0.13,p5=0.115,p6=0.1))
			samples.append(sample)

buffer_str = ''
for s in samples:
	buffer_str += s+'\n'
save_to_file('acc_samples',buffer_str)

