from datetime import datetime
start_time = datetime.now()

#Help
def proj_chat_tool():
	pass


###Code

from platform import python_version
ver = python_version()

if ver == "3.8.10":
	print("Correct Version Installed")
else:
	print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


proj_chat_tool()


#Main Code starts here
from google.colab import drive
drive.mount('/content/drive')

from builtins import input
import pandas as pd
import numpy as np

ip_1 = pd.read_csv("/content/drive/MyDrive/seating/ip_1.csv", header=1)
ip_2 = pd.read_csv("/content/drive/MyDrive/seating/ip_2.csv", header=1)
ip_3 = pd.read_csv("/content/drive/MyDrive/seating/ip_3.csv", header=0)
ip_4 = pd.read_csv("/content/drive/MyDrive/seating/ip_4.csv", header=0)

ip_1.head()

ip_1['course_code'] = ip_1['course_code'].str.strip()

ip_2.head()

ip_3.head()

ip_4.head()

ip_1.course_code.value_counts()

ip_3

def extract_floor(room_no):
    if room_no[:2].isalpha():
        return room_no[:]
    else:
        return int(room_no[0])

ip_3['floor'] = ip_3['Room No.'].apply(extract_floor)
room_cap = ip_3.sort_values(by=['floor', 'Exam Capacity'], ascending=[True, True])
room_cap

room_cap.head()

course_counts = ip_1['course_code'].value_counts().reset_index()

course_counts.columns = ['course_code', 'count']

course_counts.head()


def result(course_counts, room_cap, buffer):

  allocations = []

  for _, course in course_counts.iterrows():
      course_code = course["course_code"]
      remaining_students = course["count"]
      course_allocations = []

      for i, room in room_cap.iterrows():
          room_capacity = room["Exam Capacity"]
          effective_capacity = room["effective_capacity"]

          if remaining_students <= 0:
              break

          if effective_capacity > 0:
              if remaining_students <= effective_capacity:
                  course_allocations.append({
                      "course_code": course_code,
                      "room_no": room["Room No."],
                      "num_students_allocated": remaining_students,
                      "vacant_seats": effective_capacity - remaining_students,
                      "buffered_capacity": room["Exam Capacity"] * buffer
                  })
                  room_cap.at[i, "effective_capacity"] -= remaining_students
                  remaining_students = 0
              else:
                  course_allocations.append({
                      "course_code": course_code,
                      "room_no": room["Room No."],
                      "num_students_allocated": effective_capacity,
                      "vacant_seats": 0,
                      "buffered_capacity": room["Exam Capacity"] * buffer
                  })
                  remaining_students -= effective_capacity
                  room_cap.at[i, "effective_capacity"] = 0

      if remaining_students > 0:
          course_allocations.append({
              "course_code": course_code,
              "room_no": None,
              "num_students_allocated": remaining_students,
              "vacant_seats": 0,
              "buffered_capacity": 0
          })

      allocations.extend(course_allocations)

  allocations_df = pd.DataFrame(allocations)

  return allocations_df

final = pd.DataFrame()
result_df['course_code'].value_counts()
buffer = int(input("write the amount of buffer you want in room in percentage (e.g., 10):  "))/100
room_cap["effective_capacity"] = (room_cap["Exam Capacity"] * (1 - buffer)).astype(int)


for i, row in ip_2.iterrows():
  mor = pd.DataFrame({'course_code': row['Morning'].split('; ')})
  mor['course_code'] = mor['course_code'].str.strip()
  mor['count'] =  mor['course_code'].apply(lambda code: ip_1[ip_1['course_code'] == code].shape[0])

  mor = mor.sort_values(by="count", ascending=False).reset_index(drop=True)

  result_df = result(mor, room_cap, buffer)
  final = pd.concat([final, result_df], ignore_index=True)
  room_cap["effective_capacity"] = (room_cap["Exam Capacity"] * (1 - buffer)).astype(int)

  eve = pd.DataFrame({'course_code': row['Evening'].split('; ')})
  eve['course_code'] = eve['course_code'].str.strip()
  eve['count'] =  eve['course_code'].apply(lambda code: ip_1[ip_1['course_code'] == code].shape[0])

  eve = eve.sort_values(by="count", ascending=False).reset_index(drop=True)

  result_df = result(eve, room_cap, buffer)
  final = pd.concat([final, result_df], ignore_index=True)
  room_cap["effective_capacity"] = (room_cap["Exam Capacity"] * (1 - buffer)).astype(int)


