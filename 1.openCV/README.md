# OpenCV

---

## 1. Bacis

#### 1.1. [특정 색 영역  추출(얼굴/ ChromaKey)](https://github.com/shiney5213/SamsungMultiCampus/blob/master/OPENCV/200106_day1_OpenCV%EA%B8%B0%EC%B4%88%2C%ED%81%AC%EB%A1%9C%EB%A7%88%ED%82%A4.ipynb)

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
```

#### 1.2. 화소 점처리
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

#### 1.3.~4. 화소 영역 처리, 공간 정보 인코딩
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
	
#### 1.5. 
```