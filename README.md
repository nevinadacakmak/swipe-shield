[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blank-app-template.streamlit.app/)

# SwipeShield: A Swipe-Based User Verification System

## Overview

SwipeShield is a swipe-based user verification system that utilizes machine learning to classify swipe patterns and determine whether a user is authorized to access a device. This project employs clustering algorithms to analyze swipe data, enhancing security on mobile devices.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Data Requirements](#data-requirements)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- Upload swipe data in CSV format and visualize swipe patterns.
- Analyze the last 20 swipes to determine user authenticity based on machine learning classification.
- Display clustered swipe data with a clear visualization.
- Download processed clustered swipe data.

## Installation

To run the SwipeShield app locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/swipe-shield.git
   cd swipe-shield

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```

Here's a single comprehensive Markdown file for your README, structured and formatted as requested:

2. **Create a Virtual Environment (optional but recommended):**
   ```bash
   python -m venv swipe_env
   source swipe_env/bin/activate  # On Windows use `swipe_env\Scripts\activate`
   ```

3. **Install Required Packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Streamlit App:**
   ```bash
   streamlit run streamlit_app.py
   ```

2. **Access the App:**
   Open your web browser and navigate to `http://localhost:8501`.

3. **Upload Data:**
   Upload your swipe data (`sample_swipe_data.csv`) and clustered swipe data (`clustered_swipe_data.csv`) to analyze swipe patterns.

## How It Works

SwipeShield operates through the following key steps:

1. **Data Acquisition:** Utilize Android Debug Bridge (ADB) to gather swipe data.
2. **Data Cleaning:** Clean and parse swipe data to prepare it for analysis.
3. **Clustering:** Apply K-Means clustering to categorize swipes into user and non-user patterns.
4. **User Verification:** Analyze the last 20 swipes and determine if they align with the user's swipe pattern, using a threshold of 75% accuracy.
5. **Visualization:** Display the results and clustering outcomes through the web app interface.

## Data Requirements

- **Sample Swipe Data:** CSV file with columns:
  - `swipe_id`: Unique identifier for each swipe
  - `x_coordinate`: X coordinate of the swipe
  - `y_coordinate`: Y coordinate of the swipe
  - `timestamp`: Timestamp of the swipe

- **Clustered Swipe Data:** CSV file with columns:
  - `x_coordinate`: X coordinate of the swipe
  - `y_coordinate`: Y coordinate of the swipe
  - `cluster`: Cluster label (user or non-user)

## How to Add Clustered Data to Your Website

To include clustered data in your website, follow these steps:

1. **Prepare Your CSV File:** Ensure your clustered data is saved in a CSV format and contains the necessary columns.

2. **File Upload:** Implement a file upload feature in your web app using Streamlit's `file_uploader` function. This allows users to upload their clustered swipe data for analysis.

3. **Data Processing:** Read the uploaded CSV file and process it to extract the relevant information for your application.

4. **Visualization:** Use Matplotlib or similar libraries to create visual representations of the clustered data within your web app.

## Contributing

Contributions are welcome! To contribute, please fork the repository and submit a pull request. Make sure to follow the coding guidelines and include tests for new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/) for simplifying web app development.
- [Scikit-learn](https://scikit-learn.org/) for providing essential machine learning tools.
- The community for their support and contributions to the project.

---

## Contact

For any inquiries or support, feel free to reach out:
```

### Instructions:
- Replace `https://github.com/yourusername/swipe-shield.git` with the actual URL of your GitHub repository.
- Modify contact information and any other sections as necessary to fit your project and personal details.
