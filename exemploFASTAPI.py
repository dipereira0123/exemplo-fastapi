import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Inputs(BaseModel):
    inp1: int	
    inp2: str


@app.get ( "/helloworld" )
def example() -> str:
    return "hello world"


@app.post ( "/exemplo2" )
def example2(entregas: Inputs) -> str:
    return entregas.inp2


#Exemplo do Post para o a route /exemplo2
#{
#  "inp1": 1,
#  "inp2": "hello"
#  
#}

#para encontrar o exemplo dos preenchimentos, o FASTAPI ja cria uma documentação no diretório /docs




if __name__ == "__main__":
    uvicorn.run(app, port=8000)

