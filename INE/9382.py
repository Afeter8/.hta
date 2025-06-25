# Notificación automática sin humanos
from moralis import streams

def alerta_transferencias(wallet):
    stream = streams.create_stream({
      "webhookUrl": "https://cesar.star/api",
      "description": "Alerta IA CESAR",
      "tag": "cesar_defense",
      "chains": ["eth"],
      "advancedOptions": [{
        "topic0": "Transfer(address,address,uint256)",
        "filter": {
          "eq": ["to", wallet]
        }
      }]
    })
