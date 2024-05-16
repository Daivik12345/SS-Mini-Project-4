mport csv
from collections import defaultdict
import os


directory = '/Users/cubingultimate/Downloads/marks_add.csv'



marks_dict = defaultdict(int)

with open(file_path, mode='r', newline='') as file:
    csv_reader = csv.reader(file)
    
    
    next(csv_reader)
    
    
    for row in csv_reader:
        roll_no = row[0]
        marks = int(row[1])
        
        
        marks_dict[roll_no] += marks


output_file_path = '/Users/cubingultimate/Downloads/submission.csv'

with open(output_file_path, mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    
    
    csv_writer.writerow(['roll no', 'marks'])
    
    
    for roll_no, total_marks in marks_dict.items():
        csv_writer.writerow([roll_no, total_marks])