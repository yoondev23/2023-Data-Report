# DRT(Demand-Responsive Transit) 🚕
#### 최적경로 알고리즘 & 경로 산출물 
* * *
최적경로 알고리즘은 수요 반응형 대중교통 시스템에서 효율적인 경로 및 배차 스케줄을 결정하기 위해 개발한 알고리즘이다. DRT 시스템은 고정 경로 대중교통과 달리 수요에 따라 유동적으로 경로를 조정하고, 승객들의 출발지와 목적지를 고려하여 최적의 경로를 계산하는 것을 목표로 개발하였다.  

<br>

* **수요 예측 및 수집** <br>
DRT 시스템은 승객들의 수요를 정확히 예측하고 수집해야 하므로 이를 위해 DRT 이용자들의 과거 이용 패턴 및 다양한 요인(시간, 위치, 이벤트 등)을 고려함

* **경로 계획**<br>
DRT 시스템은 승객들의 출발지와 목적지에 따라 최적의 경로를 계획함. 출발지(Origin)-목적지(Destination) 간 거리, 교통 혼잡도, 예상 소요 시간 등을 고려

* **경로 최적화**<br>
고객들의 수요를 고려하여 다수의 승객들의 출발지와 목적지를 효율적으로 연결하는 경로를 찾는것을 목표로 하여 네트워크 최적화, 그래프 이론 등을 활용하여 효율적인 경로를 탐색함.

* **배차 스케줄링**<br>
경로 뿐만 아니라 배차 스케줄링도 고려함. 어떤 차량이 어떤 경로로 이동하며, 언제 승객을 태우고 내리게 될지 결정하는 것이 중요하므로 배차 스케줄은 대중교통 운영 효율성을 결정짓는 핵심적인 역할이 됨.

* **제약 조건 고려**<br>
DRT 시스템에서는 운영상의 제약 조건도 고려되야 하므로 차량 운행 가능 시간, 휴게시간, 차량 용량 등과 같은 제약 사항을 고려하여 경로와 배차 스케줄을 계획함.

<!--
* **실시간 업데이트**<br>
DRT 시스템은 실시간으로 변화하는 수요와 교통 상황에 대응할 수 있어야 한다. 승객의 실시간 예약 및 취소, 교통 혼잡도 등의 정보를 수집하여 경로 및 배차 스케줄을 업데이트한다. -->

* **알고리즘 종류**<br>
메타휴리스틱 알고리즘(유전 알고리즘, 입자 군집 최적화 등), 그래프 이론 알고리즘(다익스트라, D* 등), 휴리스틱 알고리즘 등을 활용
  

