# HBNB - The Console  

This repository contains the initial stage of a larger student project to build a clone of the AirBnB website. This stage focuses on creating a **backend console** to manage program data. The console provides a command-line interface where users can **create, update, destroy, and query objects**, with persistent storage through JSON serialization/deserialization.  

---

## 👨‍💻 About the Developer  
Hello! My name is **Ahmad Nawabi**, a passionate **Software Engineer** focused on building impactful applications and solving real-world problems through technology.  

- 💼 [LinkedIn](https://www.linkedin.com/in/ahmadnawabi)  
- 🌐 [Portfolio](https://github.com/ahmadnawabi/portfolio)  
- 🐦 [Twitter](https://twitter.com/ahmadnawabi)  
- 💻 [GitHub](https://github.com/ahmadnawabi)  

---

## 📖 Project Overview  
The **HBNB Console** is the backbone of the AirBnB clone. It enables:  
- Managing objects: `User`, `Place`, `City`, `State`, `Amenity`, `Review`, and more.  
- Persistent data storage using JSON files.  
- Extensible design for scaling into web applications.  

This project demonstrates mastery of **OOP in Python**, **unit testing**, **serialization**, and **interactive shells**.  

---

## 📂 Repository Contents by Project Task  

| Task | File(s) | Description |
|------|---------|-------------|
| 0. Authors/README | [AUTHORS](AUTHORS) | Contains project contributors |
| 1. Pep8 | N/A | All code follows PEP8 style guide |
| 2. Unit Testing | [/tests](tests) | Unit tests for all class-defining modules |
| 3. BaseModel | [/models/base_model.py](models/base_model.py) | Parent class for all models |
| 4. kwargs in BaseModel | [/models/base_model.py](models/base_model.py) | Recreate instances from dictionary representation |
| 5. FileStorage | [/models/engine/file_storage.py](models/engine/file_storage.py) | Persistent storage manager |
| 6. Console 0.0.1 | [console.py](console.py) | Basic console with quit, EOF handling |
| 7. Console 0.1 | [console.py](console.py) | CRUD methods for stored data |
| 8. User Class | [user.py](models/user.py) | Implements user class |
| 9. More Classes | [place.py, city.py, state.py, amenity.py, review.py](models/) | Implements additional models |
| 10. Console 1.0 | [console.py](console.py) | Dynamic console support for all classes |

---

## ⚡ Getting Started  

### 1. Clone the Repository  
```bash
git clone https://github.com/ahmadnawabi/AirBnB_clone.git
cd AirBnB_clone
```

### 2. Install Dependencies  
Ensure you have **Python 3.8+** installed. Create a virtual environment and install required dependencies:  
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Running the Project  
Start the console:  
```bash
./console.py
```

You’ll see:  
```
(hbnb)
```

---

## 🛠️ Commands  

- `create <class>` → Creates a new instance  
- `show <class> <id>` → Shows an object  
- `destroy <class> <id>` → Deletes an object  
- `all [class]` → Lists all objects (or all of a given class)  
- `update <class> <id> <attr_name> <value>` → Updates attributes  
- `quit` or `EOF` → Exit console  

### Alternative Syntax  
```
<class name>.<command>([args])
```
Examples:  
- `User.all()`  
- `User.show("1234-5678-9012")`  
- `User.destroy("1234-5678-9012")`  
- `User.update("1234", {"name": "NewName", "age": 30})`

---

## 📸 Examples  

### Creating a BaseModel  
```bash
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
```

### Showing an Object  
```bash
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-...) {...}
```

### Updating an Object  
```bash
(hbnb) update BaseModel 1234 first_name "John"
```

### Alternative Syntax Example  
```bash
(hbnb) User.update("1234", {"name": "Alice", "age": 25})
```

---

## 🚀 Story of Development  
This project was developed as part of the **ALX SE Program**.  
The main challenge was implementing a **robust command interpreter** and ensuring **data persistence** with JSON storage. Debugging required deep testing of serialization, deserialization, and CLI parsing.  

---

## ✅ Features Implemented  
- Interactive command console  
- JSON-based storage system  
- CRUD operations for multiple classes  
- Alternative advanced syntax support  

## 🔮 Features To Be Implemented  
- Database storage (MySQL)  
- API endpoints  
- Web-based front end  

---

## 🔧 Debugging Tips  
- Use `help <command>` inside the console for guidance.  
- Run unit tests with:  
```bash
python3 -m unittest discover tests
```
- Check `.json` file for raw object data.  

---

## 🤝 Contributing  
Contributions are welcome!  
1. Fork the repo  
2. Create a new branch (`git checkout -b feature-branch`)  
3. Commit changes (`git commit -m 'Add new feature'`)  
4. Push and create a Pull Request  

---

## 📜 License  
This project is licensed under the **MIT License**.  
