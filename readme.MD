# FitTrack - FastAPI

API para monitoramento de treinos físicos, com registro de exercícios, séries e progresso.

## Rotas Principais

### **Treinos**
- `GET /treinos` - Lista todos os treinos
- `POST /treinos` - Cria um novo treino
- `GET /treinos/{id}` - Busca treino por ID
- `PUT /treinos/{id}` - Atualiza treino
- `DELETE /treinos/{id}` - Remove treino

### **Exercícios**
- `GET /exercicios` - Lista todos os exercícios
- `POST /exercicios` - Adiciona novo exercício
- `GET /exercicios/{id}` - Busca exercício por ID
- `PUT /exercicios/{id}` - Atualiza exercício
- `DELETE /exercicios/{id}` - Remove exercício