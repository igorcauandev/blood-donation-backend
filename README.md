# 🩸 API de Banco de Sangue

Documentação da API REST desenvolvida em Python com Flask para gerenciamento de doações de sangue.

**Autor:** Igor Cauan de Oliveira Amancio

---

## 📋 Índice

- [Visão Geral](#visão-geral)
- [Tecnologias](#tecnologias)
- [Estrutura de Dados](#estrutura-de-dados)
- [Rotas](#rotas)
  - [Doadores](#doadores)
  - [Bolsas de Sangue](#bolsas-de-sangue)
  - [Estoque](#estoque)
  - [Hemocentros](#hemocentros)
  - [Triagem](#triagem)

---

## Visão Geral

API desenvolvida para gerenciar o fluxo de doações de sangue, incluindo cadastro de doadores, controle de bolsas, triagem clínica, gestão de hemocentros e estoque por tipo sanguíneo.

---

## Tecnologias

- Python 3.x
- Flask
- Blueprints (modularização de rotas)

---

## Estrutura de Dados

A API utiliza um módulo `dados.py` como banco de dados em memória. Abaixo estão as entidades principais:

### Usuário / Doador (`user`)

```json
{
  "id": 1,
  "name": "Igor",
  "email": "igor@email.com",
  "phone": "44999999999",
  "documentType": "CPF",
  "documentNumber": "000.000.000-00",
  "bloodType": "O+",
  "age": 30,
  "gender": "masculino",
  "weight": 70.0,
  "height": 1.75,
  "birthDate": "1994-01-01",
  "isEligibleToDonate": true,
  "address": {
    "street": "Rua das Flores",
    "number": "123",
    "complement": "Apto 1",
    "neighborhood": "Centro",
    "city": "Maringá",
    "state": "PR",
    "zipCode": "87000-000"
  },
  "createdAt": "2024-06-01",
  "updatedAt": "2024-06-01"
}
```

### Triagem (`userScreening`)

```json
{
  "id": 1,
  "userId": 1,
  "schedulingId": 1,
  "bloodPressure": "120/80",
  "ironLevel": 13.5,
  "status": "aprovado",
  "rejectionReason": "",
  "date": "2024-06-01",
  "createdAt": "2024-06-01",
  "updatedAt": "2024-06-01"
}
```

### Bolsa de Sangue (`bloodCenterBags`)

```json
{
  "id": 1,
  "userId": 1,
  "bloodDonationId": 1,
  "bloodCenterId": 1,
  "bloodType": "O+",
  "volume": 450.0,
  "status": "disponível",
  "expirationDate": "2024-12-01",
  "createdAt": "2024-06-01",
  "updatedAt": "2024-06-01"
}
```

### Hemocentro (`bloodCenter`)

```json
{
  "id": 1,
  "name": "Banco de Sangue Central",
  "phone": "44999999999",
  "isActive": true,
  "address": {
    "street": "Av. Principal",
    "number": "500",
    "complement": "",
    "neighborhood": "Centro",
    "city": "Maringá",
    "state": "PR",
    "zipCode": "87000-000"
  },
  "createdAt": "2024-06-01",
  "updatedAt": "2024-06-01"
}
```

### Agendamento (`scheduling`)

```json
{
  "id": 1,
  "userId": 1,
  "bloodCenterId": 1,
  "scheduledDateTime": "2024-07-01T09:00:00",
  "status": "agendado",
  "createdAt": "2024-06-01",
  "updatedAt": "2024-06-01"
}
```

---

## Rotas

---

### Doadores

#### `GET /doadores`

Retorna a lista completa de doadores cadastrados.

**Resposta de sucesso** `200 OK`:
```json
[
  {
    "id": 1,
    "nome": "Igor",
    "idade": 30,
    "peso": 70,
    "genero": "masculino",
    "tipoSanguineo": "O+",
    "fatorRh": "+"
  }
]
```

**Resposta quando vazio** `400`:
```json
{ "mensagem": "Nenhum doador encontrado" }
```

---

#### `POST /doadores`

Cadastra um novo doador.

**Body (JSON)**:
```json
{
  "nome": "Maria",
  "idade": 25,
  "peso": 60,
  "genero": "feminino",
  "tipoSanguineo": "A+",
  "fatorRh": "+"
}
```

**Resposta de sucesso** `201 Created`:
```json
{
  "mensagem": "Doador cadastrado",
  "doador": {
    "nome": "Maria",
    "idade": 25,
    "peso": 60,
    "genero": "feminino",
    "tipoSanguineo": "A+",
    "fatorRh": "+"
  }
}
```

---

#### `GET /doadores/<id>`

Retorna um doador específico pelo ID.

**Parâmetros:**

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| `id` | int | Índice do doador na lista |

**Resposta de sucesso** `200 OK`:
```json
{
  "id": 1,
  "nome": "Igor",
  "idade": 30,
  "peso": 70,
  "genero": "masculino",
  "tipoSanguineo": "O+",
  "fatorRh": "+"
}
```

**Resposta de erro** `400`:
```json
{ "erro": "Doador não encontrado" }
```

---

### Bolsas de Sangue

#### `GET /bolsas`

Retorna todas as bolsas de sangue registradas.

**Resposta de sucesso** `200 OK`:
```json
[
  {
    "id": 1,
    "quantidade": "100ml",
    "dataColeta": "2024-06-01",
    "dataValidade": "2024-12-01",
    "dataSaida": "2024-12-01",
    "localArmazenamento": "Banco de Sangue Central",
    "tipoSanguineo": "O+",
    "doador": "Igor"
  }
]
```

---

#### `POST /bolsas`

Registra uma nova bolsa de sangue. Os dados também são salvos no arquivo `bolsa.json`.

**Body (JSON)**:
```json
{
  "quantidade": "450ml",
  "dataColeta": "2024-06-10",
  "dataValidade": "2024-12-10",
  "dataSaida": "",
  "localArmazenamento": "Hemocentro Norte",
  "tipoSanguineo": "A-",
  "doador": "Maria"
}
```

**Resposta de sucesso** `201 Created`:
```json
{ "mensagem": "Bolsa registrada" }
```

**Resposta de erro** `400`:
```json
{ "erro": "JSON inválido" }
```

---

#### `GET /bolsas/tipo/<tipo>`

Retorna todas as bolsas de um tipo sanguíneo específico.

**Parâmetros:**

| Parâmetro | Tipo | Exemplo |
|-----------|------|---------|
| `tipo` | string | `O+`, `A-`, `AB+` |

**Resposta de sucesso** `200 OK`:
```json
[
  {
    "id": 1,
    "tipoSanguineo": "O+",
    "doador": "Igor",
    "quantidade": "100ml"
  }
]
```

---

#### `GET /bolsas/<id>`

Retorna uma bolsa específica pelo ID.

**Parâmetros:**

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| `id` | int | Identificador da bolsa |

**Resposta de sucesso** `200 OK`:
```json
{
  "id": 1,
  "quantidade": "100ml",
  "tipoSanguineo": "O+",
  "doador": "Igor"
}
```

**Resposta de erro** `400`:
```json
{ "erro": "Bolsa não encontrada" }
```

---

### Estoque

#### `GET /estoque`

Retorna o estoque completo de sangue por tipo sanguíneo.

**Resposta de sucesso** `200 OK`:
```json
{
  "A+": 10,
  "A-": 5,
  "B+": 8,
  "B-": 3,
  "AB+": 4,
  "AB-": 2,
  "O+": 15,
  "O-": 7
}
```

---

#### `GET /estoque/<tipo_sanguineo>`

Retorna a quantidade disponível de um tipo sanguíneo específico.

**Parâmetros:**

| Parâmetro | Tipo | Exemplo |
|-----------|------|---------|
| `tipo_sanguineo` | string | `A+`, `O-`, `AB+` |

**Resposta de sucesso** `200 OK`:
```json
{ "A+": 10 }
```

**Resposta de erro** `400`:
```json
{ "erro": "Tipo sanguíneo não encontrado" }
```

---

### Hemocentros

#### `GET /homocentros`

Retorna a lista de todos os hemocentros cadastrados.

**Resposta de sucesso** `200 OK`:
```json
[
  {
    "id": 1,
    "name": "Banco de Sangue Central",
    "phone": "44999999999",
    "isActive": true,
    "address": {
      "street": "Av. Principal",
      "number": "500",
      "city": "Maringá",
      "state": "PR",
      "zipCode": "87000-000"
    }
  }
]
```

---

#### `GET /homocentros/<id>`

Retorna um hemocentro específico pelo ID.

**Parâmetros:**

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| `id` | int | Índice do hemocentro na lista |

**Resposta de sucesso** `200 OK`:
```json
{
  "id": 1,
  "name": "Banco de Sangue Central",
  "isActive": true
}
```

**Resposta de erro** `400`:
```json
{ "erro": "Homocentro não encontrado" }
```

---

#### `POST /homocentros`

Cadastra um novo hemocentro.

**Body (JSON)**:
```json
{
  "name": "Hemocentro Norte",
  "phone": "44988888888",
  "isActive": true,
  "address": {
    "street": "Rua das Palmeiras",
    "number": "200",
    "city": "Maringá",
    "state": "PR",
    "zipCode": "87010-000"
  }
}
```

**Resposta de sucesso** `201 Created`:
```json
{
  "mensagem": "Homocentro registrado",
  "homocentro": {
    "name": "Hemocentro Norte",
    "isActive": true
  }
}
```

**Resposta de erro** `400`:
```json
{ "erro": "JSON inválido" }
```

---

### Triagem

#### `POST /triagem`

Registra uma nova triagem clínica para um doador.

**Body (JSON)**:
```json
{
  "userId": 1,
  "schedulingId": 1,
  "bloodPressure": "120/80",
  "ironLevel": 13.5,
  "status": "aprovado",
  "rejectionReason": "",
  "date": "2024-06-01"
}
```

**Resposta de sucesso** `201 Created`:
```json
{ "mensagem": "Triagem registrada" }
```

**Resposta de erro** `400`:
```json
{ "erro": "JSON inválido" }
```

---

#### `GET /triagens`

Retorna a lista de todas as triagens registradas.

**Resposta de sucesso** `200 OK`:
```json
[
  {
    "id": 1,
    "userId": 1,
    "bloodPressure": "120/80",
    "ironLevel": 13.5,
    "status": "aprovado",
    "date": "2024-06-01"
  }
]
```

**Resposta quando vazio** `400`:
```json
{ "mensagem": "Nenhuma triagem encontrada" }
```

---

## Resumo das Rotas

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/doadores` | Lista todos os doadores |
| POST | `/doadores` | Cadastra um novo doador |
| GET | `/doadores/<id>` | Busca doador por ID |
| GET | `/bolsas` | Lista todas as bolsas |
| POST | `/bolsas` | Registra uma nova bolsa |
| GET | `/bolsas/<id>` | Busca bolsa por ID |
| GET | `/bolsas/tipo/<tipo>` | Busca bolsas por tipo sanguíneo |
| GET | `/estoque` | Lista estoque completo |
| GET | `/estoque/<tipo>` | Busca estoque por tipo sanguíneo |
| GET | `/homocentros` | Lista todos os hemocentros |
| POST | `/homocentros` | Cadastra um novo hemocentro |
| GET | `/homocentros/<id>` | Busca hemocentro por ID |
| POST | `/triagem` | Registra uma triagem |
| GET | `/triagens` | Lista todas as triagens |