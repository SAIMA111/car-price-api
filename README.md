# Car Price Prediction Web App

This is a full-stack machine learning project that predicts car prices based on engine performance, fuel efficiency, and age.

---

## Live Demo

**Live App (Frontend):** https://eloquent-tiramisu-6aea7b.netlify.app/
  
**API Docs (Backend):** https://car-price-api-0erc.onrender.com/docs  

---

## Features

- Predict car price based on user input  
- Clean and user-friendly interface  
- Real-time predictions using deployed API  
- Full-stack integration (Frontend + Backend + ML model)  

---

## Tech Stack

- **Python** (NumPy, Pandas)  
- **Machine Learning:** Linear Regression  
- **FastAPI** (Backend API)  
- **HTML, CSS, JavaScript** (Frontend)  
- **Render** (Backend Deployment)  
- **Netlify** (Frontend Deployment)  

---

## How it works

1. User enters car details (year, HP, MPG, etc.)  
2. Frontend sends request to FastAPI backend  
3. Backend processes input using trained ML model  
4. Returns predicted price  
5. UI displays result instantly  

---

## 🚀 Run Locally

```bash
pip install -r requirements.txt
py -m uvicorn main:app --reload

```

Then open:

http://127.0.0.1:8000/docs

Frontend can be opened by running index.html in a browser.

