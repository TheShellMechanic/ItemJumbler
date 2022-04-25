# NFT Juggler
NFT images created using NFT art engines are generated in a sequential pattern, and with this comes the issue of neighbouring images to look very similar to each other. Removing the chance of them looking the same allows for what NFT's are about, randomness.

The randomness in the images can come in the smart contract, but creating a smart contract with more functions than what is necessary creates higher gas fees. This keeps it simple and cheap.

## Installation

```sh
git clone https://github.com/TheShellMechanic/ItemJuggler.git
```
```sh
python3 -m pip install -r requirements.txt
```

## Prerequisites
First you need to populate a folder named build with all of the assets that need to be converted. This includes the untouched, newly rendered, .png files and .json files. (If the images have a different file name edit lines 30, 31 and 44 to fit your needs)

You as the user need to edit the following to fit your needs:
 - AMOUNT
 - IPFS
 - NAME


## Note

Most code was taken from:
https://github.com/kamilsadik/nft_shuffler
but due to it being a Juniper file, there was no point in forking and editting it.
