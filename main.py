#Traverse Data 

#Survey-results

# Load File Data into Lists
surv_results = []
file_ref = open("survey-results.txt","r")
for line in file_ref:
  line = line.strip()
  surv_results.append(line)

age_results = []
file_ref = open("age-data.txt","r")
for line in file_ref:
  line = line.strip()
  age_results.append(int(line))

number_data = []
file_ref = open("number-data.txt","r")
for line in file_ref:
  line = line.strip()
  number_data.append(int(line))



# Process the Data in the Lists
YesCount = 0
NoCount = 0
MaybeCount = 0
for line in surv_results:
  if "Yes" == line or "Yes"==line:
    YesCount = YesCount + 1
    
  elif "No" == line:
    NoCount = NoCount + 1

  else:
    MaybeCount =  MaybeCount + 1

#Print Output
print("Expected Results: " + "Yes "+ "(" + str(YesCount) + ")," + "No "+ "("+ str(NoCount)+ "), " + "Maybe "+ "("+ str(MaybeCount)+ ")")



#AGE RESULTS
lessthan18 = 0
btw18 = 0
btw36 = 0
above65 = 0
for line in age_results:
    if line < 18 :
       lessthan18 = lessthan18 + 1
    elif line >= 18 and line <= 35:
      btw18 = btw18 + 1
    elif line >= 35 and line <= 65:
      btw36 = btw36 + 1
    else:
      above65 = above65 + 1

#Print Output
print("Expected Results: " + "Under 18 " + "(" + str(lessthan18)+ "), " + "18 to 35 " + "(" + str(btw18)+ "), " + "36 to 65 " + "(" + str(btw36)+ "), " + "Above 65 " +"(" + str(above65)+ ")")

#Number Data 
evenNum = 0
oddNumb = 0
for line in number_data:
  if (line %2) == 0 :
    evenNum = evenNum +1
  else:
    oddNumb = oddNumb + 1

#Print Output
print("Expected Results: " + "Even (" + str(evenNum) + "), " + "Odd (" + str(oddNumb) + ")")

