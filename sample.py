from app import db, Book



libro = Book("El Quijote", "Miguel de Cervantes", "1234-5678-9012", "15", "Julio de la Cruz", "787-123-4567", "julio@example.com", "El libro esta en perfectas condiciones.")

db.session.add(libro)
db.session.commit()