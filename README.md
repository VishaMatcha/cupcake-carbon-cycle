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
