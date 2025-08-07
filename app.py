import app as st
import pandas as pd
import pickle
import numpy as np
import os

# -------------------- Load Models --------------------
try:
    kmeans = pickle.load(open(r'C:\Users\alisa\OneDrive\Desktop\Shopper-Spectrum-Customer-Segmentation-and-Product-Recommendations-in-E-Commerce\models\kmeans_model.pkl', 'rb'))
    scaler = pickle.load(open(r'C:\Users\alisa\OneDrive\Desktop\Shopper-Spectrum-Customer-Segmentation-and-Product-Recommendations-in-E-Commerce\models\rfm_scaler.pkl', 'rb'))
    similarity_matrix = pickle.load(open(r'C:\Users\alisa\OneDrive\Desktop\Shopper-Spectrum-Customer-Segmentation-and-Product-Recommendations-in-E-Commerce\models\item_similarity.pkl', 'rb'))
except FileNotFoundError as e:
    st.error(f"Missing file: {e.filename}")
    st.stop()

# Segment Labels
cluster_labels = {
    0: ' Occasional',
    1: ' Regular',
    2: ' High-Value',
    3: ' At-Risk'
}

# -------------------- Streamlit Config --------------------
st.set_page_config(page_title=" Shopper Spectrum", layout="centered")
st.title(" Shopper Spectrum Dashboard")

# Navigation
page = st.sidebar.selectbox("Choose a Module", ["Product Recommender", "Customer Segmentation"])

# -------------------- Module 1: Product Recommender --------------------
if page == "Product Recommender":
    st.header(" Product Recommendation System")
    st.write("Enter a product name to get **5 similar products**.")

    product_list = list(similarity_matrix.columns)
    selected_product = st.selectbox(" Choose a Product", product_list)

    if st.button(" Get Recommendations"):
        with st.spinner("Searching for similar products..."):
            if selected_product in similarity_matrix:
                similar_items = similarity_matrix[selected_product].sort_values(ascending=False)[1:6]
                st.success(" Recommended Products:")
                for i, item in enumerate(similar_items.index, 1):
                    st.markdown(f"**{i}.** {item}")
            else:
                st.warning(" Product not found in similarity matrix.")

# -------------------- Module 2: Customer Segmentation --------------------
elif page == "Customer Segmentation":
    st.header("Customer Segmentation using RFM")
    st.markdown("###  Enter RFM values")

    col1, col2 = st.columns(2)
    with col1:
        recency = st.number_input(" Recency (days since last purchase)", min_value=0, max_value=1000, value=100)
    with col2:
        frequency = st.number_input(" Frequency (number of purchases)", min_value=1, max_value=100, value=5)

    monetary = st.number_input(" Monetary (total spend)", min_value=1.0, value=200.0, step=10.0)

    st.markdown("---")
    if st.button(" Predict Segment"):
        with st.spinner(" Analyzing customer profile..."):
            input_data = scaler.transform([[recency, frequency, monetary]])
            cluster = kmeans.predict(input_data)[0]
            segment = cluster_labels.get(cluster, "Unknown")
            st.success(f" **This customer belongs to:** `{segment} Shopper`")
