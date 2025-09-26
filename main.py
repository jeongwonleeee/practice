import sys

def solve():
    """
    백준 1000번, A+B 문제 풀이
    두 정수 A와 B를 입력받아 A+B를 출력하는 프로그램
    """
    try:
        # 한 줄에 공백으로 구분된 두 정수 입력받기
        a, b = map(int, sys.stdin.readline().split())
        
        # 결과 출력
        print(a + b)
        
    except ValueError:
        print("유효한 정수를 입력해주세요.")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

if __name__ == "__main__":
    solve()