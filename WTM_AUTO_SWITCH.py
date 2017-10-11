#!/usr/bin/env python2.7
# _*_ coding: utf-8 _*_
#### damNmad+papampi+hurvajs77 Whattomine auto switch written by papampi + hurvajs77, forked from smartminer by damNmad

import json
import requests
import sys
import urllib

configFile = "./WTM.json"
topCoinLogFile = "./WTM_top_coin"

# load config
cfg = json.loads(open(configFile).read())
requestUrl = urllib.unquote(urllib.unquote(cfg["WTM_URL"]))
minimumDifference = float(cfg["WTM_MIN_DIFFERENCE"])
includedCoins = cfg["WTM_COINS"].upper()
delimiter = ";"
# load included coins
includedCoins = includedCoins.strip(delimiter)

if not includedCoins:
    print "No incluted coins. Please, check 1bash script for WTM settings."
    sys.exit()

includedCoins = includedCoins.split(delimiter)


def saveTopCoin(data):
    logFile = open(topCoinLogFile, "w")
    logFile.write(data)
    logFile.close()
    return

# try load previous top coin
try:
    with open(topCoinLogFile) as contentFile:
        content = contentFile.read()
except:
    content = "-:0"

topCoin = content.split(":")
print "Currently mining coin: %s, profit: %s" % (topCoin[0], topCoin[1])

try:
    httpResponse = requests.get(requestUrl)
except:
    print("Can not get data from WhatToMine.com.")
    raise

try:
    data = httpResponse.json()['coins']
    data = data.values()
except:
    print "Invalid JSON"
    raise

# filter WTM coins by user selection only
for i in reversed(data):
    if i["tag"] not in includedCoins:
        data.remove(i)

# calculate coin profitability
newProfits = {}
for i in data:
    newProfits[i["tag"]] = i["btc_revenue"]
newProfits = sorted(newProfits.items(), key=lambda x: x[1], reverse=True)

# save current profit
print "New profits"
profitLog = open("current-profit", "w")
for i, j in newProfits:
    profitLog.write("%s:%s\n" % (i, j))
    print i + ": " + j + " BTC"
profitLog.close()

# is currently mining coin same as a new the most profitability coin?
if newProfits[0][0] == topCoin[0]:
    print "Same coin"
    saveTopCoin(newProfits[0][0] + ":" + newProfits[0][1])
    sys.exit()

if float(newProfits[0][1]) < (float(topCoin[1]) + minimumDifference):
    # try find actual top coin and compare their profit with maximum of current profits
    try:
        topCoinNewProfit = filter(lambda x: x["tag"] == topCoin[0], data)[0]["btc_revenue"]
        if (float(topCoinNewProfit) + minimumDifference) < float(newProfits[0][1]):
            print "Currently mining %s coin is no longer profitability" % topCoin[0]
            print "Switching to new %s coin" % newProfits[0][0]
    except:
        print "Top coin was not found in list of included coins"
        sys.exit()

#else:
# current profit is higher that currently mining
print "Found %s coin with higher profitability" % newProfits[0][0]
saveTopCoin(newProfits[0][0] + ":" + newProfits[0][1])



# algo_log = open(algoLogFile, "a")
# algo_log.write(
#    str(datetime.datetime.now()) + ": " + max_profit["coin_name"] + " (" +
#    max_profit["algo"] + ")\n")
# algo_log.close()


# coins = {coinName: coinData for coinName, coinData in data.iteritems() if
#         coinData['tag'] in includedCoins}


# coinsData = data.json()['coins']
# coins = coinsData.keys()
# highBTCrev = {}

# filteredCoins = {k: v for k, v in coinsData.iteritems() if
#                 v['tag'] in includeTags}.keys()


# print len(filteredCoins)

# def findBTCrev(d1):
#    return (d1)


# for coin in filteredCoins:
#    coinObj = coinsData[coin]
#    coinObj['smartProfitability'] = findBTCrev(coinObj['btc_revenue'])
#    highBTCrev[coin] = coinObj

# for k in highBTCrev:
#    print highBTCrev[k]['tag'], ' - ', highBTCrev[k]['smartProfitability']

# BTCrevenueSort = sorted(filteredCoins.values(),
#                        key=lambda d: d['smartProfitability'], reverse=True)

# if (len(BTCrevenueSort) > 1):
#    finalCoin = BTCrevenueSort[0]

# log = open("WTM_top_coin", "w")
# log.write(finalCoin['tag'])
# log.close()
