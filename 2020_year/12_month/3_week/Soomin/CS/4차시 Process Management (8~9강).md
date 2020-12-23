# 4차시 Process Management (8~9강)

## 8강 Process Management 1

>  Process Management 개요

![4-1](./Images/4-1.PNG)

- 부모 프로세스에서 복제하는 대상 
  - 프로세스의 문맥을 모두(코드, 스택, 데이터 영역)
  - CPU 문맥을 모두 (PC register까지)

- Copy-on-write(COW) 
  - 부모 프로세스를 복제한 그대로 자식 프로세스를 두면 중복으로 비효율적이다.
  - 따라서 기본적으로 pc만 복제를 하고 write가 발생할 때만 해당하는 부분을 복제하는 방식



![4-2](./Images/4-2.PNG)



fork : 부모 프로그램을 복제 (운영체제가 복제를 해줌)

exec : 새로운 프로그램으로 덮어씌우는 과정







![4-3](./Images/4-3.PNG)



## 9강 Process Management 2

> Process와 관련한 시스템콜, Process 간 협력



### Process와 관련한 시스템콜

#### fork()

![4-4](./Images/4-4.PNG)

왼쪽 : 부모 프로세스

오른쪽 : 자식 프로세스

부모 프로세스에서 fork를 하게 되면 똑같은 프로세스가 생기는데(오른쪽) 이 때 부모 프로세스의 pc 를 가지고 있기 때문에 fork 다음 코드부터 실행되게 된다.

#### exec()

![4-5](./Images/4-5.PNG)



![4-6](./Images/4-6.PNG)





![4-7](./Images/4-7.PNG)



- exec은 fork 없이도 가능하다.

- main함수의 execlp 이후의 코드는 실행이 불가능하다.



#### wait()

![4-8](./Images/4-8.PNG)

wait : 자식 프로세스가 종료될 때까지 기다리는 모델



#### exit()

![4-9](./Images/4-9.PNG)



### Process 간 협력

![4-10](./Images/4-10.PNG)



![4-11](./Images/4-11.PNG)



![4-12](./Images/4-12.PNG)

shared 메모리도 처음에는 kernel을 거쳐야 사용 가능











출처 : https://core.ewha.ac.kr/publicview/C0101020140321144554159683?vmode=f

