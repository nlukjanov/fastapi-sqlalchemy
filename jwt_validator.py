from pathlib import Path

import jwt
from cryptography.x509 import load_pem_x509_certificate


def decode_and_validate_token(access_token):
    unverified_headers = jwt.get_unverified_header(access_token)
    x509_certificate = load_pem_x509_certificate(
        Path('public_key.pem').read_text().encode()
    ).public_key()

    return jwt.decode(
        access_token,
        key=x509_certificate,
        algorithms=unverified_headers['alg'],
        audience='https://coffeemesh.io/orders'
    )


token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL2F1dGguY29mZmVlbWVzaC5pbyIsInN1YiI6IjQ1Njc2NTQ0NTY3OCIsImF1ZCI6Imh0dHBzOi8vY29mZmVlbWVzaC5pby9vcmRlcnMiLCJpYXQiOjE2NTYyMjIzNDQsImV4cCI6MTY1NjI3OTk0NC43NTI2MDh9.iEvoaNBvemScaCBH89tMI2_v-LvJ7rH-xHT8Qd6xgI-DTRmS5-dbqkbWSQ5ngUXfXHtj1AbtH5ELAslIvvvX-y_JXzw9URZnd-HEUkZqcglrYzSIU3qjEVp2jGo6jmHgpzSEAz68gphARKxAvwv2X3DT_lK02Ad469GFIuv75DZE3ylPz9QqtRX1e5EDC0D8SXng7ve54-IBFXhhYCQBhXBmhUsdvzSj7eVIc9_gRXQSfmksawO8Cl5zZ282wjRpya50Lql7o_Hw6pfjJIk9G6v2iWsUf3TtmTUZaMU2X8U3C7jo8T4ndfC7hnsGI63a1QhXgHED8J7V-__l2iHfJQ'

print(decode_and_validate_token(token))
