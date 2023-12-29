# Chapter05-02-ex1
# 사용자 입력
# Input 사용법
# 기본 타입(str)

#  예제1 -> 예외처리
# try :
#     n = int(input("Enter a number : "))
#     print('Ok. Your number is : ', n)
# except ValueError:
#     print('This is not a number')

# 예제2 -> 올바른 값 입력 완료 까지 지속
# while True:
#     try:
#         n = int(input("Enter a number : "))
#         print('Ok. Your number is : ', n)
#         break
#     except ValueError:
#         print('This is not a number')