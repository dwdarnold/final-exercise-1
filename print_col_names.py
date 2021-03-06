# EXERCISE INSTRUCTIONS
# This script should output a list of column names from a CSV file with any spaces replaced by underscores (the '_' character)
# This script was started by someone else, and you've been asked to fix any errors and provide this functionality

import pandas
data = pandas.read_csv("weather_data/weather_year.csv")

col_names = data.columns.values.tolist()
#print col_names

# STEP 1 - Define a function below called "replace_whitespace" that can replace characters in a string with others. The function should take two parameters, the first being the string that needs whitespace characters replacing, and the second being the character to insert instead of the whitespace.

def replace_whitespace(sequence,replacement):
    	sequence = sequence.replace(' ',replacement)
	print sequence
	    


# STEP 2 - output the new column names generated by running your replace_whitespace function
# BONUS - trim any leading (at the front of the string) or trailing (at the end) whitespace characters from each column name before you call your replace_whitespace function

a = 0
while a < len(col_names):
    if col_names[a][0] == ' ':
        col_names[a] = col_names[a][1:]
    if col_names[a][-1] == ' ':
        col_names[a] = col_names[a][:-1]
    replace_whitespace(col_names[a],'_')
    a = a + 1


# STEP 3 - Using the shell:
# (a) write ONLY the new non-whitespace column names to a new file called columnNames instead of the shell output (stdout)
# (b) similarly, sort the outputted column names into a new file called sortedColumnNames

# Push the following files to Aleksandra's github: this file containing the fixed code, file with the column names with spaces removed, and the file with the sorted names
# This will raise a pull request, so we can check your script
