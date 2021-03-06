import random
import secrets
import string
import time
from faker import Faker

fake = Faker("ja_JP")

def main(hack_type):
	if hack_type == "AttackBlock":
		logs = [
			"Security Hole Attack Detected",
			"Security Hole Attack Blocked",
			"Security Hole Detected", 
			"Security Hole Repaired",
			"ThinkPHP Attack Detected",
			"ThinkPHP Attack Blocked",
			"Spyware Virus Detected",
			"Spyware Virus Deleted",
			"Syn flood Attack Detected",
			"Syn flood Attack Blocked",
			"HOIC DoS Detected",
			"HOIC DoS Blocked",
			"LOIC DoS Detected",
			"LOIC DoS Blocked"
		]
		for count in range(3):
			generated_ip = fake.ipv4()
			logs.append(f"IP {generated_ip} Access Blocked")
		while True:
			random.shuffle(logs)
			print(logs[0])
			time.sleep(random.uniform(0.1, 0.5))
