import streamlit as st  # For creating web interface
import pandas as pd  # For data manipulation
import datetime  # For handling date
import os  # For file operations
import csv  # For reading and writing CSV files

MOOD_FILE = "mood_log.csv"  # Mood log file name

# Function to read mood data from the CSV file
def load_mood_data(): 
    # Check if the file exists
    if not os.path.exists(MOOD_FILE):
        # If no file, create an empty DataFrame with columns
        return pd.DataFrame(columns=["Date", "Mood"])
    
    # Read and return existing mood data 
    return pd.read_csv(MOOD_FILE)

# Function to add new mood entry
def save_mood_data(date, mood):
    # Open file in append mode
    with open(MOOD_FILE, "a") as file:
        # Create CSV writer
        writer = csv.writer(file)
        # Add new mood entry
        writer.writerow([date, mood])

# Streamlit app title
st.title("Mood Tracker")

# Show today's date
today = datetime.date.today()

# Create subheader for mood input
st.subheader("How are you feeling today?")

# Create dropdown for mood selection 
mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Neutral"])

# Create button to save mood 
if st.button("Log Mood"):
    # Save mood when button is clicked
    save_mood_data(today, mood)

    # Show success message 
    st.success("Mood Logged Successfully")

# Load mood data
data = load_mood_data()

# If there is data to display 
if not data.empty:     
    # Create section for visualization
    st.subheader("Mood Trends over Time")

    # Convert date string to datetime object
    data["Date"] = pd.to_datetime(data["Date"])

    # Display frequency of each mood
    mood_counts = data.groupby("Mood").count()["Date"]

    # Display the bar chart
    st.bar_chart(mood_counts)

# Footer
st.write("Built with ✨💖 by [Huzaifa Abdulrab](https://github.com/Huzaifaabdulrab)")
