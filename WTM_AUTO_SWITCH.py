#!/usr/bin/env python2.7
#_*_ coding: utf-8 _*_
import requests;


data = requests.get("https://whattomine.com/coins.json?utf8=✓&adapt_q_280x=0&adapt_q_380=0&adapt_q_fury=0&adapt_q_470=0&adapt_q_480=3&adapt_q_570=0&adapt_q_580=0&adapt_q_750Ti=0&adapt_q_10606=1&adapt_q_1070=6&adapt_1070=true&adapt_q_1080=1&adapt_q_1080Ti=1&eth=true&factor%5Beth_hr%5D=180.0&factor%5Beth_p%5D=720.0&grof=true&factor%5Bgro_hr%5D=213.0&factor%5Bgro_p%5D=780.0&x11gf=true&factor%5Bx11g_hr%5D=69.0&factor%5Bx11g_p%5D=720.0&cn=true&factor%5Bcn_hr%5D=3000.0&factor%5Bcn_p%5D=600.0&eq=true&factor%5Beq_hr%5D=2580.0&factor%5Beq_p%5D=720.0&lre=true&factor%5Blrev2_hr%5D=213000.0&factor%5Blrev2_p%5D=780.0&ns=true&factor%5Bns_hr%5D=6300.0&factor%5Bns_p%5D=930.0&lbry=true&factor%5Blbry_hr%5D=1620.0&factor%5Blbry_p%5D=720.0&bk2bf=true&factor%5Bbk2b_hr%5D=9600.0&factor%5Bbk2b_p%5D=720.0&bk14=true&factor%5Bbk14_hr%5D=15000.0&factor%5Bbk14_p%5D=750.0&pas=true&factor%5Bpas_hr%5D=5640.0&factor%5Bpas_p%5D=720.0&skh=true&factor%5Bskh_hr%5D=159.0&factor%5Bskh_p%5D=720.0&factor%5Bl2z_hr%5D=420.0&factor%5Bl2z_p%5D=300.0&factor%5Bcost%5D=0.0&sort=Profit&volume=0&revenue=current&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=bleutrade&factor%5Bexchanges%5D%5B%5D=bter&factor%5Bexchanges%5D%5B%5D=c_cex&factor%5Bexchanges%5D%5B%5D=cryptopia&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=yobit&dataset=Main&commit=Calculate");

coinsData = data.json()['coins'];
coins = coinsData.keys();
highBTCrev = {};

includeTags = [ 'ZEC', 'ZEN', 'ZCL', 'SIB' , 'LBC'  ]

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

