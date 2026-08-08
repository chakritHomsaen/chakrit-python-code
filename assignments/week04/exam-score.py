scores = []
for i in range(1,6):
    add_score = int(input(f"Enter score of student {i}: "))
    ans = "ผ่าน" if add_score >= 50 else "ไม่ผ่าน"
    scores.append([i, add_score, ans])
    
print()
print("\n" .join(f"student {No} : {score} -> {ans}" for No, score, ans in scores))