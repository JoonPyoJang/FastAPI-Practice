from fastapi import FastAPI
from todo import todo_router
app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return{
        "message": "Hello World"
    }

app.include_router(todo_router) #API 라우터를 추가

# 이 방식은 단일 경로만 고려하는 애플리케이션에서 일반적으로 사용된다.
# FastAPI 인스턴스를 사용하는 경우 애플리케이션은 한 번에 여러 라우트를 처리할 수 없어 APIRouter 클래스를 사용한다.



