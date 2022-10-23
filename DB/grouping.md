<h3>Order By</h3>
* 오름차순 ASC = 작은수부터</br>
* 내림차순 DESC = 큰수부터 </br>

#

<h3>Aggregate Function</h3>
* count, sum, max, min, avg -> null 제외하고 알 수 있음</br>
* select COUNT(*) from employee; => 직원 수</br>
* count는 null 포함하고 싶으면 null이 포함된 것 넣지 말기

#

<h3>Group By</h3>
* Group By에 있는 것이 꼭 Select에도 있어야 함

#

<h3>Having</h3>
* 조건을 넣기 위해 사용.
* Group By와 함께 사용
* ex) Having salary > count(*)

