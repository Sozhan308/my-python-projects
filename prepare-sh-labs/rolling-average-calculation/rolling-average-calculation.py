'''https://prepare.sh/interview/devops/674eb727473242bc582e99d4'''

from typing import List

def rolling_average_calculation(number: List[float], k: int) -> List[float]:
    # when Input list is empty, return empty list
    # when k is zero, empty list is returned
    # when k is greater than length of the input list , return empty list
    if len(number) == 0 or k <= 0 or k > len(number):
        return []
    
    # Logic goes here for rolling average
    
    rolling_average = []

    for i in range(len(number) - k + 1):
        window_sum = sum(number[i:i+k])
        rolling_average.append(window_sum / k)
        
    return rolling_average    
            
            
            
def main():
    k = int(input())
    number = list(map(float, input().split()))
    result = rolling_average_calculation(number, k)
    print(result)
    
if __name__=='__main__':
    main()