import firebase_admin
from firebase_admin import credentials, firestore
try:
    firebase_admin.get_app()
except ValueError:
    try:
        firebase_admin.initialize_app(credentials.Certificate("serviceAccountKey.json"))
    except Exception as e:
        print("Firebase init error:", e)
db = firestore.client()
print("Collections sample:", [c.id for c in db.collections()][:5])