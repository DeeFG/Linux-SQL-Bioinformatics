# Linux-SQL-Bioinformatics
# Linux: 
## 1. What does ls -alt do? 

* List hidden files and folders that are listed based on newest to oldest

## 2. What command would you use to list all files starting with 'Run' and ending with '.txt' in a directory and all of its subdirectories? 

 * find . -name Run \* 
 *  find . -type f -name '*.txt' 

## 3. How would you append the contents of 'exampleFile1.txt' to 'exampleFile2.txt'? 

* cat exampleFile1.txt >> exampleFile2.txt


## 4. How would you (1) sort the contents of 'exampleFile1' and (2) redirect the sorted content to 'exampleFile2.txt' in one line using the pipe operator? 

* cat exampleFile1.txt | sort > exampleFile2.txt


## 5. Which commands would you use to find files whose name match a certain pattern, and to find files containing a certain text? 

 * grep - r
 * grep  “ text-to-search” ./



# SQL: 
## 1. For the following SQL statement, what is wrong with it and how would you fix it: -- 
## Question: 

## SELECT UserId, AVG(Total) AS AvgOrderTotal 
## FROM Invoices 
## HAVING COUNT(OrderId) >= 1 

* There is no way to arrange the average data that is searched. The data is being averaged based off of multiple totals of each user. The data it need to group the user IDs together using a  **GROUP BY UserId**  so the averages are associated with each user.
