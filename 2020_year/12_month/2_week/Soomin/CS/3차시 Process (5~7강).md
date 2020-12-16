# 3차시 Process (5~7강)

## 5강 Process 1

>  Process 개요

![3-1](./Images/3-1.PNG)

![3-2](./Images/3-2.PNG)

![3-3](./Images/3-3.PNG)

![3-4](./Images/3-4.PNG)

 ![3-5](./Images/3-5.PNG)

![3-6](./Images/3-6.PNG)

**질문?** Process A의 PCB와 Process B의 PCB는 결국 물리적 메모리의 데이터 영역에 전부 할당되는 것인가?

![3-7](./Images/3-7.PNG)

(1) 번은 cache memory 를 전부 지울 필요 없어서 부담이 적다.

![3-8](./Images/3-8.PNG)

![3-9](./Images/3-9.PNG)

![3-10](./Images/3-10.PNG)

![3-11](./Images/3-11.PNG)

Long-term : 메모리에 시작 프로세스 중 어떤 것을 올리지 정하는 것

\* degree of multiprogramming : 몇개의 프로세스가 올라가 있는지

Short-term : 어떤 프로세스가 다음 running이 될지 정하는 것

Medium-term : 우리가 사용하고 있는 시스템은 장기 스케줄러가 없기 때문에 메모리에 너무 많은 프로세스가 올라가 있다면 디스크로 쫓아냄

![3-12](./Images/3-12.PNG)

Suspended : 중기 스케줄러에서 디스크로 쫓겨난 프로세스들의 상태 or 사용자가 프로그램을 일시 정지시킨 경우

Blocked와 Suspended의 가장 큰 차이는 외부에서 멈춘것인지 아닌지 이다.

 ![3-13](./Images/3-13.PNG)

System call 이나 Interrupt가 발생해도 '커널이 Running이다' 라고 하지 않고 'Process가 monitor mode에서 running이다' 라고 한다.



## 6강 Process 2

>  Thread 개요 1

**Thread** 

![3-14](./Images/3-14.PNG)

- Process 내부에 CPU 실행 단위가 여러개 있는것
- 동일한 일을 하는 프로세스를 여러개 만들면 메모리가 낭비되기 때문에 프로세스 내부에 각기 다른 코드를 실행하는 Thread를 둔다. 
- PC(Program Counter == 코드의 어떤 부분을 실행하고 ), registers, stack만 여러개 두는것 
- Process에서 공유할 수 있는건 최대한 공유한다.



![3-15](./Images/3-15.PNG)

![3-16](./Images/3-16.PNG)



## 7강 Process 3

>  Thread 개요 2

![3-17](./Images/3-17.PNG)

![3-18](./Images/3-18.PNG)

- 응답성
  - 예) 웹페이지 로드할 때 이미지 파일이 로드될 동안 다른 텍스트를 먼저 보여준다.
- 자원 공유
- 경제성
  - 프로세스를 하나 만드는 것이 아니라 빠르다.
  - 프로세스를 넘어가는 context switch를 할 필요가 없어 빠르다.
- Multiprocessor(CPU가 여러개인 경우)
  - CPU가 여러개이면 각각의 Thread가 각기 다른 CPU를 할당받아 병렬적으로 일을 할 수 있다.



![3-19](./Images/3-19.PNG)

- Kernel Threads : Kernel이 Thread의 존재를 알고 Thread를 스케줄링 하는것
- User Threads : User Program이 라이브러리의 지원을 받아서 Thread를 관리하는 것, 제약점이 조금 존재



출처 : http://www.kocw.or.kr/home/cview.do?mty=p&kemId=1046323