final.sample(15)
final[final['course_code']=='MA424']
op_1 = pd.DataFrame(columns=["Date","Course", "Shift", "Room", "Students"])


for index, row in ip_2.iterrows():

  mor = pd.DataFrame({'Course': row['Morning'].split('; '), 'Shift': 'Morning', 'Date': row['Date']})
  op_1 = pd.concat([op_1, mor], ignore_index=True)
  first = row['Morning'].split('; ')

  eve = pd.DataFrame({'Course': row['Evening'].split('; '), 'Shift': 'Evening', 'Date': row['Date']})
  op_1 = pd.concat([op_1, eve], ignore_index=True)


op_1 = op_1.explode('Course').reset_index(drop=True)
op_1.head()
final['course_code'] = final['course_code'].str.strip()
op_1['Course'] = op_1['Course'].str.strip()
expanded_op_1 = op_1.merge(final[['course_code', 'room_no', 'num_students_allocated','buffered_capacity']],
                           left_on='Course', right_on='course_code', how='left')

expanded_op_1 = expanded_op_1.drop(columns=['course_code'])

expanded_op_1 = expanded_op_1.reset_index(drop=True)

expanded_op_1
expanded_op_1.drop(columns=['Room', 'Students'], inplace=True)
expanded_op_1['Date'] = pd.to_datetime(expanded_op_1['Date'], format='%d/%m/%Y')
expanded_op_1.sort_values(by=['Date', 'Shift', 'Course', 'room_no'], ascending=[True, False, True, True], inplace=True)
expanded_op_1['Date'] = expanded_op_1['Date'].dt.strftime('%d/%m/%Y')
expanded_op_1
bachhe = pd.DataFrame(columns=["Course", "Students"])
courses = []
students = []

for group, group_df in ip_1.groupby('course_code'):
  courses.append(group) 
  student_list = ', '.join(group_df['rollno']) 
  students.append(student_list)

bachhe['Course'] = courses
bachhe['Students'] = students
bachhe
bachhe_sorted = bachhe.copy()
bachhe_sorted['Students'] = bachhe_sorted['Students'].apply(lambda students: ', '.join(sorted(students.split(', '))))
bachhe_sorted
expanded_op_1['num_students_allocated'].fillna(0, inplace=True)
expanded_op_1['buffered_capacity'].fillna(0, inplace=True)
expanded_op_1_sorted = expanded_op_1.copy()
expanded_op_1['Roll_no'] = ''

for index, row in expanded_op_1.iterrows():
    course = row['Course']
    no_of_students = int(row['num_students_allocated'])

    bachhe_row = bachhe[bachhe['Course'] == course]

    if not bachhe_row.empty:
          students_list = bachhe_row.iloc[0]['Students']

          if isinstance(students_list, str):
              students_list = students_list.split(', ')

          selected = students_list[:no_of_students]

          expanded_op_1.at[index, 'log'] = ', '.join(selected)

          remaining_students = students_list[no_of_students:]
          bachhe.loc[bachhe['Course'] == course, 'Students'] = ', '.join(remaining_students)

expanded_op_1_sorted['Roll_no'] = ''

for index, row in expanded_op_1_sorted.iterrows():
    course = row['Course']
    no_of_students = int(row['num_students_allocated'])

    bachhe_row = bachhe_sorted[bachhe_sorted['Course'] == course]

    if not bachhe_row.empty:
          students_list = bachhe_row.iloc[0]['Students']

          if isinstance(students_list, str):
              students_list = students_list.split(', ')

          selected = students_list[:no_of_students]

          expanded_op_1_sorted.at[index, 'log'] = ', '.join(selected)

          remaining_students = students_list[no_of_students:]
          bachhe_sorted.loc[bachhe_sorted['Course'] == course, 'Students'] = ', '.join(remaining_students)

expanded_op_1
expanded_op_1_sorted

end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))