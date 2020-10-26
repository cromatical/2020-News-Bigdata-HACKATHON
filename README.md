# 2020_News_Bigdata_HACKATHON (2020.10.25) 

  - 📫 아이디어명 : 취업빽 (‘너는 앞만 보고 달려가면 돼, 우리가 너의 빽이 되어줄게’)
  - 📫 아이디어 개요 : “위기의 코로나 세대가 겪는 새로운 일자리 찾기의 어려움을 해결하기 위해 개인에게 맞는 전공별 취업 콘텐츠를 추천하는 커뮤니티 사이트 생성

# 🎈Makers
- 박성찬(팀장) : `기획`, 모델링, `데이터전처리`, `발표`
- 강민지       : 모델링, 데이터전처리, `알고리즘`, `웹` 
- 고정환       : `모델링`, `데이터전처리`, 알고리즘, 웹
- 이윤환       : `모델링`, 데이터전처리, `알고리즘`, 웹
- 이민기       : `기획`, 디자인, PT


## 💡 아이디어 발상 동기
  - **문제 제기** 
    - 매년 증가하는 청년 실업률과 그에 따라 파생되는 문제의 발생.
    - 대학 등 사용자에게 주어진 환경에 따라 접근할 수 있는 정보의 비대칭성. 
    - 너무 많은 정보 속에서 자신에게 필요한 정보를 획득하는 것의 어려움.
  
  - **인공지능(AI) 기술을 통한 개발 동기**
    - 정보의 홍수 시대 속에서 사용자의 전공과 취향에 맞는 정보 제공 필요.
    - 매일 생산되는 어마어마한 양의 뉴스 데이터들을 쉽게 처리 가능.
    - 지속적으로 누적되는 사용자의 데이터를 통해 정보 추천의 정확도 향상이 가능.

## 💡 아이디어 내용
  - **서비스 이용자**
    - 직무, 취업, 진로 등에 대한 정보가 필요한 모든 대상.
    - 대학생, 취준생, 이직준비자, 전공에 대한 지식이 필요한 자.
    
  - **핵심내용**
    - 사용자의 데이터를 통해 필요한 정보를 쉽고, 빠르게 맞춤화하여 제공.
    - 관심 있는 기사를 스크랩하고, 그에 따라 자신만의 포트폴리오 구축.
    - 전공 분야에 대한 DB 확보를 통해 그에 따른 Trend 보고서 제작.
    
  - **타 서비스와의 차별점**
    - 분산된 정보들을 하나의 Channel을 통해 보다 간편하게 획득.
    - 다양한 정보들에 대한 자신만의 기록 및 저장 데이터베이스 구축.
    - 특별한 노력을 하지 않고도 취업에 필요한 정보를 자동으로 획득.
    - 진로가 아닌 전공으로 파생된 정보들을 맞춤화하여 편의성 극대화.
  
## 💡 구현계획
    
  - **데이터 수집**(🔑 핵심키워드, 📰 뉴스데이터)
    - 🔑 빅카인즈에서 제공하는 API를 사용하여 뉴스데이터 수집
    - 🔑 전공별 일반화된 키워드를 얻기 위해 교육부, 커리어넷에 제시되어있는 전공 핵심키워드 추출.
    - 🔑 인기있고 빠르게 변화하는 트렌드가 적용되는 대학 커리큘럼을 통해 추가 전공 핵심키워드 추출.
    - 🔑 잡플래닛을 통해 직무별 핵심키워드를 추출.
    - 📰 빅카인즈 API 쿼리에 전공별 추출한 핵심키워드를 쿼리로 넣어서 뉴스데이터 수집
    - 📰 본문에 핵심키워드가 들어간 경우 한번만 언급되고 정작 본문은 관련없는 내용들이 많아서 타이틀에 핵심키워드가 포함된 뉴스데이터들만 수집. 적어도 본문의 내용을 대표하는 타이틀에 전공 핵심키워드가 포함이 되어있다면 본문은 그 이상의 내용을 내포하고 있을 것이다.  
    
  - **데이터 전처리** (📦 레이블링, ✂ 사용자에게 확실한 정보 제공을 위한 필터링)
    - 📦 516개의 전공을 유사한 전공끼리 그룹화 작업. => 44개의 큰 레이블로 그룹화
    - 📦 사용자에게 맞춤화된 추천을 위해 Textrank를 이용 => 본문내에 top10을 추출하여 전공 핵심키워드가 있으면 세부레이블로 지정(ex. 본문에 인공지능이 많이 언급되면 이 기사는 인공지능이라 세부레이블을 달아준다.)
    - ✂ 광고, 주식, 대학, 입학과 같은 광고성 글 제거.
    - ✂ 정보 전달력이 약한 300자 미만의 뉴스제거.
    - ✂ 추천에 방해가 되는 중복된 뉴스제거. 중복뉴스는 짧은 기간내에 제목이 매우 유사하다는 점을 이용하여 각 뉴스의 타이틀에서 명사만 추출해 추출한 키워드가 다른 뉴스타이틀에 얼마나 언급이 되었는지 점수를 측정하여 기준치 이상일 경우 중복뉴스로 판정하여 처리.
    
    
  - **모델링 구축**
    - 하루에 생산되는 방대한 양의 뉴스데이터를 AI를 이용하여 전공에 맞게 자동분류가 된다면 사용자는 보다 빠르고 편리하게 뉴스정보를 제공받을 수가 있다. 
    - 📰 학습에 필요한 뉴스데이터는 2010~2020년도 핵심키워드를 통해 추출한 뉴스데이터를 이용.
   
    - 🧱 Doc2vec + CNN 
    - 🧱 BERT
    - 🧱 GPT-2
    
    
  - **프로토타입** 
    - 시스템아키텍처
      ![시스템아키텍처](https://github.com/cromatical/2020_News_Bigdata_HACKATHON/blob/master/Image/%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98.png)
      ---
    - SW아키텍처
      ![SW아키텍처](https://github.com/cromatical/2020_News_Bigdata_HACKATHON/blob/master/Image/SW%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98.png)
      ---
    - 웹구현
      ![웹](https://github.com/cromatical/2020_News_Bigdata_HACKATHON/blob/master/Image/%EC%9B%B9.png)
      
## 💡 기대효과
  - 📃 서비스 전후의 차이점
    - 사용자들에게 필요한 취업 정보를 획득하는데 걸리는 시간 및 비용의 감소.
    - 대학 졸업 후, 오랜 기간 경력이 단절된 사람들에게도 최신 정보 제공.
    - 서비스를 통해 비수도권 지역의 취준생들도 질 높은 취업 정보 획득 가능.
    - 취업 관련된 정보들을 하나의 채널을 통해 관리하여 나만의 포트폴리오 제작.
    - 적성과 전공에 맞는 정보 습득을 통해 취업률 증가 및 이직률 감소 효과.
    
  - 📃 확장성
    - 고등학생들도 자신의 전공을 선택하기 전에 유용한 정보 획득이 가능.
    - 전공을 통한 정보 제공으로 진로 고민을 가진 저학년 대학생에게도 서비스 가능.
    - 전과, 복수전공 등 다른 전공에도 관심 있는 학생들에게 유용한 정보 제공.
    - 전공에 따른 사용자들의 커뮤니티 형성을 통해 자유로운 정보 공유.
    
## 💡 개발후기

        
    
