from moralis import evm_api

def verificar_saldo(wallet):
    api_key = "TU_API_KEY"
    params = {
        "address": wallet,
        "chain": "eth"
    }
    resultado = evm_api.balance.get_native_balance(api_key=api_key, params=params)
    return resultado['balance']
