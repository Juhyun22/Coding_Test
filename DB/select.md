<h3>조회</h3>
* select name, position from employee where id = 9; -> employee의 id = 9인 name, position을 조회<br/>
* select attribute from tables where conditions;<br/>
* select 뭐뭐 from 테이블 이름 where 조건(selection) and 두개가 똑같은 조건(join);<br/>
* select 어디의 id, 어디의 name(중복된 이름은 확실하게 해주기) .. 충돌 안되게!<br/>

#

<h3>AS</h3>
* ~로 해서 쓴다!<br/>
* select 뭐뭐 from project AS A, employee AS B where ~<br/>

#

<h3>DISTINCT</h3>
* 중복된 튜플들 제거<br/>
* select DISTINCT P.id, P.name from employee as E, works_on as W, project as P<br/>
where E.position = 'DSGN' and E.id = W.empl_id and W.proj_id = P.id;<br/>

#

<h3>LIKE</h3>
* select name from employee where name LIKE 'N%' or name LIKE '%N'<br/>
* select name from employee where name LIKE '%NG%'<br/>
* select name from employee where name LIKE 'J___' => 첫글자 J 이면서 네글자<br/>
* %로 시작 or _로 끝나는 => '\%%' or '%/_'<br/>

#

<h3>*(asterisk)</h3>
* 모든 튜플을 선택<br/>

#

<h3>주의</h3>
* SELECT로 조회할 떄 조건들을 포함해서 조회를 한다면 이 조건들과 관련된 attributes에 index가 걸려 있어야 함<br/>
