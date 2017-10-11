# WhatToMine Auto Switch for nvOC mining OS
forked from damNmad smartminer

Put both WTM_AUTO_SWITCH and WTM_AUTO_SWITCH.py in /home/m1/


Edit /home/m1/1bash and add :
```
PAPAMPI_WTM_AUTO_SWITCH="YES"  #( whattomine.com switcher) remember to disable Parallax MODE (_Parallax_MODE="NO")

	# note!! all selected COINS must HAVE ADDRESSES below
	# select which coins you want to mine (profit switch only using this list of coins [ it will auto switch your COIN selection from	this list using whattomine.com info)
	WTM_AUTO_SWITCH_COINS="[ 'ZEC', 'SIB' ]"
	 
	WTM_AUTO_SWITCH_SYNC_INTERVAL="3" # Time to sync with WTM for best coin

	#Go to [ https://whattomine.com/coins]whattomine ] select your cards, hash rate, power. You can also select to mine base on current, 24 	hour, 3 day or a week profit and difficulty. Dont forget to choose same for both profit and difficulty or it will give wrong results. 		Click calculate, then add .json to coins at the begining of the address after you click calculate!!!
	WTM_AUTO_SWITCH_URL="https://whattomine.com/coins.json"

```

Edit /home/m1/3main and add these lines somewhere  after Maxximus007_AUTO_TEMPERATURE_CONTROL ( easier to find "SALFTER_NICEHASH_PROFIT_SWITCHING" and add before it:
```


if [ $PAPAMPI_WTM_AUTO_SWITCH == "YES" ]
then
BITCOIN="theGROUND"
# Creating a log file to record coin switch 
LOG_FILE="/home/m1/8_wtmautoswitchlog"
if [ -e "$LOG_FILE" ] ; then
  #Limit the logfile, just keep the last 2K
  LASTLOG=$(tail -n 1K $LOG_FILE)
  echo "$LASTLOG"
  echo ""
fi
echo "LAUNCHING:  PAPAMPI_WTM_AUTO_SWITCH "
echo ""

#WTM_URL=$WTM_AUTO_SWITCH_URL
#WTM_COINS=$WTM_AUTO_SWITCH_COINS
#export WTM_URL
#export WTM_COINS

cat <<EOF >/home/m1/WTM.json
{
 "WTM_URL": "$WTM_AUTO_SWITCH_URL",
 "WTM_COINS": "$WTM_AUTO_SWITCH_COINS"
}
EOF

HCD='/home/m1/PAPAMPI_WTM'
running=$(ps -ef | awk '$NF~"PAPAMPI_WTM" {print $2}')
if [ "$running" == "" ]
then
guake -n $HCD -r PAPAMPI_WTM_AUTO_SWITCH -e "bash /home/m1/PAPAMPI_WTM"
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
 
Copy the whole address and paste it to WTM_AUTO_SWITCH.py replace the default address:

```
data = requests.get("https://whattomine.com/coins.json");
```
Set the coins you want to be switched in WTM_AUTO_SWITCH.py in the included tags :

```
includeTags = [ 'ZEC', 'ZEN', 'ZCL', 'SIB' , 'LBC'  ]
```

Now you can start wtm auto switch with 
```bash WTM_AUTO_SWITCH &```
