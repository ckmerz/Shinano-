from extract_dict import AGLT2, AGLT2CHI, AGLT2RTR, RBIN
import json
import requests
import os
import time
import datetime
import pandas as pd 
import numpy as np 

aglt2 = ['CPU_load', 'CPU_utilization', 'Disk_IO_SUMMARY', 'Memory']
aglt2chi = ['input', 'output']
rbin = ['GBIn', 'GBOut', 'GBpsIn', 'GBpsOut', 'UtilIn', 'UtilOut']
aglt2rtr = ['Input', 'Output']

aglt2_min = []
aglt2_max = []
aglt2_mean = []
aglt2_std = []

aglt2chi_min = []
aglt2chi_max = []
aglt2chi_mean = []
aglt2chi_std = []

rbin_metrics = []

aglt2rtr_min = []
aglt2rtr_max = []
aglt2rtr_mean = []
aglt2rtr_std = []

for i in range(len(aglt2)):
	print("====AGLT2====", aglt2[i])
	dfmin, dfmax, dfmean, dfstd = AGLT2("{}".format(aglt2[i]))
	aglt2_min.append(dfmin)
	aglt2_max.append(dfmax)
	aglt2_mean.append(dfmean)
	aglt2_std.append(dfstd)

for j in range(len(aglt2chi)):
	print("====AGLT2_CHI====", aglt2chi[j])
	dfmin, dfmax, dfmean, dfstd = AGLT2CHI("{}".format(aglt2chi[j]))
	aglt2chi_min.append(dfmin)
	aglt2chi_max.append(dfmax)
	aglt2chi_mean.append(dfmean)
	aglt2chi_std.append(dfstd)

for k in range(len(rbin)):
	print("====RBIN====", rbin[k])
	metrics = RBIN("{}".format(rbin[k]))
	rbin_metrics.append(metrics)

for m in range(len(aglt2rtr)):
	print("====AGLT2_Routers====", aglt2rtr[m])
	dfmin, dfmax, dfmean, dfstd = AGLT2RTR("{}".format(aglt2rtr[m]))
	aglt2rtr_min.append(dfmin)
	aglt2rtr_max.append(dfmax)
	aglt2rtr_mean.append(dfmean)
	aglt2rtr_std.append(dfstd)

print(aglt2rtr_min)
print(aglt2rtr_min[0])
print(aglt2rtr_min[0]["rtr-1-eth-1-51"])

timepath = os.environ["time"]
if os.path.isdir(timepath):
        print("Path exists: ", timepath)
else:
        print("Path does not exist")

with open(os.path.join(timepath, "Timing.txt") ) as f:
	lines = f.read()

startime = int(lines[0:10])
startime = datetime.datetime.utcfromtimestamp(startime).strftime('%Y-%m-%d %H:%M:%S')
endtime = int(lines[11:21])
endtime = datetime.datetime.utcfromtimestamp(endtime).strftime('%Y-%m-%d %H:%M:%S')

