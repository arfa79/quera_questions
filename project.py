import re

skills = []
jobs = [] 
users = []
job_views = {}
user_skill_views = {}

def validate_name(name):
    if not re.fullmatch(r'[A-Za-z]{1,10}', name):
        return "invalid name"
    
def validate_age(age):
    if age < 0 or age > 200:
        return "invalid age"
        
def validate_timetype(timetype):
    if timetype not in ["FULLTIME", "PARTTIME", "PROJECT"]:
        return "invalid timetype"
        
def validate_salary(salary):
    if salary < 0 or salary >= 1000000000 or salary % 1000 != 0:
        return "invalid salary"
        
def add_job(params):
    name, minage, maxage, timetype, salary = params
    err = validate_name(name) or validate_age(minage) or validate_age(maxage)
    if maxage < minage: 
        err = "invalid age interval" 
    err = err or validate_timetype(timetype) or validate_salary(salary)
    if err:
        print(err)
        return
    
    job_id = len(jobs) + 1
    jobs.append({
        "id": job_id,
        "name": name, 
        "minage": minage,
        "maxage": maxage,
        "timetype": timetype,
        "salary": salary,
        "skills": [],
    })
    
    print("job id is", job_id)
    
def add_user(params):
    name, age, timetype, salary = params
    err = validate_name(name) or validate_age(age) 
    err = err or validate_timetype(timetype) or validate_salary(salary)
    if err:
        print(err)
        return

    user_id = len(users) + 1
    users.append({
        "id": user_id, 
        "name": name,
        "age": age,
        "timetype": timetype, 
        "salary": salary,
        "skills": []
    })
    
    print("user id is", user_id)
    
def add_job_skill(job_id, skill):
    if job_id > len(jobs): 
        print("invalid index")
        return
        
    job = jobs[job_id-1] 
    if skill not in skills:
        print("invalid skill") 
        return
    if skill in job["skills"]:
        print("repeated skill")
        return
        
    job["skills"].append(skill)
    print("skill added")
    
def add_user_skill(user_id, skill):
    if user_id > len(users):
        print("invalid index")
        return 
        
    user = users[user_id-1]
    if skill not in skills:
        print("invalid skill")
        return
    if skill in user["skills"]:
        print("repeated skill")  
        return
        
    user["skills"].append(skill)
    print("skill added")
        
def view_job(user_id, job_id):
    if user_id > len(users) or job_id > len(jobs):
        print("invalid index")
        return
        
    print("tracked")
    
    user = users[user_id-1]
    job = jobs[job_id-1]
    
    if job_id not in job_views:
        job_views[job_id] = 0
    job_views[job_id] += 1
    
    for skill in job["skills"]:
        if skill not in user_skill_views:
            user_skill_views[skill] = 0
        user_skill_views[skill] += 1
        
def print_job_status(job_id):
    if job_id > len(jobs):
        print("invalid index")
        return
        
    job = jobs[job_id-1]
    print(job["name"], end="-")
    print(job_views.get(job_id, 0), end="-")
    
    skills = []
    for skill in job["skills"]:
        cnt = user_skill_views.get(skill, 0) 
        skills.append((skill, cnt))
    skills.sort(key=lambda x: x[1])
    
    print(*(f"({skill},{cnt})" for skill, cnt in skills), sep=",")
    
def print_user_status(user_id):
    if user_id > len(users):
        print("invalid index")
        return 
        
    user = users[user_id-1]
    print(user["name"], end="-")
    
    skills = []
    for skill in user["skills"]:
        cnt = user_skill_views.get(skill, 0)
        skills.append((skill, cnt))
    skills.sort(key=lambda x: x[1], reverse=True)
    
    print(*(f"({skill},{cnt})" for skill, cnt in skills), sep=",")

def get_job_score(user, job):
    age = user["age"]
    age_score = min(job["maxage"] - age, age - job["minage"]) 
    if age < job["minage"]:
        age_score = age - job["minage"]  
    if age > job["maxage"]:
        age_score = job["maxage"] - age
        
    user_skills = set(user["skills"])
    job_skills = set(job["skills"])
    skill_score = 3*len(user_skills & job_skills) - len(job_skills - user_skills)
    
    time_score = 0
    if user["timetype"] == job["timetype"] == "FULLTIME":
        time_score = 10
    elif user["timetype"] == job["timetype"] == "PARTTIME":
        time_score = 10
    elif user["timetype"] == job["timetype"] == "PROJECT":
        time_score = 10
    elif (user["timetype"], job["timetype"]) in [("FULLTIME", "PARTTIME"), ("PARTTIME", "FULLTIME")]:
        time_score = 5
    elif (user["timetype"], job["timetype"]) in [("FULLTIME", "PROJECT"), ("PROJECT", "FULLTIME")]: 
        time_score = 4
    elif (user["timetype"], job["timetype"]) in [("PARTTIME", "PROJECT"), ("PROJECT", "PARTTIME")]:
        time_score = 5
        
    salary_diff = abs(user["salary"] - job["salary"])
    salary_score = int(1000 / max(salary_diff, 1))
    
    total_score = age_score + skill_score + time_score + salary_score
    return job["id"], total_score*1000 + job["id"]
    
def get_job_list(user_id):
    if user_id > len(users):
        print("invalid index")
        return
        
    user = users[user_id-1]
    scores = []
    for job in jobs:
        score = get_job_score(user, job)
        if score:
            scores.append(score)
            
    scores.sort(key=lambda x: x[1], reverse=True) 
    for job_id, score in scores[:5]:
        print(f"({job_id},{score})")

while True:
    line = input().split()
    cmd = line[0]
    
    if cmd == "ADD-USER":
        add_user(line[1:])
        
    elif cmd == "ADD-JOB":   
        add_job(line[1:])
        
    elif cmd == "ADD-JOB-SKILL":
        add_job_skill(int(line[1]), line[2])
        
    elif cmd == "ADD-USER-SKILL":
        add_user_skill(int(line[1]), line[2])
        
    elif cmd == "VIEW":
        view_job(int(line[1]), int(line[2]))
        
    elif cmd == "JOB-STATUS":
        print_job_status(int(line[1]))
        
    elif cmd == "USER-STATUS":
        print_user_status(int(line[1]))
        
    elif cmd == "GET-JOBLIST":
        get_job_list(int(line[1]))
