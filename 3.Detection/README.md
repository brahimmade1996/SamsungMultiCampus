# Detection

---

## 1. 특징점(Feature) 검출 알고리즘
#### 1.1. Haar Cascade
- 영역의 밝기 차들을 이용한 feature
- 다양한 형태의 elementary feature들을 다수 조합하여 물체에 대한 특징 추출
- [face detection](https://github.com/shiney5213/SamsungMultiCampus/blob/master/3.Detection/200128_day1_1.Face_Detection.ipynb)
- haar llight  + Ada boost + cascade

<table>
    <tr>
    <td><img src="images\1.haar_1.png"  /></td>
    <td><img src="images\1.haar_2.png"  /></td>
    </tr>
</table>

#### 1.2. HOG (Histogram Of Gradient)
- edge의 방향 히시트로그램 템플릿
- 영역을 일정한 셀로 분할하고 각 셀마다 edge픽셀들이 방향에 대한 히스토그램 구하기
- 히스토그램 bin값을 이용
- [people detection](https://github.com/shiney5213/SamsungMultiCampus/blob/master/3.Detection/200128_day1_2.full_body_detection(HOG_%EB%8F%99%EC%98%81%EC%83%81%EC%97%90%EC%84%9C%EA%B2%80%EC%B6%9C).ipynb)
- 강한 분류기 사용
 <img src="images\1.hog_1.png"  />

#### 1.3.  SIFT(Scale Invariant Feature Transform)
- 영상에서 코너점 등 식별이 용이한 특징점을 선택한 후, 각 특징점을 중심으로 한 로컬 패치에 대해 특징 벡터를 추출

#### 1.4. Ferns
- 영상에서 먼저 특징점들을 뽑고 각 특징점을 중심으로 로컬패치에 대해 계산

#### 1.5. LBP(Local Binary Pattern)
- 영상의 texture 분류, 얼굴 인식
- 각 픽셀의 주변 3 * 3 영역의 상대적인 밝기 변화를 2진수로 코딩한 인덱스값
- 각 셀마다 LBP에 대한 히스토그램을 일렬로 연결한 벡터를 최종 feature로 사용

#### 1.6. MCT(Modified cencus Transform)
- 얼굴 검출에서 가장 뛰어난 검출 성능
- LBP와 비슷

#### 1.7. [ORB](https://github.com/shiney5213/SamsungMultiCampus/blob/master/3.Detection/200128_day1_3.회전문제해결_ORB알고리즘%2CHomograph.ipynb)
- 회전 문제에 강함
- [비슷한 책 찾기](https://github.com/shiney5213/SamsungMultiCampus/blob/master/3.Detection/200128_day1_3.%ED%9A%8C%EC%A0%84%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0_ORB%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%2CHomograph.ipynb)

<table>
    <tr>
    <td><img src="images\1.orb.png"  /></td>
    <td><img src="images\1.orb_2.png"  /></td>
    </tr>
</table>

1.8. Homography

- 원본의 코너점이 어디에 있는지 찾을 때

- 카메라 회전되었을 때 사진보고 얼마나 변형해야 하는지 찾을 때

<table>
      <tr>
      <td><img src="images\1.homo_1.png"  /></td>
      <td><img src="images\1.homo_2.png"  /></td>
          <td><img src="images\1.homo_3.png"  /></td>
      </tr>
  </table>

---

## 2. YOLO

#### 2.1. [YOLO test](https://github.com/shiney5213/SamsungMultiCampus/blob/master/3.Detection/200128_day1_4.yolo.ipynb)

- 리눅스 서버에서 YOLO  test 하기

<table>
      <tr>
      <td><img src="images\2.yolo_1.png"  /></td>
      <td><img src="images\2.yolo_2.png"  /></td>
      </tr>
  </table>

#### 2.2. [YOLO 개념](https://github.com/shiney5213/SamsungMultiCampus/blob/master/3.Detection/200128_day1_5.yolo_test.ipynb)
- 기존의 detection: sliding window, region proposal
- NMSThreshold: 근처에 있는 픽셀이 같은 물체/ 다른 물체
- Rounding box에 대한 regression
- output layer: 3개

#### 2.3. [동영상에 YOLO 적용](https://github.com/shiney5213/SamsungMultiCampus/blob/master/3.Detection/200129_day2_2.%EB%8F%99%EC%98%81%EC%83%81%EC%97%90%EC%84%9C_yolo%EC%A0%81%EC%9A%A9%ED%95%98%EA%B8%B0.ipynb)

- opencv로 동영상 만들기
- 동영상에 YOLO 적용
- [셀 단위로 classID 그리기](https://github.com/shiney5213/SamsungMultiCampus/blob/master/3.Detection/200129_day2_3.셀단위로classID그리기%2C동영상에yolo적용하기.ipynb))

<table>
    <tr>
    <td><img src="images\2.yolo_3.png"  /></td>
    <td><img src="images\2.yolo_4.png"  /></td>
    </tr>
</table>

---

## 3. [Segmentation: MRCNN](https://github.com/shiney5213/SamsungMultiCampus/blob/master/3.Detection/200130_day3_2.SEGMENTATION(MRCNN).ipynb)

- RPN(Region Proposal Network)
- ROI(Regoin Of Interest)
- IOU

<table>
    <tr>
    <td><img src="images\3.mrcnn.png"  /></td>
    <td><img src="images\3.mrcnn_2.png"  /></td>
    </tr>
</table>

---

## 4. [Pose Detection](https://github.com/shiney5213/SamsungMultiCampus/blob/master/3.Detection/200130_day3_3.openpose.ipynb)

<table>
    <tr>
    <td><img src="images\4.pose_1.png"  /></td>
    <td><img src="images\4.pose_2.png"  /></td>
    </tr>
</table>

---

## 5. 기타

- [서버에서 jupyter notebook 사용하기](https://github.com/shiney5213/SamsungMultiCampus/blob/master/3.Detection/200129_day2_1.서버에서_주피터노트북_실행하기.ipynb)
- [openCV에서 keras에서 만든 모델 사용하기](https://github.com/shiney5213/SamsungMultiCampus/blob/master/3.Detection/200130_day3_1.kerasmodel을_opencv에서_활용하기위해pb형식으로변환.ipynb)

