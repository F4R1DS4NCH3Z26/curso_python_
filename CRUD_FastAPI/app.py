from fastapi import FastAPI
from routes.RoutesUser import routes_user
from routes.RouteCreate import routes_create
app = FastAPI()

app.include_router(routes_create)
app.include_router(routes_user)
