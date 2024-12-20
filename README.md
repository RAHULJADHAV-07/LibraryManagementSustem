# 📚 Library Management System

## 🌟 Overview

The Library Management System is a 🕸️ web-based application designed to efficiently manage 📚 books in a 🏛️ library. This app allows users to:
✨ Add new books
🔄 Borrow & return books
❌ Remove books
🔍 Search for books easily.

### 🌐 Hosted Application

Click here to explore the live app: [🚀 Library Management System](https://library-management-9kzq.onrender.com)

---

## 🛠️ Features

1️⃣ **📖 View Books**\
📝 Display all books with 🆔 ID, 📘 Title, 👩‍💻 Author & 📦 Available copies.

2️⃣ **🔎 Search Books**\
Type 🔤 Title or 👤 Author to quickly locate books.

3️⃣ **➕ Add Books**\
Include new 📚 by specifying 🆔 ID, 🖋️ Title, 🧑‍🎨 Author & 🔢 Copies.

4️⃣ **❌ Remove Books**\
Delete books using their unique 🆔 ID.

5️⃣ **📤 Borrow Books**\
Decrease 📉 available copies by 1 (if in stock ✅).

6️⃣ **📥 Return Books**\
Increase 📈 available copies by 1.

---

## 💻 Technology Stack

- 🔙 **Backend**: Flask 🐍 (Python)
- 🎨 **Frontend**: HTML 📄, CSS 🎨, Jinja2 🖌️
- 🗄️ **Database**: CSV 🗃️ for storage
- 🚀 **Deployment**: Render 🌐

---

## 🛠️ Installation and Setup

Follow these steps to ⚙️ run the app locally:

1️⃣ **Clone Repository**

```bash
git clone https://github.com/username/LibraryManagementSystem.git
cd LibraryManagementSystem
```

2️⃣ **Install Dependencies**\
Ensure 🐍 Python is installed, then run:

```bash
 pip install -r requirements.txt
```

3️⃣ **Run Application**

```bash
flask run
```

App available at 🌐 `http://127.0.0.1:5000`

4️⃣ **Access Application**\
Open your 🌍 browser & visit `http://127.0.0.1:5000`.

---

## 🗂️ Project Structure

```
LibrayManagementSystem/
├──  templates/         # 🖌️ HTML templates
│   ├──  index.html     # 🏠 Home page
│   ├──  add_book.html  # ➕ Add book page
│   ├──  remove_book.html # ❌ Remove book page
│   ├──  borrow_book.html # 📤 Borrow book page
│   └──  return_book.html # 📥 Return book page
├──  app.py             # Main Flask app
├──  books.csv          # 📜 CSV data storage
├──  requirements.txt   # 🐍 Python dependencies
└──  README.md          # 📚 Documentation
```

---

## 🔗 Routes and Functionalities

| 🌐 Route  | 🚦 Method   | 📃 Description                      |
| --------- | ----------- | ----------------------------------- |
| `/`       | 🔄 GET/POST | 🏠 Home page: book listing & search |
| `/add`    | 🔄 GET/POST | ➕ Add new 📚                        |
| `/remove` | 🔄 GET/POST | ❌ Remove 📚                         |
| `/borrow` | 🔄 GET/POST | 📤 Borrow 📚                        |
| `/return` | 🔄 GET/POST | 📥 Return 📚                        |

---

## 🏗️ Usage

### ➕ Adding a Book

1️⃣ Navigate to `/add`.\
2️⃣ Fill in 🆔 ID, 🖋️ Title, 👩‍💻 Author, and 🔢 Copies.\
3️⃣ Submit form to save 📚.

### ❌ Removing a Book

1️⃣ Navigate to `/remove`.\
2️⃣ Enter the 🆔 ID of the 📚 to remove.\
3️⃣ Submit form to delete.

### 📤 Borrowing a Book

1️⃣ Navigate to `/borrow`.\
2️⃣ Input 🆔 ID of the 📚.\
3️⃣ Decreases 📉 count if in stock ✅.

### 📥 Returning a Book

1️⃣ Navigate to `/return`.\
2️⃣ Enter 🆔 ID of 📚.\
3️⃣ Increases 📈 count.

### 🔎 Searching for Books

1️⃣ Use 🔤 search bar 🏠 on home page.\
2️⃣ Enter 📘 Title or 👤 Author.

---

## 🚀 Deployment

Steps for Render deployment 🌐:

1️⃣ **Install Gunicorn**\
Add to `requirements.txt`:

```bash
 gunicorn app:app --bind 0.0.0.0:$PORT
```

2️⃣ **Setup Render**

- Add repo to Render.
- Build command:

```bash
pip install -r requirements.txt
```

- Start command:

```bash
gunicorn app:app --bind 0.0.0.0:$PORT
```

3️⃣ **Environment Variables**

- 🔢 `PORT`: Auto-set by Render.

---

## 🔮 Future Enhancements

- 🛠️ Migrate CSV to relational DB 🗄️ (SQLite/PostgreSQL).
- 🔑 Add user authentication 🔒.
- 📜 Logging for debugging 🐞.
- 🔢 Pagination 📖 for books.
- 🌐 Build REST API 🌍.

---

## 🤝 Contribution

💡 Contributions welcome! Follow these steps:
1️⃣ Fork 🍴 repo.\
2️⃣ Create branch (`git checkout -b feature-name`).\
3️⃣ Commit changes (`git commit -m 'Add feature'`).\
4️⃣ Push changes (`git push origin feature-name`).\
5️⃣ Create PR 📩.



---

## 📬 Contact

For 📩 support:

- **👤 Name**: Rahul Jadhav
- **📧 Email**: [rahuljadhav0417@gmail.com](mailto\:rahuljadhav0417@gmail.com)
- **🌐 Project URL**: [Library Management System](https://library-management-9kzq.onrender.com)

