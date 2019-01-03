import pywaves as pw
from coinbase.wallet.client import Client
import configparser

```
Grabbing keys from 'config.ini'

```

config = configparser.ConfigParser()
config.read('config.ini')

apiKey = config['COINBASE']['api']
secretKey = config['COINBASE']['secret']
privKey = config['WAVES']['privkey']

assetPrice = config['WAVES']['assetprice']

```
Functions

```

def calcAmtSent(amtUSD): 
	total = amtUSD/assetPrice
	return total



```
Pseudocode/Semicode
Piecing Ideas

```

wavesAccount = pw.Address(privateKey=privKey)

if notifReceived():
	wavesAccount.sendAsset(otherAddress, myToken, 50)

