salary = { 
          'sue'    :42000, 
          'george' :27000, 
          'ali'    :53000,
          'gina'   :37000,
          'peter'  :62000  
         }

listOfKeys = list(salary.keys())
listOfKeys.sort()

for key in listOfKeys:
    print(f"{key:8s} {salary[key]}")






# salary['jim'] = 44000
# salary['ali'] = 56000
# salary['peter'] = None
# # del salary['gina']
# salary.pop('gina')
# print(salary)
#            
# if 'ali' in salary:
#     print("ali is in dict")
#            
# if not 'jon' in salary:
#     print("jon is NOT in dict")
