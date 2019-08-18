# -*- coding: utf-8 -*-
import pandas as pd
import os, time
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '5G'
sheet['A1'] = 'BTSID'
sheet['B1'] = 'IPADDR'
sheet['C1'] = 'TIMESTAMP'
sheet['D1'] = 'PRODUCT CODE'
sheet['E1'] = 'SERIAL NUMBER'
sheet['F1'] = 'ISTI'
sheet['G1'] = 'RESET COUNTER'
sheet['H1'] = 'RESET timestamp'
sheet['I1'] = 'RESET Reason'
sheet['J1'] = 'SW VERSION: active'
sheet['K1'] = 'SW VERSION: passive'
sheet['L1'] = 'SW VERSION: active filesystem'
sheet['M1'] = 'single-bit'
sheet['N1'] = 'double-bit'
at = []
ar = []
#fpath = []
def finddir(startdir, target):
    try:
        os.chdir(startdir)
    except:
        return
    for new_dir in os.listdir(os.curdir):
        btsid = new_dir.split('_')[0]
        ipaddr = new_dir.split('_')[1]
        fpath = [os.getcwd() + os.sep + new_dir]
        #print(fpath)
        for wenjian in fpath:
            #print(wenjian)
            with open(wenjian,'r', encoding='utf-8') as fil:
                df = fil.readlines()
                #print(df)
                ala = df[6:-5]
                at = [a for a in ala]
                for a in ala:
                    print(a)
                timestamp = df[0].replace('TIMESTAMP:', '')
                product_code = df[1].replace('PRODUCT CODE: ', '')
                serial_number = df[2].replace('SERIAL NUMBER: ', '')
                isti = df[3].replace('ISTI: ', '')
                reset_counter = df[4].replace('RESET COUNTER: ', '')
                sw_active = df[-5].replace('SW VERSION: active: ', '')
                sw_passive = df[-4].replace('SW VERSION: passive: ', '')
                filesystem = df[-3].replace('SW VERSION: active filesystem: ', '')
                single = df[-2].replace('ERRORS: ECC single-bit error counter:', '')
                double = df[-1].replace('ECC double-bit error counter:', '')
                #time.sleep(3)

                print(len(ala))
                for x in range(len(ala)):
                    sheet.append([btsid,ipaddr,timestamp,product_code,serial_number,\
                                  isti,reset_counter,at[x],at[x],sw_active,\
                                  sw_passive,filesystem,single,double])

lis = 'C:/Users/25108/Desktop/5G NSA/blackbox0817(1)/'
target = r'*.186_blackbox'
startdir = lis
finddir(startdir, target)

time.sleep(5)
wb.save('5G.xlsx')
