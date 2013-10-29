# coding=utf-8
import csv

global okrsek

s01 = s02 = s03 = s04 = s05 = s06 = s07 = s08 = s09 = s10 = s11 = s12 = s13 = s14 = s15 = s16 = s17 = s18 = s19 = s20 = s21 = s22 = S23 = s24 = okrsek = '0'


def sorter(arr):
	global s01
	global s02
	global s03
	global s04
	global s05
	global s06
	global s07
	global s08
	global s09
	global s10
	global s11
	global s12
	global s13
	global s14
	global s15
	global s16
	global s17
	global s18
	global s19
	global s20
	global s21
	global s22
	global s23
	global s24	

	if (arr[2] == '1'):
		s01 = arr[3]
	elif (arr[2] == '2'):
		s02 = arr[3]
	elif (arr[2] == '3'):
		s03 = arr[3]				
	elif (arr[2] == '4'):
		s04 = arr[3]				
	elif (arr[2] == '5'):
		s05 = arr[3]				
	elif (arr[2] == '6'):
		s06 = arr[3]				
	elif (arr[2] == '7'):
		s07 = arr[3]				
	elif (arr[2] == '8'):
		s08 = arr[3]				
	elif (arr[2] == '9'):
		s09 = arr[3]				
	elif (arr[2] == '10'):
		s10 = arr[3]				
	elif (arr[2] == '11'):
		s11 = arr[3]				
	elif (arr[2] == '12'):
		s12 = arr[3]					
	elif (arr[2] == '13'):
		s13 = arr[3]				
	elif (arr[2] == '14'):
		s14 = arr[3]		
	elif (arr[2] == '15'):
		s15 = arr[3]						
	elif (arr[2] == '16'):
		s16 = arr[3]
	elif (arr[2] == '17'):
		s17 = arr[3]		
	elif (arr[2] == '18'):
		s18 = arr[3]		
	elif (arr[2] == '19'):
		s19 = arr[3]		
	elif (arr[2] == '20'):
		s20 = arr[3]		
	elif (arr[2] == '21'):
		s21 = arr[3]		
	elif (arr[2] == '22'):
		s22 = arr[3]		
	elif (arr[2] == '23'):
		s23 = arr[3]			
	elif (arr[2] == '24'):
		s24 = arr[3]		
	else:
		print "guvno"

f = open('/Users/jancibulka/DEVEL/IHNED/demografie/scripts/out.csv', 'a')
f.write('okrsek;CSSD;SSO;CPS;TOP09;HLAVU_VZHURU;ODS;RDS;KAN;PHZ;SSCR;KDU_CSL;CIBULKA;SUVERENITA;AKTIV_NO;SPOZ;OB11;USVIT;DSSS;blank;ANO;KSCM;LEV21;SZ;KČ' + '\n')

with open('/Users/jancibulka/DEVEL/IHNED/demografie/scripts/prahaOkr.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in reader:
		if (row[0] == 'OBEC'):
			continue
		if (okrsek == '0'):
			okrsek = row[1]

		if (row[1] == okrsek):
			sorter(row)
		else:
			f.write(okrsek + ";" + s01 + ';' + s02 + ';' + s03 + ';' + s04 + ';' + s05 + ';' + s06 + ';' + s07 + ';' + s08 + ';' + s09 + ';' + s10 + ';' + s11 + ';' + s12 + ';' + s13 + ';' + s14 + ';' + s15 + ';' + s16 + ';' + s17 + ';' + s18 + ';' + s19 + ';' + s20 + ';' + s21 + ';' + s22 + ';' + s23 + ';' + s24 + '\n')
			okrsek = row[3]
			s01 = s02 = s03 = s04 = s05 = s06 = s07 = s08 = s09 = s10 = s11 = s12 = s13 = s14 = s15 = s16 = s17 = s18 = s19 = s20 = s21 = s22 = S23 = s24 = okrsek = '0'
			sorter(row)

f.write(okrsek + ";" + s01 + ';' + s02 + ';' + s03 + ';' + s04 + ';' + s05 + ';' + s06 + ';' + s07 + ';' + s08 + ';' + s09 + ';' + s10 + ';' + s11 + ';' + s12 + ';' + s13 + ';' + s14 + ';' + s15 + ';' + s16 + ';' + s17 + ';' + s18 + ';' + s19 + ';' + s20 + ';' + s21 + ';' + s22 + ';' + s23 + ';' + s24 + '\n')

f.close()
