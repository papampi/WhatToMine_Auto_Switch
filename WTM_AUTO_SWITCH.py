#!/usr/bin/env python2.7
#_*_ coding: utf-8 _*_
#### damNmad+papampi Whattomine auto switch written by papampi, forked from smartminer by damNmad

import requests;

import sys
import os
import json
cfg=json.loads(open(sys.argv[1]).read())

coin_list=cfg["WTM_URL"]

includeTags=cfg["WTM_COINS"]

#data = requests.get("https://whattomine.com/coins.json");

#coin_list = os.environ["WTM_URL"]

data = requests.get(coin_list);

coinsData = data.json()['coins'];
coins = coinsData.keys();
highBTCrev = {};

#includeTags = [ 'ZEC', 'ZEN', 'ZCL', 'SIB' , 'LBC'  ]
#includeTags = os.environ["WTM_COINS"]

filterdCoins = {k: v for k, v in coinsData.iteritems() if v['tag']  in includeTags}
coins = filterdCoins.keys()
# print len(filterdCoins)

def findBTCrev(d1):
    return (d1)

for coin in coins:
    coinObj = coinsData[coin]
    coinObj['smartProfitability'] = findBTCrev(coinObj['btc_revenue'])
    highBTCrev[coin] = coinObj

for k in highBTCrev:
    print highBTCrev[k]['tag'], ' - ', highBTCrev[k]['smartProfitability']

BTCrevenueSort = sorted(filterdCoins.values(), key=lambda d: d['smartProfitability'],reverse=True);

if (len(BTCrevenueSort) > 1):
    finalCoin = BTCrevenueSort[0]

log=open("top_coin", "w")
log.write(finalCoin['tag'])
log.close()
