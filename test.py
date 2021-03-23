import requests as r
from random import choice, getrandbits
import threading
from app import main
from pprint import pprint


def test():
    print("Requesting all jobs")
    jobs = r.get('http://127.0.0.1:8080/api/jobs').json()
    pprint(jobs)
    print()

    print("Requesting only one job")
    job = r.get(f'http://127.0.0.1:8080/api/jobs/{choice(tuple(jobs.keys()))}').json()
    print(job, end='\n'*2)

    print("Checking wrong id")
    job = r.get(f"http://127.0.0.1:8080/api/jobs/{getrandbits(10)}")
    print(job.status_code, job.json(), end='\n'*2)

    print("Checking error type (String)")
    job = r.get(f"http://127.0.0.1:8080/api/jobs/gg")
    print("Status:", job.status_code)


test()
