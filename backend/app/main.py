from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from .database import get_db
from .services import db_export

from .routes import category
from .routes import user 
from .routes import auth
from .routes import product
from .routes import contact
from .routes import cart
from .routes import order
from .routes import location
from .routes import analytics
from .routes import admin
from .routes import favorite
from .routes import reports

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping-db")
def ping_db():
    try:
        # Get a connection from the pool
        db_gen = get_db()
        db = next(db_gen)
        cursor = db.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        cursor.close()
        db.close()
        return {"status": "Database connected successfully!", "result": result}
    except Exception as e:
        return {"error": str(e)}

app.include_router(category.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(product.router)
app.include_router(contact.router)
app.include_router(cart.router)
app.include_router(order.router)
app.include_router(location.router)
app.include_router(analytics.router)
app.include_router(admin.router)
app.include_router(favorite.router)
app.include_router(reports.router)



if __name__ =="__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8020, reload=False)