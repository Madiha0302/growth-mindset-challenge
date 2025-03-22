import streamlit as st
import datetime as datetime
import os

# Function to save data 
def save_submission(data):
    try:
        df=pd.read_csv("submissions.csv")
    except FileNotFoundError: 
        df=pd.DataFrame(columns=["Name","Email","Phone","Position","Resume","Date"])
        
        df=df.append(data,ignore_index=True)
        df.to_csv("submissions.csv",index=False)

#Streamlit UI
st.title("Job Submission Form")

# User Inputs
name = st.text_input("Full Name")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number")
address = st.text_input("Address")
region = st.selectbox("Region",["islam","hindu","christian","sikh","other"])
position = st.selectbox("Position Applied For",["Software Engineer", "Data Scientist" , "Designer", "Product Manager"])
age = st.selectbox("Age",["18-25","25-35","35-45","45+"])
experience = st.selectbox("Experience",["0-1 years","1-3 years","3-5 years","5+ years"])
skill = st.text_area("Skills,[skill1,skill2,skill3]")
resume = st.file_uploader("Upload Resume(PDF)",type=["pdf"])
images = st.file_uploader("Upload Image",type=["jpg","jpeg","png"])
submit_date = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")

# Submission Button
if st.button("Submit Application"):
    if name and email and phone and address and region and position and age and experience and skill and resume and images:

        # Save File
        with open(f"resumes/{name.replace(' ', '_')}.pdf") as f:
            f.write(resume.getbuffer())


    UPLOAD_FOLDER = "upload_images"
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

        # File uploader
        upload_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])     
        st.success(f"file uploaded successfully: {upload_file.name}")   

        # Display uploaded images
        images("file_path",captain="Uploaded Image",use_column_width=True)  
      

            # Save to CSV
        submission_data = {"Name":name,"Email":email,"Phone":phone,"Position":position,"Resume":f"resumes/{name.replace(' ', '_')}.pdf","Date":submit_date}
        save_submission(submission_data)

        st.success("Application Submitted Successfully!")

else:  
  st.error("Please fill in all fields and upload a resume")












