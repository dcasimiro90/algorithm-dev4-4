def main ():
    num1 = 5
    num2 = 10
    
    sequence = [num1, num2]
    while len(sequence) < 5:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
        
    print(sequence)
    
if __name__ == "__main__":
    main()
