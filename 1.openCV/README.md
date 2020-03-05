# OpenCV

---

## 1. Basic

#### 1.1. [특정 색 영역  추출(얼굴/ ChromaKey)](https://github.com/shiney5213/SamsungMultiCampus/blob/master/1.openCV/200106_day1_OpenCV기초%2C크로마키.ipynb)

- bgr값 plot으로 확인

  ```
  b,g,r = cv2.split(img)
  plt.hist(x=b.ravel(), bins =256, range = [0,256], color = 'b')
  plt.hist(x=g.ravel(), bins =256, range = [0,256], color = 'g')
  plt.hist(x=r.ravel(), bins =256, range = [0,256], color = 'r')
  plt.show()
  ```

- Chromakey

  ```
  result = img.copy()
  mask = img.copy()
  
  for r in range(h.shape[0]):
      for c in range(h.shape[1]):
          hh = h[r,c]>= 55 and h[r,c]<= 65
          vv = v[r,c]>= 250 and v[r,c]<= 255
          ss = s[r,c]>= 210 and s[r,c]<= 220
  
          if not(hh and ss and vv):
              result[r, c, :]= img[r,c,:]
              mask[r,c,:] = 255
          else:
              result[r, c, :]= 0
              mask[r,c,:] = 0
  ```

 - 빈도수가 가장 높은 값 확인

   ``` 
   max_r = (np.where(hr[0]==np.max(hr[0])))[0][0]
   ```


#### 1.2. [화소 점처리](https://github.com/shiney5213/SamsungMultiCampus/blob/master/1.openCV/200107_day2_2.화소점처리%2C클래핑%2CLUT%2Cgif_file%2Cpil_한글처리(np.clip%2Cnp.LUT).ipynb)
-  선형 연산
   -  Null tranform : output (q)= input(p)
   -  사칙연산: 일정 값을 더하기, 빼기, 나누기, 곱하기
   -  영상의 반전영상: output(q) = 255 - input(p)
   -  np.clip() : 0~255값을 유지(255 이상은 255, 0 이하는 0)
- 비선형변환
  - LUT(Look Up Table, mapping table)
    - binary LUT
    - reverce LUT
    - posterise LUT
    - gamma LUT
- git 파일 만들기
- PIL로 한글 출력하기

#### 1.3. [화소 영역 처리](https://github.com/shiney5213/SamsungMultiCampus/blob/master/1.openCV/200108_day3_1.필터(다양한 필터%2C정규화%2C1차미분%2C2차 미분%2C엣지 검출%2C이상치 검출).ipynb)

#### 1.4. [공간 정보 인코딩(필터)](https://github.com/shiney5213/SamsungMultiCampus/blob/master/1.openCV/200108_day3_1.%ED%95%84%ED%84%B0(%EB%8B%A4%EC%96%91%ED%95%9C%20%ED%95%84%ED%84%B0%2C%EC%A0%95%EA%B7%9C%ED%99%94%2C1%EC%B0%A8%EB%AF%B8%EB%B6%84%2C2%EC%B0%A8%20%EB%AF%B8%EB%B6%84%2C%EC%97%A3%EC%A7%80%20%EA%B2%80%EC%B6%9C%2C%EC%9D%B4%EC%83%81%EC%B9%98%20%EA%B2%80%EC%B6%9C).ipynb)

- 화소 점처리: 픽셀 단위 값만 변경하는 것
- 화소 영역 처리: 픽셀 값과 그 주위 값(공간 영역) 연산
- 화소 마스크= 회선 필터 = 회선 처리 = 컨볼루션
- 회선 마스크: 주변 픽셀과의 평균 사용 
- 종류
	- 엠보싱
	- 블러링
	- 샤프닝
	- 경게선 검출(수직, 수평)
		- 1차 미분을 이용한 edge 검출
		- 2차 미분을 이용한 edge 검출
	- 잡음 제거
		- 가우시안 blur
		- 소벨 필터
		- median blur
	
#### 1.5.[analog to digital ](https://github.com/shiney5213/SamsungMultiCampus/blob/master/1.openCV/200108_day3_2.아날로그신호_to_디지털신호.ipynb)
-  표준화 단계
-  양자화 단계
-  부호화 단계

---
## 2. shape_detection

#### 2.1 [binary processing](https://github.com/shiney5213/SamsungMultiCampus/blob/master/1.openCV/200109_day4_1.binary_processing(threshold%2C).ipynb)
- binary threshold
	- cv2.threshold() :  histogram보고 thheshold 적용  
	- cv2.THRSHOLOD_OTSU: 역치값을 찾는 알고리즘 이용
	- cv2.adaptiveThreshold: adaptive threshole값 찾기
- noise 제거 후, threshold
	- GaussianBlur - threshole

#### 2.2. [shape detection](https://github.com/shiney5213/SamsungMultiCampus/blob/master/1.openCV/200109_day4_2.shape_detection(contour%2C%20morphologyEx).ipynb)
-  외곽선 검출
	- cv2.findContours() : 
	- cv2.drawContours(): 외곽선 그리기
- 외곽선 개수에 따라 도형 확인하기
	- cv2.approxPolyDP(): contours에서 꼭지점 개수 찾기

---

## 3. [OCR](https://github.com/shiney5213/SamsungMultiCampus/blob/master/1.openCV/200110_day5_1.ocr_program.ipynb)
- tesseract_ocr

