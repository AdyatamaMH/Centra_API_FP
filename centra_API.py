from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from datetime import datetime
import mysql.connector
from mysql.connector import Error
from fastapi.middleware.cors import CORSMiddleware
from centra_pydantic import BatchID, Centra, Delivery

# Database configuration
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'Labmda767',
    'database': 'moringa'
}

app = FastAPI()

# CORS Middleware Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database connection
def get_db_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        raise HTTPException(status_code=500, detail="Database connection error")

# BatchID
@app.get("/batch_id/{batch_id}")
def get_batch_id(batch_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM batch_id WHERE Batch_ID = %s", (batch_id,))
        batch = cursor.fetchone()
        conn.close()
        if batch is None:
            raise HTTPException(status_code=404, detail="Batch not found")
        return JSONResponse(content=jsonable_encoder(batch))
    except Exception as e:
        print(f"Error fetching batch_id: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/batch_id/")
def create_batch_id(batch: BatchID):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO batch_id (RawWeight, InTime_Raw, InTime_Wet, OutTime_Wet, WetWeight, InTime_Dry, OutTime_Dry, Centra_ID, DryWeight, InTime_Powder, OutTime_Powder, PowderWeight, Status, Package_ID, WeightRescale) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (batch.RawWeight, batch.InTime_Raw, batch.InTime_Wet, batch.OutTime_Wet, batch.WetWeight, batch.InTime_Dry, batch.OutTime_Dry, batch.Centra_ID, batch.DryWeight, batch.InTime_Powder, batch.OutTime_Powder, batch.PowderWeight, batch.Status, batch.Package_ID, batch.WeightRescale)
        )
        conn.commit()
        conn.close()
        return JSONResponse(content={"message": "Batch created successfully"}, status_code=201)
    except Exception as e:
        print(f"Error creating batch_id: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Delivery
@app.get("/delivery/{package_id}")
def get_delivery(package_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM delivery WHERE Package_ID = %s", (package_id,))
        delivery = cursor.fetchone()
        conn.close()
        if delivery is None:
            raise HTTPException(status_code=404, detail="Delivery not found")
        return JSONResponse(content=jsonable_encoder(delivery))
    except Exception as e:
        print(f"Error fetching delivery: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/delivery/")
def create_delivery(delivery: Delivery):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO delivery (Status, InDeliveryTime, OutDeliveryTime, ExpeditionType) VALUES (%s, %s, %s, %s)",
            (delivery.Status, delivery.InDeliveryTime, delivery.OutDeliveryTime, delivery.ExpeditionType)
        )
        conn.commit()
        conn.close()
        return JSONResponse(content={"message": "Delivery created successfully"}, status_code=201)
    except Exception as e:
        print(f"Error creating delivery: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.put("/delivery/{package_id}")
def update_delivery(package_id: int, delivery: Delivery):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE delivery SET Status = %s, InDeliveryTime = %s, OutDeliveryTime = %s, ExpeditionType = %s WHERE Package_ID = %s",
            (delivery.Status, delivery.InDeliveryTime, delivery.OutDeliveryTime, delivery.ExpeditionType, package_id)
        )
        conn.commit()
        conn.close()
        return JSONResponse(content={"message": "Delivery updated successfully"})
    except Exception as e:
        print(f"Error updating delivery: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.delete("/delivery/{package_id}")
def delete_delivery(package_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM delivery WHERE Package_ID = %s", (package_id,))
        conn.commit()
        conn.close()
        return JSONResponse(content={"message": "Delivery deleted successfully"})
    except Exception as e:
        print(f"Error deleting delivery: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Centra
@app.get("/centra/{centra_id}")
def get_centra(centra_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM centra WHERE Centra_ID = %s", (centra_id,))
        centra = cursor.fetchone()
        conn.close()
        if centra is None:
            raise HTTPException(status_code=404, detail="Centra not found")
        return JSONResponse(content=jsonable_encoder(centra))
    except Exception as e:
        print(f"Error fetching centra: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/centra/")
def create_centra(centra: Centra):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO centra (name, description, created_at) VALUES (%s, %s, %s)",
            (centra.name, centra.description, datetime.utcnow())
        )
        conn.commit()
        conn.close()
        return JSONResponse(content={"message": "Centra created successfully"}, status_code=201)
    except Exception as e:
        print(f"Error creating centra: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.put("/centra/{centra_id}")
def update_centra(centra_id: int, centra: Centra):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE centra SET name = %s, description = %s, updated_at = %s WHERE Centra_ID = %s",
            (centra.name, centra.description, datetime.utcnow(), centra_id)
        )
        conn.commit()
        conn.close()
        return JSONResponse(content={"message": "Centra updated successfully"})
    except Exception as e:
        print(f"Error updating centra: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.delete("/centra/{centra_id}")
def delete_centra(centra_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM centra WHERE Centra_ID = %s", (centra_id,))
        conn.commit()
        conn.close()
        return JSONResponse(content={"message": "Centra deleted successfully"})
    except Exception as e:
        print(f"Error deleting centra: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
