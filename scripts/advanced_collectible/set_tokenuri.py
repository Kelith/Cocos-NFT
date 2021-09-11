#!/usr/bin/python3
from brownie import SimpleCollectible, AdvancedCollectible, accounts, network, config
from metadata import sample_metadata
from scripts.helpful_scripts import get_breed, OPENSEA_FORMAT


dog_metadata_dic = {
    "Cocos1": "https://ipfs.io/ipfs/QmNrtnTjiwPeFfkgWgGJSkpb97NEoe9Hw1kEBbaJAR1FkS?filename=1-Cocos1.json",
    "Cocos2": "https://ipfs.io/ipfs/QmReSFfyiwUtvv3u4UzBmcAUvg3HvChvWsHCsN58zvscXH?filename=2-Cocos3.json",
    "Cocos3": "https://ipfs.io/ipfs/QmReSFfyiwUtvv3u4UzBmcAUvg3HvChvWsHCsN58zvscXH?filename=2-Cocos3.json",
}

def main():
    print("Working on " + network.show_active())
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(
        "The number of tokens you've deployed is: "
        + str(number_of_advanced_collectibles)
    )
    for token_id in range(number_of_advanced_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        if advanced_collectible.tokenURI(token_id).startswith("None"):
            print("Setting tokenURI of {}".format(token_id))
            set_tokenURI(token_id, advanced_collectible,
                         dog_metadata_dic[breed])
        else:
            print("Skipping {}, we already set that tokenURI!".format(token_id))
            print(advanced_collectible.tokenURI(token_id))


def set_tokenURI(token_id, nft_contract, tokenURI):
    dev = accounts.add(config["wallets"]["from_key"])
    nft_contract.setTokenURI(token_id, tokenURI, {"from": dev})
    print(
        "Awesome! You can view your NFT at {}".format(
            OPENSEA_FORMAT.format(nft_contract.address, token_id)
        )
    )
    print('Please give up to 20 minutes, and hit the "refresh metadata" button')
