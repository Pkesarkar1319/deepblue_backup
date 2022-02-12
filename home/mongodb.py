from unittest import result
import pymongo as py
import json

myclient = py.MongoClient("mongodb://localhost:27017/")
db = myclient["Resume"]
collection = db['data']


def get_skills():

    return collection.distinct('skills')


def search(mandatory, optional):
    results=[]
    eachvalue = round(1/(len(mandatory[0])+1), 2)
    x = 1/(len(optional[0])+len(optional[1]))
    eachvalue_o = round(x, 2)

    
    

    for i in collection.find({}):
      temp = {}
      exp=mandatory[1]
      skillset=list(set(mandatory[0]) & set(i['skills']))
      optional_skills=list(set(optional[0]) & set(i['skills']))
      temp['Id'] = str(i['_id'])
      temp['Name'] = i['name']
      temp['time'] = str(i['Time'])
      temp['matched_mandatory_skills'] = skillset
      temp['matched_optional_skills'] = optional_skills
      lang=list(set(optional[1]) & set(i['languages']))
      if len(lang)>0:
       temp['language_matched']=lang
      else:

       temp['language_matched']=[]
      if i['Work_Experience'] in range(exp[0],exp[1]):
       temp['matched_experience']=i['Work_Experience']


       Experience=1
      else:
       #temp['experience of {} and {}'.format(exp[0],exp[1])] ='NA'
       temp['matched_experience']=[]




       Experience = 0




      temp['notmatched_mandatory_skills'] = list(set(mandatory[0]) - set(skillset))
      temp['notmatched_optional_skills'] = list(set(optional[0]) - set(optional_skills))
      temp['mandatory_value']=round((len(skillset)+Experience)*eachvalue,1)
      temp['optional_value']=round((len(optional_skills)+len(lang))*eachvalue_o,1)
      results.append(temp)
    return results
    # for i in results:
    #     # print("mandate value:{} optional value:{}".format(i['mandatory_value'],i['optional_value']))
    #     if (i['mandatory_value'] > 0 and i['matched_mandatory_skills'] != []):
    #         if (i['mandatory_value'] == 1):
    #             completely_matched.append(i)
    #         else:
    #             partially_matched.append(i)


    #     else:
    #         Not_matched.append(i)




# def complete_matched():
#     completely_matched.sort(key=lambda e:(e['optional_value']),reverse=True)
#     return completely_matched
# def partial_matched():
#     partially_matched.sort(key=lambda e:(e['mandatory_value'],e['optional_value']),reverse=True)
#     return partially_matched
# def not_matched():
#     Not_matched.sort(key=lambda e:(e['optional_value']),reverse=True)
#     return Not_matched


#mandatory=[['Android','Python','SQL'],[3,9]]
#optional=[['Docker','HTML','Javascript'],['Marathi','English']]