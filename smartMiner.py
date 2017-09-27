#!/usr/bin/env python2.7
import requests;

DEFAULT_COIN = {'tag': "ZEC"};

data = requests.get("https://whattomine.com/coins.json");
coinsData = data.json()['coins'];
coins = coinsData.keys();
highBTCrev = {};

includeTags = [ 'HUSH', 'ZEC', 'ZEN', 'ZCL', 'SIB' , 'XDN', 'LBC'  ]

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
log=open("current-profit", "w")
log.write(highBTCrev[k]['tag']+ ' - '+ highBTCrev[k]['smartProfitability'])
log.close()

#print sorted(filterdCoins.values(), key=lambda d: d['smartProfitability']);

BTCrevenueSort = sorted(filterdCoins.values(), key=lambda d: d['smartProfitability'],reverse=True);

finalCoin = DEFAULT_COIN;

if (len(BTCrevenueSort) > 1):
    finalCoin = BTCrevenueSort[0]

print finalCoin['tag'];
