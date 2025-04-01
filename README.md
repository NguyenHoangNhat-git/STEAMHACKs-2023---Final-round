# For round 2 and 3 - STEAMHacks2023
**Team name**: MEMEtal-Health
  
**Tributes to my teammates** : Đỗ Ngọc Mai and Lê Phan Trung Quốc (design + marketing)
  
**Topic** : a supportive online platform to connect young people with potential mental problems with experts in the field. The site provice a safe place for users to express their feelings and work towards mental well-being with professional support.

## Functionalities include:
**Key Features :**
- **Authenciation** : 2 account types for specialists and normal users(patient)
- **Online Consultations**: Schedule online meet-up (helping session) with specialists
- **Real-time messaging between specialists and normal users**
- **Community Blog** : where users can share their stories, experiences and insights on mental health

**Patient exclusive:**
  - Free short courses regarding mental health
  - Progress monitoring system to help create and stay on goals
  - Virtual diary to help better reflect on one's self

## Requirements
- Download all packages in PACKAGES.text
- Require docker to host redis (required for real-time messaging through sockets)

## How to run
```
docker run --rm -p 6379:6379 redis:7
py manage.py runserver
```
## Demo

- User guide in Vietnamese : https://drive.google.com/file/d/1-mVTPO6IQJL77niSoGPO5chs1-nUxEST/view?usp=drive_link
