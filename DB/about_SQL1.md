<h3>SQL</h3>
* structured query language
* table / column / row / domain
* SQL에서 relation = multiset of tuples(중복 허용한 table)
* SQL & RDBMS = 실제 구현에 강제가 없음! 사용하는 RDBMS의 언어를 사용하면 됨!

<h3>예제</h3>
* IT회사 관련 RDB만들기 by MySQL(InnoDB)
* show databases; = db에 뭐가 있는지 보여줌
* create database company; = company db 생성
* select database(); = 사용중인 database 출력
* use company; = company database 사용 -> 활성화됨
* drop database company; = compant databse 사용 안함

<h3>database vs schema</h3>
* MySQL에서는 DATABASE와 SCHEMA가 같은 뜻을 의미
* 다른거 -> schema가 database의 namespace를 의미

<h3>company database 만들기</h3>
* ex) department - id, name, leader_id(사원번호)
* create table department(id INT PRIMARY_KEY,..., leader_id int int);
* 정수, 부동 소수점 방식(고정에 비해 정확하지 않음), 고정 소수점 방식(실수 정확하게 저장)
* 고정 크기 문자열(char), 가변 크기 문자열(varchar), 사이즈가 큰 문자열(tinytext, text, mediumtext, longtext)
* 날짜(DATE), 시간(TIME), 날짜와 시간(DATETIME, TIMESTAMP UTC)

<h3>primary key</h3>
* table의 tuple을 식별하기 위해 사용
* 선언 - int ID primary key, primary key(id, name)
* unique key - 중복된 값을 가질 수 없음
* Not Null - Null일 수 없다
* default 10 = 값이 없을 때 10을 넣어라
* check = 제한사항 .. ex) check (age >= 20)
* foreign key = 기준 id, references, on delete 옵션, on update 옵션

