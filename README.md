# WhatToMine Auto Switch for nvOC mining OS
forked from damNmad smartminer

Put both WTM_AUTO_SWITCH and WTM_AUTO_SWITCH.py in /home/m1/


Edit /home/m1/1bash and add :
```
# WTM AUTO SWITCH SETTINGS# remember to disable Parallax MODE (_Parallax_MODE="NO")
 
WTM_AUTO_SWITCH="YES"
WTM_AUTO_SWITCH_SYNC_INTERVAL="3" # Time to sync with WTM for best coin
#WTM_AUTO_SWITCH_URL="FOR NOW EDIT IT IN WTM_AUTO_SWITCH.py
#WTM_AUTO_SWITCH_COINS=" FOR NOW EDIT IT IN WTM_AUTO_SWITCH.py > includeTags = [ 'ZEC', 'ZEN', 'ZCL', 'SIB' , 'LBC'  ]
#WTM_AUTO_SWITCH_diff="TO BE ADDED IN NEXT VERSIONS"  # PERCENTAGE TO CHANGE IF TOP COIN IS HIGHER THAN CURRENT COIN 
```

Edit /home/m1/3main and add these lines somewhere  after Maxximus007_AUTO_TEMPERATURE_CONTROL ( easier to find "SALFTER_NICEHASH_PROFIT_SWITCHING" and add before it:
```
if [ $WTM_AUTO_SWITCH == "YES" ]
then
HCD='/home/m1/WTM_AUTO_SWITCH'
running=$(ps -ef | awk '$NF~"WTM_AUTO_SWITCH" {print $2}')
if [ "$running" == "" ]
then
guake -n $HCD -r WTM_AUTO_SWITCH -e "bash /home/m1/WTM_AUTO_SWITCH"
running=""
fi
fi
```
Install requests python module with :
```
sudo apt install  python-requests
```

Go to [url=https://whattomine.com/coins]whattomine[/url] select your cards, hash rate, power.
You can also select to mine base on current, 24 hour, 3 day or a week profit and difficulty. 
Dont forget to choose same for both profit and difficulty or it will give wrong results.
Click calculate, then add .json to coins at the begining of the address after you click calculate!!!
From:
```https://whattomine.com/coins?utf8=✓&adapt_q_280x=0....
```
To: 
```https://whattomine.com/coins.json?utf8=✓&adapt_q_280x=0&adapt_q_380=0&adapt_q_fury=0&adapt_q
```
 
Copy the whole address and paste it to WTM_AUTO_SWITCH.py replace the default address:

```data = requests.get("https://whattomine.com/coins.json");
```
Set the coins you want to be switched in WTM_AUTO_SWITCH.py in the included tags :

```includeTags = [ 'ZEC', 'ZEN', 'ZCL', 'SIB' , 'LBC'  ]
```

Now you can start wtm auto switch with 
```bash WTM_AUTO_SWITCH &```
