# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 02:27:36 2019

@author: Mani
"""
from kamene.all import *
from pyx import *
import json
import pandas as pd
proto = []
src = []
dst = []
data = []
ttl = []
with PcapReader('1.pcap') as pcap_reader:
  for pkt in pcap_reader:
      data.append(pkt)
for i in range(len(data)):
    proto.append(data[i][IP].proto)
    src.append(data[i][IP].src)
    dst.append(data[i][IP].dst)
    ttl.append(data[i][IP].ttl)

src1 = pd.DataFrame(src)
dst1 = pd.DataFrame(dst)
ttl1 = pd.DataFrame(ttl)
df = pd.concat([src1,dst1,ttl1],axis=1)
df.to_csv('1.csv')