data = {
	"summary": {
	'Name': 'Environment Metrics'
	,
	'Start': startime #AGLT2_ind.start_final
	,
	'End': endtime #AGLT2_ind.end_final
	}, 
	"aglt2 dest":{
		'CPU Load Min': aglt2_min[0]
		,
		'CPU Load Max': aglt2_max[0]
		,
		'CPU Load Ave': aglt2_mean[0]
		, 
		'CPU Load Std': aglt2_std[0]
		,
		'CPU Utilization Min': aglt2_min[1]
		,
		'CPU Utilization Max': aglt2_max[1]
		,
		'CPU Utilization Ave': aglt2_mean[1]
		,
		'CPU Utilization Std': aglt2_std[1]
		,
		'Disk IO Min': aglt2_min[2]
		, 
		'Disk IO Max': aglt2_max[2]
		,
		'Disk IO Ave': aglt2_mean[2]
		, 
		'Disk IO Std': aglt2_std[2]
		, 
		'Memory Min': aglt2_min[3] 
		, 
		'Memory Max': aglt2_max[3]
		, 
		'Memory Ave': aglt2_mean[3]
		, 
		'Memory Std': aglt2_std[3]
	},

#Chicago Metrics
	"paths":{
		"chic-aglt2":{
			'Input Min': aglt2chi_min[0] 
			,
			'Input Max': aglt2chi_max[0]
			,
			'Input Ave': aglt2chi_mean[0]
			,
			'Input Std': aglt2chi_std[0]
			,
			'Output Min': aglt2chi_min[1]
			,
			'Output Max': aglt2chi_max[1]
			,
			'Output Ave': aglt2chi_mean[1]
			,
			'Output Std': aglt2chi_std[1]
		},
	},
	
#AGLT2 Router Metrics
	'router':{
		'Input':{
			"rtr-1-eth-1-51 Min": aglt2rtr_min[0]["rtr-1-eth-1-51"]
  			,
			"rtr-1-eth-1-52 Min": aglt2rtr_min[0]["rtr-1-eth-1-52"]
			,
			"rtr-2-eth-1-51 Min": aglt2rtr_min[0]["rtr-2-eth-1-51"]
			,
			"rtr-2-eth-1-52 Min": aglt2rtr_min[0]["rtr-2-eth-1-52"]
			,
			"rtr-1-eth-1-51 Max": aglt2rtr_max[0]["rtr-1-eth-1-51"]
			,
			"rtr-1-eth-1-52 Max": aglt2rtr_max[0]["rtr-1-eth-1-52"]
			,
			"rtr-2-eth-1-51 Max": aglt2rtr_max[0]["rtr-2-eth-1-51"]
			,
			"rtr-2-eth-1-52 Max": aglt2rtr_max[0]["rtr-2-eth-1-52"]
			,
			"rtr-1-eth-1-51 Mean": aglt2rtr_mean[0]["rtr-1-eth-1-51"]
			,
			"rtr-1-eth-1-52 Mean": aglt2rtr_mean[0]["rtr-1-eth-1-52"]
			,
			"rtr-2-eth-1-51 Mean": aglt2rtr_mean[0]["rtr-2-eth-1-51"]
			,
			"rtr-2-eth-1-52 Mean": aglt2rtr_mean[0]["rtr-2-eth-1-52"]
			,
			"rtr-1-eth-1-51 Std": aglt2rtr_std[0]["rtr-1-eth-1-51"]
			,
			"rtr-1-eth-1-52 Std": aglt2rtr_std[0]["rtr-1-eth-1-52"]
			,
			"rtr-2-eth-1-51 Std": aglt2rtr_std[0]["rtr-2-eth-1-51"]
			,
			"rtr-2-eth-1-52 Std": aglt2rtr_std[0]["rtr-2-eth-1-52"]
		},
		'Output':{
			"rtr-1-eth-1-51 Min": aglt2rtr_min[1]["rtr-1-eth-1-51"]
  			,
			"rtr-1-eth-1-52 Min": aglt2rtr_min[1]["rtr-1-eth-1-52"]
			,
			"rtr-2-eth-1-51 Min": aglt2rtr_min[1]["rtr-2-eth-1-51"]
			,
			"rtr-2-eth-1-52 Min": aglt2rtr_min[1]["rtr-2-eth-1-52"]
			,
			"rtr-1-eth-1-51 Max": aglt2rtr_max[1]["rtr-1-eth-1-51"]
			,
			"rtr-1-eth-1-52 Max": aglt2rtr_max[1]["rtr-1-eth-1-52"]
			,
			"rtr-2-eth-1-51 Max": aglt2rtr_max[1]["rtr-2-eth-1-51"]
			,
			"rtr-2-eth-1-52 Max": aglt2rtr_max[1]["rtr-2-eth-1-52"]
			,
			"rtr-1-eth-1-51 Mean": aglt2rtr_mean[1]["rtr-1-eth-1-51"]
			,
			"rtr-1-eth-1-52 Mean": aglt2rtr_mean[1]["rtr-1-eth-1-52"]
			,
			"rtr-2-eth-1-51 Mean": aglt2rtr_mean[1]["rtr-2-eth-1-51"]
			,
			"rtr-2-eth-1-52 Mean": aglt2rtr_mean[1]["rtr-2-eth-1-52"]
			,
			"rtr-1-eth-1-51 Std": aglt2rtr_std[1]["rtr-1-eth-1-51"]
			,
			"rtr-1-eth-1-52 Std": aglt2rtr_std[1]["rtr-1-eth-1-52"]
			,
			"rtr-2-eth-1-51 Std": aglt2rtr_std[1]["rtr-2-eth-1-51"]
			,
			"rtr-2-eth-1-52 Std": aglt2rtr_std[1]["rtr-2-eth-1-52"]
		},		
	}
}

date = os.environ["currentdate"]
#Change currentdate to something else? Appears in IndEnv.sh 

dictpath = os.environ["dict"]
#print(data)

if os.path.isdir(dictpath):
        print("Path exists: ", dictpath)
else:
        print("Path does not exist")

with open(os.path.join(dictpath,'dict_{}.json'.format(date)), 'w') as json_file:
    json.dump(data, json_file, indent=4)