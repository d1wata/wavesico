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

otherAddress = pw.Address('3PNTcNiUzppQXDL9RZrK3BcftbujiFqrAfM')
myAddress.sendWaves(otherAddress, 10000000)
myToken = myAddress.issueAsset('Token1', 'My Token', 1000, 0)
while not myToken.status():
	pass
myAddress.sendAsset(otherAddress, myToken, 50)
