from numpy import real, imag

K = [complex(0) for _ in range(10)]
directions = {"R": 1,"L": -1,   "U": 1j,"D": -1j}
visits_T = {0}
visits_1 = {0}

for step in open("d9.txt").readlines():
    D, L = step.strip().split(" ")
    for i in range(int(L)):
        K[0] += directions[D]

        for j in range(len(K)-1):
            if abs(K[j] - K[j+1]) >= 2:
                if real(K[j]) != real(K[j+1]):
                    K[j+1] += 1 if real(K[j]) > real(K[j+1]) else -1
                if imag(K[j]) != imag(K[j+1]):
                    K[j + 1] += 1j if imag(K[j]) > imag(K[j+1]) else -1j

        visits_1.add(K[1])
        visits_T.add(K[-1])

print(len(visits_1), len(visits_T))
