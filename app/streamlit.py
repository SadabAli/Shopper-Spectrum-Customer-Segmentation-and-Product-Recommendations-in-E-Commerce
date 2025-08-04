import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load models
kmeans = pickle.load(open(r'C:\Users\alisa\OneDrive\Desktop\Shopper-Spectrum-Customer-Segmentation-and-Product-Recommendations-in-E-Commerce\models\kmeans_model.pkl', 'rb'))
scaler = pickle.load(open(r'C:\Users\alisa\OneDrive\Desktop\Shopper-Spectrum-Customer-Segmentation-and-Product-Recommendations-in-E-Commerce\models\rfm_scaler.pkl', 'rb'))
similarity_matrix = pickle.load(open(r'models/item_similarity.pkl', 'rb'))

# Segment label mapping (adjust if your labels are different)
cluster_labels = {
    0: 'Occasional',
    1: 'Regular',
    2: 'High-Value',
    3: 'At-Risk'
}

# Set Streamlit Page Config
st.set_page_config(page_title="🛍 Shopper Spectrum", layout="centered")

# Sidebar Navigation
page = st.sidebar.selectbox("Choose a Module", ["Product Recommender", "Customer Segmentation"])

# --------------------  Module 1: Product Recommendation --------------------
if page == "Product Recommender":
    st.title(" Product Recommendation System")
    st.write(" Enter a product name to get 5 similar products.")

    product_list = list(similarity_matrix.columns)
    selected_product = st.selectbox("Choose a product", product_list)

    if st.button("Get Recommendations"):
        with st.spinner("Finding similar products..."):
            if selected_product in similarity_matrix:
                similar_items = similarity_matrix[selected_product].sort_values(ascending=False)[1:6]
                st.success(" Recommended Products:")
                for i, item in enumerate(similar_items.index, 1):
                    st.markdown(f"**{i}.** {item}")
            else:
                st.warning("Product not found!")

# --------------------  Module 2: Customer Segmentation --------------------
elif page == "Customer Segmentation":
    st.title(" Customer Segmentation")
    st.write(" Input RFM values to get customer segment.")

    recency = st.number_input(" Recency (days since last purchase)", min_value=0, max_value=1000, value=100)
    frequency = st.number_input(" Frequency (total purchases)", min_value=1, max_value=100, value=5)
    monetary = st.number_input(" Monetary (total spend)", min_value=1.0, value=200.0, step=10.0)

    if st.button("Predict Cluster"):
        with st.spinner("Predicting customer segment..."):
            input_data = scaler.transform([[recency, frequency, monetary]])
            cluster = kmeans.predict(input_data)[0]
            segment = cluster_labels.get(cluster, "Unknown")
            st.success(f" Predicted Segment: **{segment}**")
