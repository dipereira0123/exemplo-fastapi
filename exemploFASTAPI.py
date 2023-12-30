import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class inputs(BaseModel):
    inp1: int	
    inp2: str



@app.get ( "/helloworld" )
def example() -> str:
    return "hello world"


@app.get ( "/exemplo2" )
def example2(inputs: Input) -> str:
   
    return inputs.inp2




if __name__ == "__main__":
    uvicorn.run(app, port=8000)

