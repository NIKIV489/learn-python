"""
You are given a log file containing entries like:
"ERROR: Disk full", "INFO: User logged in", "WARNING: CPU high"
Write a Python program to:
Count how many ERROR, WARNING, INFO
Print the most frequent message type
"""

log=[
    "ERROR: Disk full",
    "INFO: User logged in",
    "WARNING: CPU high",
    "ERROR: Disk full",
    "INFO: User logged in",
    "WARNING: CPU high",
    "ERROR: Disk full",
    "INFO: User logged in",
    "WARNING: CPU high",
    "INFO: User logged in",
    "WARNING: CPU high",
    "WARNING: CPU high"
]
WARNING=0
INFO=0
ERROR=0
for logg in log:
    if logg.startswith("WARNING"):
        WARNING+=1
    elif logg.startswith("ERROR"):
        ERROR+=1
    elif logg.startswith("INFO"):
        INFO+=1
    else:
        exit
print("count of ERROR is ",ERROR ,"\n count of WARNING is ",WARNING ,"\n count of INFO is ",INFO)
print("Most frequent message type is", max({"ERROR": ERROR, "WARNING": WARNING, "INFO": INFO}, key={"ERROR": ERROR, "WARNING": WARNING, "INFO": INFO}.get))


    
