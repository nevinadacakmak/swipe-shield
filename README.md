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
