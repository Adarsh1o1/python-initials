for i in range(2,21):
        with open(f"tables{i}.txt","w") as f:
            for j in range(1,11):
                f.write(f"{i}*{j}={i*j}\n")
              