from database import Base, engine
from models import Student, Scholarship

print("📢 Creating tables in database...")
Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully!")
