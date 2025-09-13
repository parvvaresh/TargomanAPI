# 🐍 Python Translator with CI/CD 🚀

This project is a simple **Python translator client** for the [Targoman API](https://targoman.ir), fully containerized with Docker and tested automatically using **GitHub Actions (CI/CD)**.

---

## 📂 Project Structure
- `api.py` → Main code for translation  
- `test_translate.py` → Unit tests (with pytest & mock)  
- `Dockerfile` → Container setup  
- `.github/workflows/ci.yml` → CI/CD pipeline  

---

## ⚡ Features
- ✅ Translation (fa → en / en → fa)  
- ✅ Unit tests with `pytest`  
- ✅ Linting with `flake8`  
- ✅ Dockerized environment  
- ✅ GitHub Actions CI/CD  

---

## 🔧 Run Locally

```bash
# Create venv
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest -v
