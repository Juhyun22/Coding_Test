<h3>데이터 추가하기</h3>
* create table employee(); = table 만들기
* insert into employee values(값); = table에 넣은 순서대로 data 넣어주기
* show create table employee = table 확인(int인지)
* select * from employee; = 모든 데이터 출력

<h3>데이터 수정하기</h3>
* where id = 1; = id는 1일시에 확인
* set dept_id = 1003 where id = 1 = dept_id는 1003이고 id는 1일 시에
* update set salary = salary * 2 where dept_id = 3 => salary를 두배로 dept_id가 3일때
* update employee, works_on where employee.id = works_on.empl_id
* update table_name set attribute = value [where conditions] 

<h3>데이터 삭제</h3>
* delete from employee where id = 8;
