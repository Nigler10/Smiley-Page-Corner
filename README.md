***1️⃣ Clone the repo***
```cmd
git clone <https://github.com/Nigler10/Smiley-Page-Corner>
cd "Smiley Page Corner\Project"
```

***2️⃣ Set up Python environment***

:: 🔹 Create virtual environment
```cmd
python -m venv .venv
```

:: 🔹 Activate virtual environment
```cmd
.venv\Scripts\activate.bat
```

:: 🔹 Install Python dependencies
```cmd
pip install -r requirements.txt
Python version: 3.13.5
```

***3️⃣ Verify Node + npm***

:: 🔹 Check Node.js version
```cmd
node -v
```

:: Should be v20.15.0

:: 🔹 Check npm version
```cmd
npm -v
```

***4️⃣ Install Tailwind + DaisyUI packages***

:: 🔹 From the Project folder (where package.json lives)
```cmd
npm install -D tailwindcss@3.4.18 daisyui@4.12.24 autoprefixer@10.4.22 postcss@8.5.6 postcss-cli@11.0.1
```
**Versions are exact to ensure DaisyUI works correctly.**

***5️⃣ Build Tailwind + DaisyUI CSS***

:: 🔹 Build and watch CSS
```cmd
npx tailwindcss -i ./tailwind/input.css -o ./static/css/output.css --watch
```
**Keep this CMD window open during development**

Rebuilds automatically when input.css or templates change

***6️⃣ Run Django server***

:: 🔹 Make migrations (first time only)
```cmd
python manage.py makemigrations
python manage.py migrate
```

:: 🔹 Run server
```cmd
python manage.py runserver
```

***Open browser → http://127.0.0.1:8000/***

***Tailwind + DaisyUI should now work perfectly***

