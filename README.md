# Computer Application Design MSA

컴퓨터 응용 설계 마이크로서비스 아키텍쳐 설계  과제 

Computer Application Design MSA Project at Korea Polytechnic University


## Prerequisites
연동이 잘 되는지 테스트를 하기 위해서 해당 저장소를 참고 하고 있다면,

각자 개인이 개발한 컨테이너가 몇번 포트에 돌고 있는지 확인 해야 합니다.

만약 개인이 맡은 서비스 구성이 끝나면 PM인 저에게 말씀해 주시면 제가 설정 및 연동 진행 하겠습니다.


## Installation
별도의 설치는 필요 없습니다.
단지 docker-compose 로 컨테이너를 실행해 주세요
```bash
    docker-compose up -d
```

localhost:5001 에서 확인하면 해당 웹 앱이 돌고 있는 걸 확인 할 수 있습니다.
 
## Settings
배포 및 최종적으로는 각각의 서비스가 하나의 EC2 Instance에서 실행 될 것이기 때문에 포트 할당의 문제가 없겠으나,

 제가 임시로 연동 시에는 포트가 제한되어 있으니 아래를 참고해 주세요.

```
현재 할당 된 포트 번호
5001[app.py: 메인 포털 사이트]
27017[football: mongodb]
8081[football: mongodb-express]
8001[football: fastapi/web]
```

## 진행 상황
- [x] 한상우 팀원의 [football](https://github.com/comungsul/football) 앱 서비스와의 연동 -> 12/3
- [x] 기본적인 UI 구성 및 도커 컴포즈 설정 -> 12/3
- [ ] 홍성민 팀원의 기업 기술 스택 검색 서비스 연동 -> ~ing
- [ ] 임혜진 팀원의 블로그 서비스 연동
- [ ] 박태민 팀원의 날씨 서비스 연동
- [ ] 배준일 팀원의 장터 서비스 연동
- [ ] EC2 배포 및 Docker Swarm 설정
- [ ] 이거 제가 1주일도 할 시간 없는거 아시죠?
- [ ] 모니터링 설정 및 테스트
- [ ] 로드 밸런싱 및 네트워크 과부하 시 관리
## Contributors 
[홍성민(PM)](https://github.com/KKodiac)

[배준일](https://github.com/bjo6300)

[한상우](https://github.com/sktkddn777)

[박태민](https://github.com/Taemin0624)

[임혜진](https://github.com/imagine99)

