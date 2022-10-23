<h3>DBMS</h3>
* Database management system

<h3>metadata</h3>
* data about data
* ex) 사진 - 사진 해상도, 언제 찍은건지...
* catalog

<h3>query</h3>
* 데이터를 들고오기 위한 요청
* query -> 요청 파악 / 처리 -> 데이터 정의 / 데이터베이스 들고오기

<h3>data models</h3>
* DB구조를 기술하는데 필요한 개념 -> 추상화하여 사용

<h3>conceptual data models</h3>
* entity realtionship model
* ER diagram

<h3>logical data models</h3>
* 디테일하게 DB구조화
* 특정 DBMS나 storage에 종속되지 않는 수준
* relational data model

<h3>phisical data models</h3>
* 컴퓨터에 DB가 어떻게 파일 형태호 저장되는지 기술 수단

<h3>schema</h3>
* data model을 바탕으로 DB구조를 기술한 것
* schema는 DB설계 시 정해짐
* ex) student - id, name, major, grade

<h3>state</h3>
* 실제 data는 꽤 자주 바뀜!
* DB에 있는 현재 DB상태

<h3>three-schema architecture</h3>
* user application으로부터 물리적인 database를 분리시키는 조정

<h3>external schema</h3>
* 특정 유저들이 필요로 하는 데이터만 표현
* logical data model을 통해 표현

<h3>conceptual schema</h3>
* 전체 database 구조 기술
* internal 추상화

<h3>DBMS</h3>
* DML + VDL + DDL = SQL(relational DB language)
