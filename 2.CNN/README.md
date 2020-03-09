# CNN

---

## 1. [Deep Learning Q&A](https://github.com/shiney5213/SamsungMultiCampus/blob/master/2.CNN/200120_day1_1.Deep%20Learing(QnA).ipynb)

- 기계학습과 딥러닝의 차이점은?
- 경사하강법을 그림으로 표현하면?
- 가중치는 신경망의 어디에 해당하는가?
- 어떻게 다층으로 복잡한 문제를 풀 수 있는가?
- 다층학습이 어려운가?
- 활성화함수는 왜 비선형이어야 하는가?
- 시그모이드 함수의 장점은?
- y = wx + b에서 b는 왜 필요한가?
- 딥러닝의 핵심 돌파구는?
- 왜  CNN을 특징추출과 분류기의 결합으로 보는가?

---

## 2. 역행렬로 방정식 풀기
#### [최적해 구하기](https://github.com/shiney5213/SamsungMultiCampus/blob/master/2.CNN/200120_day1_2.%EC%B5%9C%EC%A0%81%ED%9A%8C%EA%B5%AC%ED%95%98%EA%B8%B0.ipynb)

- 역행렬 이용
	- 정방행렬일때: 역행렬이용
	- 정방행렬이 아닐때: pseudo inverse(슈도 역행렬, 의사역행렬)

---

## 3. 딥러닝으로 문제 풀기
#### 3.1. [XOR문제 풀기](https://github.com/shiney5213/SamsungMultiCampus/blob/master/2.CNN/200120_day1_3.DNN%EC%9C%BC%EB%A1%9C_XOR%EB%AC%B8%EC%A0%9C%ED%92%80%EA%B8%B0.ipynb)
- 단층 신경망 모델
- 다층 신경망 모델
	- 적합한 노드의 수: input 데이터 개수의 1.5~2배
	- plot으로 결과 살펴보기
	
<table>
	      <tr>
	      <td> <img src="images\3.xor_3.png"  /></td>
	      <td> <img src="images\3.xor_2.png"  /></td>
          <td> <img src="images\3.xor.png"  /></td>
    </tr>
</table>

#### 3.2. [Moon문제 풀기](https://github.com/shiney5213/SamsungMultiCampus/blob/master/2.CNN/200120_day1_4.DNN%EC%9C%BC%EB%A1%9C_MOON%EB%AC%B8%EC%A0%9C%ED%92%80%EA%B8%B0(LambdaCallback).ipynb)
- moon모양 데이터셋 그리기

<table>
    <tr>
    <td> <img src="images\3.moon.png"  /></td>
    <td> <img src="images\3.moon_2.png"  /></td>
    </tr>
</table>

---

## 4. MLP

#### 4.1. LambdaCallback

- epoch마다 출력되는 내용 제어

  ```
  from keras.callbacks import LambdaCallback
  def lambdaf_(epoch, logs, step) : 
      if epoch % step == 0 : print(f"{epoch} => {logs}")                
          
  def printepoch(step) :   
      return LambdaCallback(on_epoch_end=lambda epoch, logs: lambdaf_(epoch, logs, step))
      
  model = Sequential()
  model.add(Dense(5, input_dim = 2))
  model.add(Activation('relu'))
  model.add(Dense(1))
  model.add(Activation('sigmoid'))
  
  
  model.compile(loss='binary_crossentropy', optimizer="adam")  
  model.fit(x_data, y_data, batch_size=100, epochs=500, verbose=0,
            validation_data=(x_data, y_data),
            callbacks=[printepoch(100)]
           )
  ```
#### 4.2. activation함수

- LeakyReLU

```
from keras.layers import LeakyReLU

model = Sequential([
    Dense(5,activation = LeakyReLU(alpha=0.1), input_dim=2),
    Dense(10,activation = LeakyReLU(alpha=0.1)),
    Dense(10,activation = LeakyReLU(alpha=0.1)),
    Dense(10,activation = LeakyReLU(alpha=0.1)),
    Dense(10,activation = LeakyReLU(alpha=0.1)),
    Dense(10,activation = LeakyReLU(alpha=0.1)),
    Dense(1,activation = 'sigmoid'),    
])
```

