

class Warriors: 
    def warriors(self, strength , attack_range):
        answer = {}

        for i in range(len(strength)):    
            answer[i] = i
            if answer[i] > 


            N = 1
            while True:
                if i == len(strength)-1:
                    answer.append(i)
                    break
                elif i+N == len(strength)-1 and attack_range[i] >= N and strength[i] > strength[i+N]:
                    answer.append(i+N)
                    break
                elif attack_range[i] < N or strength[i+N] >= strength[i]:
                    answer.append(i+N-1)
                    break
                N += 1
        return answer

if __name__ == "__main__":
    sol = Warriors()
    print(sol.warriors([11, 13, 11, 7, 15],
                       [ 1,  8,  1, 7,  2]))
