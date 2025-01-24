import secrets

# Gera uma chave secreta aleatória de 32 bytes
jwt_secret = secrets.token_urlsafe(32)
print(jwt_secret)