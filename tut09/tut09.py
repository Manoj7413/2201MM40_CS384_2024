import pandas as pd

att_timing = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Csv_data/input_attendance.csv")

att_timing.sample(5)

att_timing.shape

att_timing['Timestamp'] = pd.to_datetime(att_timing['Timestamp'], dayfirst=True)

att_timing.info()

att_timing.sample(5)

att_timing['date_data'] = att_timing['Timestamp'].dt.date
att_timing['time_data'] = att_timing['Timestamp'].dt.time

att_timing.sample(3)

att_timing.drop('Timestamp', axis=1, inplace=True)
att_timing.head()

att_timing_sorted = att_timing.sort_values(by='date_data', ascending=True)

att_timing_sorted.head(5)

att_timing['date_data'] = pd.to_datetime(att_timing['date_data'], dayfirst=True)

att_timing['time_data'] = pd.to_datetime(att_timing['time_data'], format='%H:%M:%S')

att_timing.head()

import re
import ast

# Read the file
with open("/content/drive/MyDrive/Colab Notebooks/Csv_data/python dates.txt", "r") as file:
    data = file.read()

# Extract dates using regex
dates = re.findall(r'\d{2}/\d{2}/\d{4}', data)
classes_taken_dates = []

# Process each line as a string
for line in data.splitlines():
    line = line.strip()  # Remove leading/trailing whitespace
    if line.startswith('classes_taken_dates'):
        # Evaluate the list safely using ast.literal_eval
        classes_taken_dates = ast.literal_eval(line.split('=')[1].strip())

dates

from datetime import datetime

dates = pd.Series(dates)
dates = pd.to_datetime(dates, format='%d/%m/%Y', dayfirst=True)
dates = dates.sort_values()
dates = dates.dt.strftime('%d/%m/%Y')

dates

with open('/content/drive/MyDrive/Colab Notebooks/Csv_data/stud_list.txt', 'r') as file:
    stud = file.readlines()

students = []
for name in stud:
  name = name.strip()
  students.append(name)

students[:5]

from datetime import datetime

dates_sorted = sorted([datetime.strptime(date, "%d/%m/%Y") for date in dates])
dates_sorted_str = [date.strftime("%d/%m/%Y") for date in dates_sorted]

# Create the DataFrame
final_attendance_data = pd.DataFrame(columns=['Students'])

# Add each sorted date as a column with default value 0
for date in dates_sorted_str:
    final_attendance_data[date] = 0

final_attendance_data

final_attendance_data['Students'] = students

final_attendance_data.fillna(0, inplace=True)
numeric_cols = final_attendance_data.select_dtypes(include='number').columns
final_attendance_data[numeric_cols] = final_attendance_data[numeric_cols].astype(int)
final_attendance_data.head()

final_attendance_data['Allowed_Attendance'] = len(classes_taken_dates)*2
final_attendance_data['Marked_By_Students'] = 0
final_attendance_data['Proxy_By_students'] = 0
final_attendance_data['Actual_Attendance'] = 0



Make_color = pd.DataFrame('', index=final_attendance_data.index, columns=final_attendance_data.columns)

for index, row in att_timing.iterrows():
  name = row['Roll']
  for index1, row1 in final_attendance_data.iterrows():
    if name == row1['Students']:
      date = row['date_data']
      time = row['time_data'].time()
      dates = pd.to_datetime(dates, dayfirst=True)
      if date in dates.values:
        if time >= pd.to_datetime("18:00:00").time() and time <= pd.to_datetime("20:00:00").time():
          final_attendance_data.at[index1, date.strftime('%d/%m/%Y')] += 1
          final_attendance_data.at[index1, 'Marked_By_Students'] += 1
          final_attendance_data.at[index1, 'Actual_Attendance'] += 1

          if Make_color.at[index1, date.strftime('%d/%m/%Y')] != 'background-color: rgba(255, 0, 0, 0.5)':
            if final_attendance_data.at[index1, date.strftime('%d/%m/%Y')] == 1:
                Make_color.at[index1, date.strftime('%d/%m/%Y')] = 'background-color: rgba(255, 255, 0, 0.5)'  # Yellow
            elif final_attendance_data.at[index1, date.strftime('%d/%m/%Y')] == 2:
                Make_color.at[index1, date.strftime('%d/%m/%Y')] = 'background-color: rgba(0, 255, 0, 0.5)'  # Green
            elif final_attendance_data.at[index1, date.strftime('%d/%m/%Y')] >= 3:
                Make_color.at[index1, date.strftime('%d/%m/%Y')] = 'background-color: rgba(255, 0, 0, 0.5)'  # Red
                final_attendance_data.at[index1, 'Proxy_By_students'] += 1
                final_attendance_data.at[index1, 'Actual_Attendance'] -= 1

          else:
            final_attendance_data.at[index1, 'Proxy_By_students'] += 1
            if final_attendance_data.at[index1, date.strftime('%d/%m/%Y')] >= 3:
              final_attendance_data.at[index1, 'Actual_Attendance'] -= 1

        else:
          final_attendance_data.at[index1, date.strftime('%d/%m/%Y')] += 1 #and make it red
          final_attendance_data.at[index1, 'Proxy_By_students'] += 1
          final_attendance_data.at[index1, 'Marked_By_Students'] += 1
          Make_color.at[index1, date.strftime('%d/%m/%Y')] = 'background-color: rgba(255, 0, 0, 0.5)'

      else:
        final_attendance_data.at[index1, 'Proxy_By_students'] += 1
        final_attendance_data.at[index1, 'Marked_By_Students'] += 1

output_excel = final_attendance_data.style.apply(lambda x: Make_color, axis=None)
output_excel

final_attendance_data.to_excel('output_excel.xlsx', index=False)
from google.colab import files
files.download('output_excel.xlsx')