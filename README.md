# Mood Tracker

## Overview
Mood Tracker is a simple web-based application built using **Streamlit** and **Pandas**. It allows users to log their daily mood and visualize mood trends over time using a bar chart. The data is stored in a CSV file for easy tracking and analysis.

## Features
- Select and log your mood (Happy, Sad, Angry, Neutral)
- Store mood logs in a CSV file
- Visualize mood trends over time with a bar chart
- Simple and interactive UI powered by Streamlit

## Installation & Setup
### Prerequisites
Ensure you have **uv** installed. If not, install it using:
```sh
pip install uv
```

### Clone the Repository
```sh
git clone https://github.com/Huzaifaabdulrab/Mood_Tracker.git
cd Mood_Tracker
```

### Create a Virtual Environment
```sh
uv venv .venv
```

### Activate the Virtual Environment
- **Windows:**
  ```sh
  .venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```sh
  source .venv/bin/activate
  ```

### Install Dependencies
```sh
uv pip install -r requirements.txt
```

## Usage
Run the Mood Tracker application using the following command:
```sh
streamlit run main.py
```

This will start a local server, and you can access the app in your browser.

## File Structure
```
Mood_Tracker/
│-- main.py  # Main application file
│-- mood_log.csv  # Stores mood data
│-- requirements.txt  # Project dependencies
│-- .venv/  # Virtual environment
```

## Contributing
If you want to improve this project, feel free to fork the repository and submit a pull request.

## Author
Developed by **Huzaifa Abdulrab**

## License
This project is open-source and available under the MIT License.

## Connect with Me
🔗 [GitHub](https://github.com/Huzaifaabdulrab)

📱 [LinkedIn](https://www.linkedin.com/in/huzaifaabdulrab/)