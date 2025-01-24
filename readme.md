## Entregável capacitação IJR

### Instalação

1. **Clone o Repositório**
   ```bash
   git clone https://github.com/seuusuario/appreservas.git
   cd appreservas
   ```

2. **Crie um Ambiente Virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as Dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as Variáveis de Ambiente**
   
   Crie um arquivo 

.env

 no diretório raiz e adicione as seguintes variáveis:
   ```env
   ENVIRONMENT=dev
   FERNET_SECRET_KEY=sua_chave_secreta_fernet
   MONGO_USER=seu_usuario_mongo
   MONGO_PWD=sua_senha_mongo
   SENDGRID_API_KEY=sua_chave_api_sendgrid
   CLIENT_URL=http://localhost:5173
   JWT_SECRET_KEY=sua_chave_secreta_jwt
   ```

5. **Execute a Aplicação**
   ```bash
   uvicorn src.app:app --reload
   ```

   A API estará acessível em `http://localhost:8000`.

### Endpoints da API

#### Autenticação

- **Registrar**
  - `POST /client/auth/register`
  - `POST /admin/auth/register`

- **Login**
  - `POST /client/auth/login`
  - `POST /admin/auth/login`

#### Gerenciamento de Reservas

- **Criar Reserva**
  - `POST /client/create-reservation`

- **Atualizar Reserva**
  - `PUT /admin/update-reservation/{reservation_id}`

- **Deletar Reserva**
  - `DELETE /admin/delete-reservation/{reservation_id}`

- **Obter Reservas**
  - `GET /admin/get-reservations`
  - `GET /admin/get-reservation/{reservation_id}`
  - `GET /client/get-reservation/{client_id}`

#### Gerenciamento de Usuários

- **Criar Usuário**
  - `POST /client/auth/register`
  - `POST /admin/auth/register`

- **Deletar Usuário**
  - `DELETE /client/delete/{client_id}`
  - `DELETE /admin/delete/{admin_id}`

- **Checar Usuário**
  - `POST /client/auth/check/token`
  - `POST /admin/auth/check/token`

