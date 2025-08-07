#  Shopper Spectrum: Customer Segmentation & Product Recommendation

This project analyzes customer purchasing behavior using **RFM (Recency, Frequency, Monetary) analysis** and builds a **product recommendation system** using **Collaborative Filtering**. Deployed via an interactive **Streamlit** web app.

---

##  Features

###  1. Customer Segmentation (RFM)
- Users input Recency, Frequency, and Monetary values.
- Predicts which **segment** the customer belongs to:
  - **High-Value**
  - **Regular**
  - **Occasional**
  - **At-Risk**

###  2. Product Recommendation
- Input a product name.
- Recommends **5 similar products** using **item-item collaborative filtering**.

---

##  Tech Stack

- **Python**
- **Pandas**, **NumPy**
- **Scikit-learn**
- **Joblib**
- **Streamlit**

---

##  Getting Started

### 1️ Clone the repo
```bash
git clone https://github.com/your-username/shopper-spectrum.git
cd shopper-spectrum
```
### Install dependencies
```
pip install -r requirements.txt
```

### Run the Streamlit app
```
streamlit run app.py
```
## RFM Segments (Based on Clustering)

| Cluster ID | Characteristics        | Label      |
| ---------- | ---------------------- | ---------- |
| 0          | High R, High F, High M | High-Value |
| 1          | Medium F, Medium M     | Regular    |
| 2          | Low F, Low M, older R  | Occasional |
| 3          | High R, Low F, Low M   | At-Risk    |


## Screenshots
<img width="1992" height="1060" alt="Screenshot 2025-08-05 012215" src="https://github.com/user-attachments/assets/587b091f-c355-4ff3-9b06-1e11ab0f40b7" />
<img width="1990" height="1062" alt="Screenshot 2025-08-05 012242" src="https://github.com/user-attachments/assets/7d2c1cf4-5b1a-4b9b-899a-65cd5a60a853" />



## Acknowledgements
- Inspired by real-world e-commerce customer analytics

- Built with ❤️ for learning and experimentation
