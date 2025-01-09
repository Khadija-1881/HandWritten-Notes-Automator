import streamlit as st
from PIL import Image
import pandas as pd
from process_image import (
    process_image_gemini_2_A,
    process_image_gemini_2_B,
    process_image_gemini_2_C,
    process_image_gemini_2_D,
    process_image_gemini_2_E,
)

# Function to process the image based on selected model
def process_image(selected_model, image, file_name):
    if selected_model == 'Form_E':
        return process_image_gemini_2_E(image, file_name)
    elif selected_model == 'Form_D':
        return process_image_gemini_2_D(image, file_name)
    elif selected_model == 'Form_C':
        return process_image_gemini_2_C(image, file_name)
    elif selected_model == 'Form_B':
        return process_image_gemini_2_B(image, file_name)
    elif selected_model == 'Form_A':
        return process_image_gemini_2_A(image, file_name)

# Streamlit app configuration
st.set_page_config(
    page_title="Automatic Data Entry Module",
    page_icon="📄",
    layout="centered",
)

# Custom CSS for aesthetics
st.markdown(
    """
    <style>
        .main {
            background-color: black;
        }
        .stButton button {
            background-color: #0073e6;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
        }
        .stButton button:hover {
            background-color: #005bb5;
        }
        .block-container {
            padding-top: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and description
st.title("📄 Automatic Data Entry Module")
st.markdown("Upload an image to extract structured data into DataFrames.")

# Initial file upload section
uploaded_file = st.file_uploader(
    "Upload an image file (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"]
)

if uploaded_file:
    # Show loading spinner while processing
    with st.spinner("Uploading and processing the file..."):
        # Save the uploaded file temporarily
        file_name = uploaded_file.name
        image = Image.open(uploaded_file)

        # Show form selection only after file upload
        st.subheader("Select the Form Type")
        form_options = ["Form_A", "Form_B", "Form_C", "Form_D", "Form_E"]
        selected_model = st.radio(
            "Choose a form type to extract the data:", form_options, horizontal=True
        )

        # Process the image when a form type is selected
        if selected_model:
            st.subheader("Processing Results")
            try:
                if selected_model == "Form_A":
                    df1, df2, df3, df4, df5 = process_image(
                        selected_model, image, file_name
                    )
                    dataframes = {
                        "OUTREACH CLINIC DATA": df1,
                        "OUTREACH CLINIC INFORMATION": df2,
                        "Total Patients": df3,
                        "Money Collected": df4,
                        "Money Distributed": df5,
                    }
                elif selected_model == "Form_B":
                    df1, df2, df3, df4, df5, df6, df7, df8, df9 = process_image(
                        selected_model, image, file_name
                    )
                    dataframes = {
                        "OUTREACH CLINIC DATA": df1,
                        "OUTREACH CLINIC INFORMATION": df2,
                        "Service Offered": df3,
                        "Impacted Services": df4,
                        "ART Data": df5,
                        "Patients Duration": df6,
                        "Patients Receiving ART": df7,
                        "New Patients Linked": df8,
                        "Viral Load Samples": df9,
                    }
                elif selected_model == "Form_C":
                    df1, df2, df3, df4 = process_image(selected_model, image, file_name)
                    dataframes = {
                        "OUTREACH CLINIC DATA": df1,
                        "Other Services": df2,
                        "Field 3": df3,
                        "Field 4": df4,
                    }
                elif selected_model == "Form_D":
                    df1, df2, df3, df4 = process_image(selected_model, image, file_name)
                    dataframes = {
                        "OUTREACH CLINIC DATA": df1,
                        "HIV COUNSELING AND TESTING": df2,
                        "New Positives": df3,
                        "Patients Tested for First Time": df4,
                    }
                elif selected_model == "Form_E":
                    df1, df2, df3, df4 = process_image(selected_model, image, file_name)
                    dataframes = {
                        "OUTREACH CLINIC DATA": df1,
                        "Family Planning & Maternal Health": df2,
                        "Perinatal Health": df3,
                        "COVID-19 Vaccinations": df4,
                    }

                # Display DataFrames
                st.success("Data extraction complete! Here are the results:")
                for title, df in dataframes.items():
                    st.subheader(title)
                    st.dataframe(df)

            except Exception as e:
                st.error(f"An error occurred: {e}")

else:
    st.info("Upload an image file to begin.")