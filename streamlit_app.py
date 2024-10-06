# Streamlit app for Swipe Authentication Project
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import os

# Set up the page
st.set_page_config(page_title="SwipeGuard: Swipe Authentication", layout="wide")

# Sidebar for navigation
st.sidebar.title("SwipeGuard Project")
st.sidebar.header("Menu")
page = st.sidebar.selectbox("Choose a section", ["Project Overview", "Data", "Clustering Demo", "Security System"])

# Project Overview Section
if page == "Project Overview":
    st.title("SwipeGuard: Swipe-Based Phone Authentication")
    st.markdown("""
    **Project Goal:** Create a system to classify phone users based on swipe data and secure the device from non-users.
    
    **Problem Statement:** Many security breaches occur due to unauthorized access, especially on mobile devices. Our project aims to build an ML model that differentiates between the user and non-user based on swipe patterns.
    
    **Key Features:**
    - Swipe coordinates (X, Y)
    - Timestamps
    - Unique swipe IDs
    
    **Questions We Asked:**
    1. How do we get the swipe and touch data?
    2. Which metrics can we calculate?
    3. How can we create a system to recognize user vs non-user?
    4. How do we take action based on the system's result?
    """)

# Data Section
if page == "Data":
    st.title("Swipe Data")
    st.markdown("""
    We collected swipe data from our devices using Android Debug Bridge (ADB). The raw data was cleaned and prepared for machine learning by removing missing values and sorting by swipe_id and timestamp.
    """)

    # Load sample data and clean it
    file_path = 'sample_swipe_data.csv'  # Change this to your actual file path
    expected_columns = 5  # Set this to the expected number of columns in your CSV
    
    try:
        # Read the CSV file
        data = pd.read_csv(file_path)

        # Check the initial shape of the DataFrame
        st.write(f"Initial data shape: {data.shape}")

        # Remove rows with broken lines (i.e., rows that do not have the expected number of columns)
        cleaned_data = data.dropna(thresh=expected_columns, axis=0)

        # Check the shape after cleaning
        st.write(f"Cleaned data shape: {cleaned_data.shape}")

        # Display cleaned data
        st.dataframe(cleaned_data.head())
        
        # Save cleaned data to a new CSV file (optional)
        cleaned_data.to_csv('cleaned_sample_swipe_data.csv', index=False)
        st.success("Cleaned data saved to 'cleaned_sample_swipe_data.csv'")

    except Exception as e:
        st.error(f"An error occurred: {e}")

    st.markdown("""
    **Key Data Columns:**
    - `x_coordinate`: The X position of the swipe.
    - `y_coordinate`: The Y position of the swipe.
    - `timestamp`: The time the swipe was made.
    - `swipe_id`: A unique ID to track each swipe session.
    """)

# Clustering Demo Section
if page == "Clustering Demo":
    st.title("Swipe Classification Demo")
    
    st.markdown("Using K-Means clustering to classify swipes into two categories: user and non-user.")
    
    # Load and preprocess the data
    data = pd.read_csv('cleaned_sample_swipe_data.csv')  # Use cleaned data
    data['timestamp'] = pd.to_numeric(data['timestamp'], errors='coerce')
    data = data.dropna(subset=['x_coordinate', 'y_coordinate', 'timestamp', 'swipe_id'])
    data = data.sort_values(by=['swipe_id', 'timestamp'])
    
    # Calculate offsets and time differences
    starting_points = data.groupby('swipe_id').agg({
        'x_coordinate': 'first',
        'y_coordinate': 'first'
    }).reset_index().rename(columns={'x_coordinate': 'start_x', 'y_coordinate': 'start_y'})
    data = data.merge(starting_points, on='swipe_id', how='left')
    data['x_offset'] = data['x_coordinate'] - data['start_x']
    data['y_offset'] = data['y_coordinate'] - data['start_y']
    data['time_diff'] = data.groupby('swipe_id')['timestamp'].diff().fillna(0)

    # Prepare features
    features = data[['x_offset', 'y_offset', 'time_diff', 'x_coordinate', 'y_coordinate']]
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # Apply K-Means clustering
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(features_scaled)
    data['cluster'] = kmeans.labels_

    # Display scatter plot
    st.subheader("Swipe Pattern Clustering")
    fig, ax = plt.subplots(figsize=(10, 6))
    scatter = ax.scatter(data['x_coordinate'], data['y_coordinate'], c=data['cluster'], cmap='viridis', alpha=0.5)
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('K-Means Clustering of Swipe Data')
    st.pyplot(fig)
    
    # Display cluster centers (if needed)
    st.write("Cluster Centers (Swipe Patterns):", kmeans.cluster_centers_)

    # Cluster analysis
    user_cluster_percentage = np.mean(data['cluster'] == 0) * 100
    st.write(f"Approximate percentage of swipes classified as User: {user_cluster_percentage:.2f}%")

# Security System Section
if page == "Security System":
    data = pd.read_csv('cleaned_sample_swipe_data.csv')  # Use cleaned data
    data['timestamp'] = pd.to_numeric(data['timestamp'], errors='coerce')
    data = data.dropna(subset=['x_coordinate', 'y_coordinate', 'timestamp', 'swipe_id'])
    data = data.sort_values(by=['swipe_id', 'timestamp'])
    
    # Calculate offsets and time differences
    starting_points = data.groupby('swipe_id').agg({
        'x_coordinate': 'first',
        'y_coordinate': 'first'
    }).reset_index().rename(columns={'x_coordinate': 'start_x', 'y_coordinate': 'start_y'})
    data = data.merge(starting_points, on='swipe_id', how='left')
    data['x_offset'] = data['x_coordinate'] - data['start_x']
    data['y_offset'] = data['y_coordinate'] - data['start_y']
    data['time_diff'] = data.groupby('swipe_id')['timestamp'].diff().fillna(0)

    # Prepare features
    features = data[['x_offset', 'y_offset', 'time_diff', 'x_coordinate', 'y_coordinate']]
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # Apply K-Means clustering
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(features_scaled)
    data['cluster'] = kmeans.labels_

    st.title("Real-Time Security System")
    st.markdown("""
    The system monitors swipe patterns and checks if at least 75% of the last 20 swipes match the user’s swipe type.
    
    If swipes don't match, the system returns `False`, triggering potential security actions such as locking the phone or alerting the user.
    """)
    
    # Mocking the last 20 swipes accuracy check
    last_20_swipes = data.tail(20)
    user_swipes = (last_20_swipes['cluster'] == 0).sum()
    accuracy = user_swipes / 20
    
    st.write(f"Last 20 swipes accuracy: {accuracy * 100:.2f}%")
    
    if accuracy >= 0.75:
        st.success("User swipes detected: Phone is secure!")
    else:
        st.error("Non-user swipes detected: Take security action!")
        os.system('./lock')

# Footer
st.sidebar.markdown("### Created by SwipeGuard Team")