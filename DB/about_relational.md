<h3>set</h3>
* 서로 다른 elements를 가지는 collection
* relation in marhematics .. Cartesian product(set X1와 Xn의 관계 = 부분집합)
* 각각의 list = tuple

<h3>relational data model</h3>
* ex) student
* domain 정하기 - id, names, grade, major, phone_number, emergency_number(비상 연락망)
* domain of student relation - 각각의 domain들이 어떻게 서로 attribute하는지
* 가장 잘 나타낸 것이 table
* domain - value들의 set(더 이상 나누어 지지 않아야 함)
* attribute - domain이 relation에서 맡은 역할 이름

<h3>relation schema</h3>
* relation의 구조
* ex) student(id, name, ...)
* degree - attribute의 수(id, name, .. 이것들 수!)
* relation = set of tuples(table)
* relational database = relation data model에 기반한 구조화된 database
* relation database schema = relation schemas set + integrety consntrate set

<h3>relation 특징들</h3>
* 중복된 tuple을 가질 수 없다
* attribute의 key 가 있음 = id
* tuple 순서는 중요하지 않다
* attribute의 이름 중복 안됨
* attribute는 atomic해야한다(나눠질 수 없음) .. ex) 서울특별시 강남구 청담동 / 전공, 부전공 나눠서 저장

<h3>null의 의미</h3>
* 값이 없음
* 값이 어떤게 들어올지 모름

<h3>keys</h3>
* relation에서 tuples를 unique하게 식별할 수 있는 attributes set
* candidate key = 어느 한 attribute라도 제거하면 unique하게 tuples를 식별할 수 없는 super key
* primary key = relation에서 tuples를 unique하게 식별하기 위한 key
* unique key = primary key가 아닌 candidate key = alternate key
* foreign key = 다른 relation의 pk를 참조하는 attribute
* constraints = relation이 지켜야하는 규약사항 - ex) tuple은 unique하다
* domain, key, null value, entity integrity, referential integrity constraints가 있음 
* constraints = 위반하면 에러 뜸! 조심하셈!!
