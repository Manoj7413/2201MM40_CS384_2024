import streamlit as st
import pandas as pd
import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

st.title("File Upload Example")
stud_grade1 = st.file_uploader("Choose file")

st.sidebar.title("Check your result")
option = st.sidebar.radio("Select", ["student_det", "student_grade", "grading_system"])

try:
    if stud_grade1 is not None:
        try:
            # Reading the uploaded file
            stud_grade = pd.read_excel(stud_grade1)
            logging.info("File successfully uploaded and read.")
        except Exception as e:
            logging.error(f"Error reading the uploaded file: {e}")
            st.error("Error reading the uploaded file. Please upload a valid Excel file.")
            st.stop()

        # Adding columns
        stud_grade['total_marks'] = '0'
        stud_grade['grade'] = ' '
        logging.debug("Added 'total_marks' and 'grade' columns.")

        # Calculating total marks
        for i in range(2, len(stud_grade)):
            try:
                total_mark = (
                    (stud_grade['Mid Sem'][i] * stud_grade['Mid Sem'][1]) / stud_grade['Mid Sem'][0] +
                    (stud_grade['Endsem'][i] * stud_grade['Endsem'][1]) / stud_grade['Endsem'][0] +
                    (stud_grade['Quiz 1'][i] * stud_grade['Quiz 1'][1]) / stud_grade['Quiz 1'][0] +
                    (stud_grade['Quiz 2'][i] * stud_grade['Quiz 2'][1]) / stud_grade['Quiz 2'][0]
                )
                stud_grade.at[i, 'total_marks'] = round(total_mark, 3)
            except Exception as e:
                logging.error(f"Error calculating total marks for row {i}: {e}")

        # Setting initial values for total_marks and Name
        stud_grade.at[0, 'total_marks'] = ' '
        stud_grade.at[1, 'total_marks'] = ' '
        stud_grade.at[0, 'Name'] = ' '
        stud_grade.at[1, 'Name'] = ' '
        logging.debug("Initial values set for 'total_marks' and 'Name'.")

        # Grading system dataframe
        grading_sys = {
            'grade': ['AA', 'AB', 'BB', 'BC', 'CC', 'CD', 'DD', 'F', 'I', 'PP', 'NP'],
            'old iapc reco': ['5', '15', '25', '30', '15', '5', '5', '0', '0', '0', '0'],
            'Counts': [' ' for _ in range(11)],
            'Round': [' ' for _ in range(11)],
            'Count verified': [' ' for _ in range(11)]
        }

        df = pd.DataFrame(grading_sys)
        df['old iapc reco'] = pd.to_numeric(df['old iapc reco'])
        df['Counts'] = 102 * df['old iapc reco'] / 100
        df['Round'] = df['Counts'].round(0)
        logging.debug("Grading system dataframe created.")

        # Sorting by total_marks
        stud_grade_before = stud_grade.iloc[:2]
        stud_grade_after = stud_grade.iloc[2:]
        stud_grade_after_sorted = stud_grade_after.sort_values(by='total_marks', ascending=False)
        stud_grade = pd.concat([stud_grade_before, stud_grade_after_sorted], ignore_index=True)

        # Assigning grades
        for i in range(2, len(stud_grade)):
            try:
                if i < 7:
                    stud_grade.at[i, 'grade'] = 'AA'
                elif i < 22:
                    stud_grade.at[i, 'grade'] = 'AB'
                elif i < 48:
                    stud_grade.at[i, 'grade'] = 'BB'
                elif i < 79:
                    stud_grade.at[i, 'grade'] = 'BC'
                elif i < 94:
                    stud_grade.at[i, 'grade'] = 'CC'
                elif i < 99:
                    stud_grade.at[i, 'grade'] = 'CD'
                elif i < 104:
                    stud_grade.at[i, 'grade'] = 'DD'
            except Exception as e:
                logging.error(f"Error assigning grade for row {i}: {e}")

        # Sorting by Roll
        stud_grade_before = stud_grade.iloc[:2]
        stud_grade_after = stud_grade.iloc[2:]
        stud_grade_after_sorted = stud_grade_after.sort_values(by='Roll', ascending=True)
        stud_grade = pd.concat([stud_grade_before, stud_grade_after_sorted], ignore_index=True)
        logging.info("Grades assigned and data sorted by Roll.")

        # Updating grade counts
        for idx, grade in enumerate(['AA', 'AB', 'BB', 'BC', 'CC', 'CD', 'DD', 'F', 'I', 'PP', 'NP']):
            df.at[idx, 'Count verified'] = stud_grade['grade'].value_counts().get(grade, 0)

        # Sidebar functionality
        if option == "student_det":
            vip = st.button("View Input")
            if vip:
                st.write(pd.read_excel(stud_grade1))

        elif option == "student_grade":
            vip1 = st.button("Generate Output")
            if vip1:
                st.write(stud_grade)

        elif option == "grading_system":
            st.write(df)

except Exception as e:
    logging.critical(f"An unexpected error occurred: {e}")
    st.error("An unexpected error occurred. Please check the logs for more details.")
