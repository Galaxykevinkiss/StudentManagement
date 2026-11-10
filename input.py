def input_score():
    while True:
        try:
            score = float(input("input score:"))
            if score < 0 or score > 100:
                print("Score should be between 0 and 100")
            else:
                return score
        except ValueError:
            print("Please input number!")

if __name__ == '__main__':
    score = input_score()
    print(score)