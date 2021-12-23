# Computer Application Design MSA

컴퓨터 응용 설계 마이크로서비스 아키텍쳐 설계  과제 

구현자 홍성민

기타 서브 웹 서비스 및 API 연동 및 AWS EC2 배포 및 스웜 연동 및 HealthCheck 개발

구현 도움: 한상우, 배준일

스웜 연동 중 발생하는 이슈 확인 및 동적 자원 할당을 위한 컨테이너 구축

Computer Application Design MSA Project at Korea Polytechnic University

## 사용자 서비스 및 운영 층 모듈 설명

- 사용자의 [메인 포털 사이트](http://ec2-3-34-48-86.ap-northeast-2.compute.amazonaws.com/) 접속 이후 각자의 서브 서비스 사용 -> 홍성민
- 서비스
	- [오늘의 기술 스택](http://ec2-3-34-48-86.ap-northeast-2.compute.amazonaws.com/) -> 홍성민
	- [EPL 순위 정보](http://ec2-3-34-48-86.ap-northeast-2.compute.amazonaws.com:8001/rank) -> 한상우
	- [일정 관리 앱](http://ec2-3-34-48-86.ap-northeast-2.compute.amazonaws.com:8004/example-webapp/main.jsp) -> 임혜진
	- [오늘의 장터](http://ec2-3-34-48-86.ap-northeast-2.compute.amazonaws.com:8002/goods/list) -> 배준일
	로 연동 되어 있다. 

- 자원 관리 모듈
	- 도커 스웜 및 도커 스택 모니터링 툴
		- [Main Grafana](http://ec2-3-34-48-86.ap-northeast-2.compute.amazonaws.com:3000/d/zr_baSRmk/docker-swarm-services?refresh=30s&orgId=1)
	- 헬스 체크 모듈(결함 포용)
		- [health-check]()
	- 로드 밸런서(동적 자원 할당)
		- [dynamic-allocation]()


## 동작 방법
1. [메인 포털](http://ec2-3-34-48-86.ap-northeast-2.compute.amazonaws.com/)로 이동
2. 작동 확인


## 진행 상황
- [x] 한상우 팀원의 [football](https://github.com/comungsul/football) 앱 서비스와의 연동 -> 12/3
- [x] 기본적인 UI 구성 및 도커 컴포즈 설정 
- [x] 홍성민 팀원의 기업 기술 스택 검색 서비스 연동 
- [x] 임혜진 팀원의 블로그 서비스 연동
- [x] 배준일 팀원의 장터 서비스 연동
- [x] EC2 배포 및 Docker Swarm 설정 
- [x] 이거 제가 1주일도 할 시간 없는거 아시죠?
- [x] 모니터링 설정 및 테스트
- [x] 로드 밸런싱 및 네트워크 과부하 시 관리
## Contributors 
[홍성민(PM)](https://github.com/KKodiac) 

[배준일](https://github.com/bjo6300)

[한상우](https://github.com/sktkddn777)

[박태민](https://github.com/Taemin0624)

[임혜진](https://github.com/imagine99)