- [Sigmoid](https://github.com/shiney5213/SamsungMultiCampus/blob/master/2.CNN/200120_day1_5.activation.ipynb)

#### [4.3.함수로 Sequential model만들기](https://github.com/shiney5213/SamsungMultiCampus/blob/master/2.CNN/200120_day1_6.creatModel()%EC%9D%B4%EC%9A%A9%ED%95%98%EC%97%AC_Sequential_model%EB%A7%8C%EB%93%A4%EA%B8%B0.ipynb)

```
def creatModel(layers, activation, input_dim):
    model = Sequential()
    d = layers.pop(0)
    model.add(Dense(d, activation = activation, input_dim = input_dim))
    for l in layers:
        model.add(Dense(l, activation = activation))
    model.add(Dense(1, activation = 'sigmoid'))
    return model
```

#### 4.4. [경사하강법](https://github.com/shiney5213/SamsungMultiCampus/blob/master/2.CNN/200121_day2_1.경사하강법%2C초기화문제.ipynb)
- sigmoid
- gradient vanishi문제

#### 4.5 초기화
- Xavier초기화

- He초기화

#### [4.6. 선형/ 비선형](https://github.com/shiney5213/SamsungMultiCampus/blob/master/2.CNN/200121_day2_3.%EC%84%A0%ED%98%95vs%EB%B9%84%EC%84%A0%ED%98%95%ED%95%A8%EC%88%98.ipynb)
- 왜 비선형으로 풀어야 하는가?
- 선형함수 조합의 한계
- 경사하강법을 이용한 최적화

---

## 5. [Advanced_MLP](https://github.com/shiney5213/SamsungMultiCampus/blob/master/2.CNN/200121_day2_2.Advanced_MLP.ipynb)

#### 5.1. basic model

```
model = Sequential()
model.add(Dense(50, input_shape = (784, )))
model.add(Activation('sigmoid'))
model.add(Dense(50))
model.add(Activation('sigmoid'))
model.add(Dense(10))
model.add(Activation('softmax'))

sgd = optimizers.SGD(lr = 0.001) 
model.compile(optimizer = sgd, loss = 'categorical_crossentropy', metrics = ['accuracy'])
history = model.fit(X_train, y_train, batch_size = 256, validation_split = 0.3, epochs = 200, verbose = 0)

```

#### 5.2. Initialization

- Xavier, HE Initialization

```
model.add(Activation('sigmoid'))    
model.add(Dense(50, kernel_initializer='he_normal'))  
```

  #### 5.3. Activation function(Nonlinearity)

```
model.add(Activation('relu'))    # use relu
```

#### 5.4. Optimizers

- Adam
- 모멘텀

```
adam = optimizers.Adam(lr = 0.001)                     # use Adam optimizer
    model.compile(optimizer = adam, loss = 'categorical_crossentropy', metrics = ['accuracy'])
```

#### 5.5. Batch Normalization

- 모든 입력을 다시 정규분포 형태로 만들기

- 비선형 변환 전에 주기

```
model.add(Dense(50, input_shape = (784, )))
model.add(BatchNormalization())       
model.add(Activation('sigmoid'))   
```

#### 5.6. Dropout

```
model.add(Dense(50, input_shape = (784, )))
model.add(Activation('sigmoid'))    
model.add(Dropout(0.5))   
```

#### 5.7. Model Ensemble

```
model1 = KerasClassifier(build_fn = mlp_model, epochs = 100, verbose = 0)
model2 = KerasClassifier(build_fn = mlp_model, epochs = 100, verbose = 0)
model3 = KerasClassifier(build_fn = mlp_model, epochs = 100, verbose = 0)

ensemble_clf = VotingClassifier(estimators = [('model1', model1), ('model2', model2), ('model3', model3)], voting = 'soft')

ensemble_clf.fit(X_train, y_train)
y_pred = ensemble_clf.predict(X_test)

```

<table>
	      <tr>
	      <td> <img src="images\5.model1.png"  /></td>
	      <td> <img src="images\5.model2.png"  /></td>
          <td> <img src="images\5.model3.png"  /></td>
          <td> <img src="images\5.model4.png"  /></td>
          <td> <img src="images\5.model5.png"  /></td>
    </tr>
</table>

---

## 6. [CNN](https://github.com/shiney5213/SamsungMultiCampus/blob/master/2.CNN/200121_day2_4.Advanced_CNN.ipynb)

#### 6.1. basic model

```

model.add(Conv2D(input_shape = (X_data.shape[1], X_data.shape[2], X_data.shape[3]), filters = 10, kernel_size = (3,3), strides = (1,1), padding = 'valid'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (2,2)))

model.add(Flatten())
model.add(Dense(50, activation = 'relu'))
model.add(Dense(10, activation = 'softmax'))

adam = optimizers.Adam(lr = 0.001)
model.compile(loss = 'categorical_crossentropy', optimizer = adam, metrics = ['accuracy'])
history = model.fit(X_train, y_train, batch_size = 50, validation_split = 0.2, epochs = 100, verbose = 0)


```

#### 6.2. Deep CNN

```
model = Sequential()
    
model.add(Conv2D(input_shape = (X_train.shape[1], X_train.shape[2], X_train.shape[3]), filters = 50, kernel_size = (3,3), strides = (1,1), padding = 'same'))
model.add(Activation('relu'))
model.add(Conv2D(filters = 50, kernel_size = (3,3), strides = (1,1), padding = 'same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Conv2D(filters = 50, kernel_size = (3,3), strides = (1,1), padding = 'same'))
model.add(Activation('relu'))
model.add(Conv2D(filters = 50, kernel_size = (3,3), strides = (1,1), padding = 'same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Conv2D(filters = 50, kernel_size = (3,3), strides = (1,1), padding = 'same'))
model.add(Activation('relu'))
model.add(Conv2D(filters = 50, kernel_size = (3,3), strides = (1,1), padding = 'same',kernel_initializer='he_normal'))                                                        # 초기화
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (2,2)))


model.add(Flatten())    
model.add(Dense(50, activation = 'relu', kernel_initializer='he_normal'))    # 초기화
model.add(Dense(10, activation = 'softmax'))

adam = optimizers.Adam(lr = 0.001)
model.compile(loss = 'categorical_crossentropy', optimizer = adam, metrics = ['accuracy'])
```

<table>
	      <tr>
	      <td> <img src="images\6.model_1.png"  /></td>
	      <td> <img src="images\6.model_2.png"  /></td>
    </tr>
</table>

#### 6.3 [CNN_Pratice : hand writing](https://github.com/shiney5213/SamsungMultiCampus/blob/master/2.CNN/200122_day3_1.CNN_practice(hard_handwriting_shape).ipynb)

- layer의 weight정보 확인

  ```
  w = model.layers[0].get_weights()
  print(w[0][:,:,0,0])
  plt.imshow(w[0][:,:,0,0])
  ```

- trainable 설정
```
for layer in model.layers:
    print(layer.trainable)
```
- 중간 output 결과 확인
```
conv_output = model.layers[0].output
conv_model = Model(model.input, conv_output)   
conv_pred = conv_model.predict(X_test)
sample_index = 1
plt.title('Input', {'fontsize': 20})
plt.imshow(X_test[sample_index,:,:,0])
```
<img src="images\6.output.png"  />

- 최종 결과물 확인(true, pred)

<img src="images\6.output2.png"  />

---

## 7.[ Data Augmentation](https://github.com/shiney5213/SamsungMultiCampus/blob/master/2.CNN/200122_day3_2.data_augmentation.ipynb)

#### 7.1 ImageDataGenerator.flow
- width_shift
- rescale
- horizontal_flip /vertical_flip 
- brightness_range
- rotation_range
- zoom_range
```
generator = tf.keras.preprocessing.image.ImageDataGenerator( 
    width_shift_range = 0.2,
    zoom_range=[0.5, 1.0],   
    horizontal_flip = True, vertical_flip = True,
    rotation_range=90,
    rescale=1./255)
obj = generator.flow(sample, batch_size=1)
```

<img src="images\7.augmentation.png"  />

#### 7.2.ImageDataGenarator.flow_from_dirictory()

```
obj = generator.flow_from_directory(
    train_path,
    target_size = (150, 150),   
    batch_size = 4,           # 45개 이미지 중에서 한번에 생성할 이미지 수 
    class_mode = 'binary',
    ave_prefix="image", save_format="jpg",save_to_dir='tmp'  # 저장가능
    )
```

#### 7.3. [Augmentation 예제(dog and cat)](https://github.com/shiney5213/SamsungMultiCampus/blob/master/2.CNN/200123_day4_1.Augmentation(dog_and_cat)%2Cmodel.save.ipynb)

```
train_datagen = ImageDataGenerator( rescale=1./255,
        						  shear_range=0.2,
                                    zoom_range=0.2,
                                    horizontal_flip=True)

# 검증 및 테스트 이미지는 a이미지 원본을 사용
validation_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

# 이미지를 배치 단위로 불러와 줄 generator
train_generator = train_datagen.flow_from_directory('./smallcatdog/train', 
                                                    target_size=(150, 150), 
                                                    batch_size=batch_size,
                                                    class_mode='binary') 

validation_generator = validation_datagen.flow_from_directory('./smallcatdog/validation',
                                                            target_size=(150, 150),
                                                            batch_size=batch_size,
                                                            class_mode='binary')

test_generator = test_datagen.flow_from_directory('smallcatdog/validation',
                                                    target_size=(150, 150),
                                                    batch_size=batch_size,
                                                    class_mode='binary')
model.fit_generator( train_generator,
                    steps_per_epoch=2000 // batch_size,    # 2000/16  한번에 125개씩 생성
                    epochs=5,  
                    validation_data=validation_generator,
                    validation_steps=800 // batch_size
```

#### 7.4 [Multi-classification](https://github.com/shiney5213/SamsungMultiCampus/blob/master/2.CNN/200123_day4_3.multi_classification(fruits).ipynb)

---

## 8. 기타

#### 8.1 model save & load

- architecture, weight 모두 저장
```
model2.save('bicycleship.h5')

from keras.models import load_model
model2 = load_model('smallcatdog.h5')
```
#### 8.2. imagenet에서 검색, 다운로드
- bs4, request, urlib 이용
```
page = requests.get("http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04194289") 
soup = BeautifulSoup(page.content, 'html.parser')
str_soup=str(soup)
split_urls=str_soup.split('\r\n')

def url_downalod(urls, path, prefix) :    
    idx = 0
    for url in urls :
        try:
            resp = urllib.request.urlopen(url)
            image = np.asarray(bytearray(resp.read()), dtype="uint8")
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)
            if ( len(image.shape)) == 3 :
                print(url)
                idx += 1
                save_path = path + '/' + prefix + str(idx)+'.jpg'
            	cv2.imwrite(save_path,image)
        except :
        	None
        	
url_downalod(bikes_split_urls, 'imagenet/bikes', 'bike')
```

---

## 9. Pretrained_CNN

#### 9.1.[pretrained_model](https://github.com/shiney5213/SamsungMultiCampus/blob/master/2.CNN/200123_day4_4.pretrained_model.ipynb)
- load_model

```
vgg_model = vgg16.VGG16(weights='imagenet', include_top = False)
inception_model = inception_v3.InceptionV3(weights='imagenet', include_top = False)
resnet_model = resnet50.ResNet50(weights='imagenet', include_top = False)
mobilenet_model = mobilenet.MobileNet(weights='imagenet', include_top = False)

```

- preprocessing

```
processed_image = vgg16.preprocess_input(image_batch.copy())

```

- predict

```
predictions = vgg_model.predict(processed_image)
```

- label 확인

```
label_vgg = decode_predictions(predictions, top=10)
print(label_vgg)
```

- 이미지 확인

<img src="images\9.pretrain_2.png"  />

#### 9.2 transfer Learning
- Freeze all the layers
```
for layer in vgg_conv.layers[:]:
    layer.trainable = False
for layer in vgg_conv.layers:
    print(layer, layer.trainable)
```

- model
```
model = models.Sequential()

model.add(vgg_conv)
model.add(layers.Flatten())
model.add(layers.Dense(1024, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(3, activation='softmax'))
```

<table>
	      <tr>
	      <td> <img src="images\9.transfer_1.png"  /></td>
	      <td> <img src="images\9.transfer_2.png"  /></td>
    </tr>
</table>

