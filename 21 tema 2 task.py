from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)

engine = create_engine('sqlite:///school.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_student(name):
    """Įterpia mokinį, jei jo dar nėra."""
    if not session.query(Student).filter_by(name=name).first():
        new_student = Student(name=name)
        session.add(new_student)
        session.commit()
        print(f'Mokinys {name} pridėtas.')
    else:
        print(f'Mokinys {name} jau yra duomenų bazėje.')

def add_teacher(name):
    """Įterpia mokytoją."""
    new_teacher = Teacher(name=name)
    session.add(new_teacher)
    session.commit()
    print(f'Mokytojas {name} pridėtas.')

def get_all_students():
    """Išveda visų mokinių sąrašą."""
    students = session.query(Student).all()
    for student in students:
        print(f'Mokinys: {student.name}')

def get_all_teachers():
    """Išveda visų mokytojų sąrašą."""
    teachers = session.query(Teacher).all()
    for teacher in teachers:
        print(f'Mokytojas: {teacher.name}')

add_student('Tomas')
add_student('Dariuš')
add_student('Martynas')

add_teacher('Laura')
add_teacher('Povilas')

print("\nVisi mokiniai:")
get_all_students()

print("\nVisi mokytojai:")
get_all_teachers()
