# FRESHKEEP : 식자재 관리 웹앱
## 기획 개요
* 기획 목표 : 유통기한이 지난 식자재나 유통기한이 임박한 식자재를 파악하고 효율적으로 관리하여, 식자재의 낭비를 최소화하기 위해 만들어진 웹앱

* 사용기술
  + Frontend: Svelte, TailwindCSS, flowbite-svelte
  + Backend: Django, Django Ninja

## 기획 상세
### FRONTEND
- 기능
  + **식품 관리**: 사용자가 냉장고에 있는 식품을 추가, 수정, 삭제
  + **카테고리 관리**: 식품을 카테고리별로 분류하고, 활성/비활성 상태를 관리
  + **유통 기한 추적**: 유통 기한이 임박한 식품을 쉽게 확인
  + **다양한 단위 지원**: 다양한 단위를 지원하여 식품의 양을 관리
  + **반응형 디자인**: 다양한 화면 크기에서 최적화
  + **음식 기록** : 사용자 식사 기록을 DIARY형태로 저장하고 기록

- 사용방법
  + **MAIN page**: 각 카테고리 별 음식 이름, 양, 유통기한의 정보를 한눈에 확인가능
      - **Add Food**: 각 카테고리 음식 옆 + 버튼을 누르면 음식 추가
      - **Food Detail**: 각 카테고리별 음식 정보를 누르면 각 카테고리 별 상세 정보 확인
          - **Delete Food**: 상세 정보 하단에 DELETE버튼
          - **Edit Food**: 상세 정보 하단에 EDIT 버튼
  + **MY REFRIGERATOR page**: 카테고리별 활성/비활성 조절 가능
  + **FOOD DIARY page**: 사용자 음식 기록 페이지

- 주요 파일 및 디렉토리 
  + static: 정적 파일 (이미지, HTML 파일 등)
  + src: 소스 코드 디렉토리
    + lib/fetchData.js: API 호출을 위한 유틸리티 함수
    + routes: 페이지 컴포넌트
      - food_diary/+page.svelte: 식품 일기 페이지
      - my_refrigerator/+page.svelte: 냉장고 관리 페이지
      - receipe/+page.svelte: 레시피 페이지
      - +page.svelte: 메인 페이지 컴포넌트
      - +layout.svelte: navbar
      - loading.svelte: 로딩 애니메이션 컴포넌트
      - modal_detail.svelte: 식품 상세 정보 모달 컴포넌트
      - modal_edit.svelte: 식품 수정 모달 컴포넌트
      - app.html: 애플리케이션의 HTML 템플릿

- 설치
  1. clone the repository
     ```
     git clone https://github.com/your-username/freshkeep-frontend.git
     ```
  2. install dependencies
     ```
      cd refrigerator1-frontend
     ```
  3. open the project in your browser
    ```
    npm run dev -- --port 9526
      ```

### BACKEND
- DB소개(MODEL 소개)
  - **Category (카테고리)   **
      name: 카테고리 이름 (예: VEGETABLES, DRINKS)   
      img_url: 카테고리 아이콘의 URL   
      isactive: 카테고리 활성화 상태 (기본값: True)
  - **FoodUnit (식품 단위)  ** 
      name: 단위 이름 (예: 개, 조각, L)
  - **FoodItem (식품 항목) **   
      category: 카테고리 (외래 키)   
      foodname: 식품 이름   
      volume: 식품의 양   
      unit: 단위 (외래 키)   
      expiration_date: 유통 기한   
      purchase_date: 구매 날짜 (기본값: 현재 날짜)   
      
- API 엔드포인트
  - **카테고리 엔드포인트**
    - GET /api/foods/categories   
      기능: 모든 카테고리 가져오기   
      응답: List[CategorySchema]
      
    - PUT /api/foods/categories/{category_id}   
      기능: 카테고리 업데이트   
      요청: CategorySchema   
      응답: CategorySchema

  - **식품 단위 엔드포인트**
    - GET /api/foods/foodunits   
      기능: 모든 식품 단위를 가져오기   
      응답: List[FoodUnitSchema]
      
  - **식품 항목 엔드포인트**
    - GET /api/foods/fooditems   
      기능: 모든 식품 항목을 가져옴   
      응답: List[FoodItemSchema]
    

    - POST /api/foods/fooditems   
      기능: 새로운 식품 항목 생성   
      요청: FoodItemCreateSchema   
      응답: FoodItemSchema
      
    - PUT /api/foods/fooditems/{fooditem_id}   
      기능: 특정 식품 항목 업데이트   
      요청: FoodItemSchema   
      응답: FoodItemSchema
    
    - DELETE /api/foods/fooditems/{fooditem_id}   
      기능: 특정 식품 항목 삭제   
      응답: 204 No Content
      
    - PATCH /api/foods/fooditems/{fooditem_id}/update_volume   
      기능: 특정 식품 항목의 양 업데이트   
      요청: VolumeUpdateSchema   
      응답: FoodItemSchema
      
- 설치
  1. install django-ninja
     ```
     pip install django django-ninja
     ```
  2. migration DB
     ```
      python manage.py makemigrations
      python manage.py migrate
     ```
  3. run server
    ```
    python manage.py runserver 10.125.208.187:9526
    ```

  
