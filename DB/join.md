<h3>JOIN</h3>
* 두개 이상의 table들에 있는 데이터를 한번에 조회하는 것</br>

#

<h3>IMPLICIT JOIN</h3>
* from절에는 table만 나열하고 where절에 join condition을 명시하는 것</br>

#

<h3>EXMPLICIT JOIN</h3>
* from절에는 JOIn 키워드와 함께 JOINED table을 명시하는 것</br>

#

<h3>INNER JOIN</h3>
* 두 table에서 join condition을 만족하는 tuple들로 result table을 만드는 join</br>
* form table1 JOIN table2 on join condition</br>

#

<h3>OUTER JOIN</h3>
* 두 table에서 join condition을 만족 + 만족하지 않는 tuple들로 result table을 만드는 join</br>
* form table1 LEFT OUTER JOIN table2 on join condition -> 만족하지 않는 조건도 출력</br>

#

<h3>Equi JOIN</h3>
* =을 사용한 JOIN</br>

#

<h3>USING</h3>
* 이름이 같으면 USING(dept_id);</br>

#

<h3>Natural Join</h3>
* 두 table에서 같은 이름을 가진 모든!! attribute pair에 대해 equi join을 수행</br>
* select * from employee E NATURAL Department D;</br>

#

<h3>Cross Join</h3>
* select from employee CROSS JOIN department;</br>
* 잘 안씀

#

<h3>Self Join</h3>
* 본인 스스로 join</br>
