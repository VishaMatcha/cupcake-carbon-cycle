# CupCake Carbon Cycle Model - README

## **Overview**
The **CupCake Carbon Cycle Model** is a full-stack web application designed to track and visualize carbon cycles across ecosystems. It provides researchers with real-time data visualization of carbon emissions, helping analyze the impact on climate change.

## **Features**
- **Real-time data tracking** of carbon cycles.
- **Graphical representation** using interactive charts.
- **RESTful API** for backend data processing.
- **Cloud deployment** with free-tier hosting solutions.

## **Tech Stack**
- **Frontend:** React, Chart.js, Axios
- **Backend:** Flask (Python), Flask-CORS, Flask-SQLAlchemy
- **Database:** PostgreSQL
- **Deployment:** Render (Backend), Vercel (Frontend)

---

## **1. Prerequisites**
Ensure the following software is installed on your system:
- **Git**: `brew install git`
- **Node.js & npm**: `brew install node`
- **Python (3.x) & pip**: `brew install python`
- **PostgreSQL**: `brew install postgresql`
- **Vercel CLI** (for frontend deployment): `npm install -g vercel`

---

## **2. Project Setup**

### **Step 1: Clone the Repository**
```sh
git clone https://github.com/your-username/cupcake-carbon-cycle.git
cd cupcake-carbon-cycle
```
---

## **3. Backend Setup (Flask + PostgreSQL)**

### **Step 2: Set Up Python Virtual Environment**
```sh
cd backend
python3 -m venv venv
source venv/bin/activate
```

### **Step 3: Install Dependencies**
```sh
pip install flask flask-cors flask-sqlalchemy psycopg2 gunicorn
pip freeze > requirements.txt
```


### **Step 4: Set Up PostgreSQL Database**
```sh
psql postgres
CREATE DATABASE carbon_cycle;
CREATE USER admin WITH ENCRYPTED PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE carbon_cycle TO admin;
```

### **Step 5: Run the Backend**
```sh
python app.py
```
Test API:
```sh
curl http://127.0.0.1:5000/data
```
---

## **4. Frontend Setup (React)**

### **Step 6: Set Up React App**
```sh
cd ../frontend
npx create-react-app .
npm install axios chart.js react-chartjs-2
```

### **Step 7: Run Frontend Locally**
```sh
npm start
```
---
## **5. Deployment**

### **Step 8: Deploy Backend to Render**
1. Go to **[Render](https://render.com/)** > **New Web Service**
2. Connect your **GitHub repository**
3. Set **Root Directory** to `backend/`
4. **Build Command:**
   ```sh
   pip install -r requirements.txt
   ```
5. **Start Command:**
   ```sh
   gunicorn app:app
   ```
6. Deploy and get the **Render backend URL** (e.g., `https://your-backend-service.onrender.com`)

---

### **Step 9: Deploy Frontend to Vercel**
1. Install **Vercel CLI** (if not installed):
   ```sh
   npm install -g vercel
   ```
2. Build the frontend:
   ```sh
   npm run build
   ```
3. Deploy to Vercel:
   ```sh
   vercel
   ```
4. Get the **Vercel frontend URL** (e.g., `https://your-frontend.vercel.app`)

---

## **6. Testing & Verification**
- Open **Frontend URL**: `https://your-frontend.vercel.app`
- Ensure **data loads correctly from the backend**.
- Use **Developer Console (F12)** → **Network Tab** to debug API calls.
- If issues persist, **check Render logs** under `Logs` tab.

---

## **7. Final Summary**
### ✅ **Local Development**
```sh
# Run Backend
cd backend && python app.py

# Run Frontend
cd frontend && npm start
```

### ✅ **Deployment**
- **Backend** → Render (`https://your-backend-service.onrender.com`)
- **Frontend** → Vercel (`https://your-frontend.vercel.app`)

🚀 **Congratulations! Your CupCake Carbon Cycle Model is live!** 🎉
