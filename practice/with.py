# with
# 매번 file에 대한 close()를 안해줘도 됨!

# 예제 1
import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))
    
# 예제 2
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")
    
# 예제 3
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
