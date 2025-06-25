from moralis import evm_api

def verificar_nfts(wallet):
    return evm_api.nft.get_wallet_nfts(
        api_key="TU_API_KEY",
        params={"address": wallet, "chain": "eth"}
    )
