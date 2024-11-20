import pandas as pd

from google.colab import files

stud_grade = pd.read_excel('/content/drive/MyDrive/Colab Notebooks/Input-1.xlsx')

stud_grade['total_marks'] = 0
stud_grade['grade'] = ''

stud_grade.head(20)
total_stud_given = stud_grade['Name'].count()

for i in range(2,len(stud_grade)):
  total_mark = (stud_grade['Mid Sem'][i]*stud_grade['Mid Sem'][1])/stud_grade['Mid Sem'][0] + (stud_grade['Endsem'][i]*stud_grade['Endsem'][1])/stud_grade['Endsem'][0] + (stud_grade['Quiz 1'][i]*stud_grade['Quiz 1'][1])/stud_grade['Quiz 1'][0] + (stud_grade['Quiz 2'][i]*stud_grade['Quiz 2'][1])/stud_grade['Quiz 2'][0]
  stud_grade.at[i,'total_marks'] = total_mark
stud_grade.at[0,'total_marks'] = ' '
stud_grade.at[1,'total_marks'] = ' '
stud_grade.at[0,'Name'] = ' '
stud_grade.at[1,'Name'] = ' '
stud_grade.head()

grading_sys = {
    'grade' : ['AA','AB','BB','BC','CC','CD','DD','F','I','PP','NP'],
    'old iapc reco' : ['5','15','25','30','15','5','5','0','0','0','0'],
    'Counts' : [' ' for _ in range(11)],
    'Round' : [' ' for _ in range(11)],
    'Count verified' : [' ' for _ in range(11)]
    }

df = pd.DataFrame(grading_sys)
df['old iapc reco'] = pd.to_numeric(df['old iapc reco'])
df['Counts'] = 102*df['old iapc reco']/100
df['Round'] = df['Counts'].round(0)
df.head(11)

stud_grade_before = stud_grade.iloc[:2]
stud_grade_after = stud_grade.iloc[2:]
stud_grade_after_sorted = stud_grade_after.sort_values(by='total_marks', ascending=False)
stud_grade = pd.concat([stud_grade_before, stud_grade_after_sorted], ignore_index=True)

stud_grade.head()

for i in range(2,len(stud_grade)):
  if i<7:
    stud_grade.at[i,'grade'] = 'AA'
  elif i<22:
    stud_grade.at[i,'grade'] = 'AB'
  elif i<48:
    stud_grade.at[i,'grade'] = 'BB'
  elif i<79:
    stud_grade.at[i,'grade'] = 'BC'
  elif i<94:
    stud_grade.at[i,'grade'] = 'CC'
  elif i<99:
    stud_grade.at[i,'grade'] = 'CD'
  elif i<104:
    stud_grade.at[i,'grade'] = 'DD'

stud_grade.head(21)

AA_count = stud_grade['grade'].value_counts().get('AA', 0)  # Default to 0 if 'Alice' doesn't exist
df.at[0,'Count verified'] = AA_count
AB_count = stud_grade['grade'].value_counts().get('AB', 0)  # Default to 0 if 'Alice' doesn't exist
df.at[1,'Count verified'] = AB_count
BB_count = stud_grade['grade'].value_counts().get('BB', 0)  # Default to 0 if 'Alice' doesn't exist
df.at[2,'Count verified'] = BB_count
BC_count = stud_grade['grade'].value_counts().get('BC', 0)  # Default to 0 if 'Alice' doesn't exist
df.at[3,'Count verified'] = BC_count
CC_count = stud_grade['grade'].value_counts().get('CC', 0)  # Default to 0 if 'Alice' doesn't exist
df.at[4,'Count verified'] = CC_count
CD_count = stud_grade['grade'].value_counts().get('CD', 0)  # Default to 0 if 'Alice' doesn't exist
df.at[5,'Count verified'] = CD_count
DD_count = stud_grade['grade'].value_counts().get('DD', 0)  # Default to 0 if 'Alice' doesn't exist
df.at[6,'Count verified'] = DD_count
F_count = stud_grade['grade'].value_counts().get('F', 0)    # Default to 0 if 'Alice' doesn't exist
df.at[7,'Count verified'] = F_count
I_count = stud_grade['grade'].value_counts().get('I', 0)    # Default to 0 if 'Alice' doesn't exist
df.at[8,'Count verified'] = I_count
PP_count = stud_grade['grade'].value_counts().get('PP', 0)  # Default to 0 if 'Alice' doesn't exist
df.at[9,'Count verified'] = PP_count
NP_count = stud_grade['grade'].value_counts().get('NP', 0)  # Default to 0 if 'Alice' doesn't exist
df.at[10,'Count verified'] = NP_count

df

stud_grade_before = stud_grade.iloc[:2]
stud_grade_after = stud_grade.iloc[2:]
stud_grade_after_sorted = stud_grade_after.sort_values(by='Roll', ascending=True)
stud_grade = pd.concat([stud_grade_before, stud_grade_after_sorted], ignore_index=True)

stud_grade.head(21)

df1 = pd.DataFrame(stud_grade)
df1.to_excel('Output-1.xlsx', index=False)
with pd.ExcelWriter('Output-1.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Sheet1', index=False)
    df.to_excel(writer, sheet_name='Sheet2', index=False)
    workbook  = writer.book
    worksheet1 = workbook.get_sheet_by_name('Sheet1')
    worksheet2 = workbook.get_sheet_by_name('Sheet2')
# files.download('Output-1.xlsx')